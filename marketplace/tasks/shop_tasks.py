from marketplace.models.shop import Shop
from marketplace.models import db

from sqlalchemy import func
import json


def get_shop_items():
    shop_items = Shop.query.all()

    return shop_items


# We can do a lot of error checking on creation of a shop because we can assume that the vendor
# won't need to create multiple shops. We may as well take care of the minor details to make sure
# required fields are being filled up, such as:
#
# "name"  : Name of the shop; so it would be their company name. There should not be any duplicates
# "items" : To have a shop, the assumption is that there are at least one item available.
#           We also make sure that there are no negative inventory counts
def create_shop(shop_info):
    status = {"success": False, "error_msg": ""}

    if "name" not in shop_info:
        status["error_msg"] = "Please add a [name] field to declare the name of your shop"
        return status

    # TODO: Add duplicate name of shop checking so that there will be no two shops with the same name
    # is_duplicate = db.session.query(Shop.shop_info)
    # print(is_duplicate)
    # if is_duplicate:
    #     status["error_msg"] = "Name of the shop has already been taken, please have a new name"
    #     return status

    # Error Checking if POST request has valid fields; if not, then the shop will not be added
    if "items" not in shop_info:
        status["error_msg"] = "There are no [items] listed in the shop; Shop will not be added"
        return status

    for items in shop_info["items"]:
        item_count_type = type(
            shop_info["items"][items].get("inventory", None))
        item_price_type = type(shop_info["items"][items].get("price", None))
        item_count = shop_info["items"][items].get("inventory", -1)
        item_price = shop_info["items"][items].get("price", -1)

        # TODO: Refactor this later
        if not isinstance(item_count, int):
            status["error_msg"] = "The item [{}] has an inventory type of [{}].Type should be a positive int".format(
                items, item_count_type)
            return status

        if not isinstance(item_price, int):
            status["error_msg"] = "The item [{}] has an inventory type of [{}].Type should be a positive int".format(
                items, item_count_type)
            return status

        if int(item_count) < 0:
            status["error_msg"] = "The item [{}] has a negative inventory count. Please have a positive inventory".format(
                items)
            return status

        if int(item_price) < 0:
            status["error_msg"] = "The item [{}] has a negative price. Please have a positive price".format(
                items)
            return status

    # Adding shop to database
    try:
        shop = Shop(shop_info=json.dumps(shop_info))

        db.session.add(shop)
        db.session.commit()

        status["success"] = True
    except:
        status["error_msg"] = "Create shop has failed; Database may corrupted. Try resetting the database"

    return status

# TODO: Create a task to update shop inventory count from the vendor side

# TODO: Create a task to delete shops using DELETE request


def purchase_request(purchase_info):
    # Status to return back. Error message will be returned on illegal transactions
    status = {"success": False, "error_msg": ""}

    # Key constants defined in the JSON; TODO: Refactor these constants elsewhere
    shop_id = "shop_id"
    items = "items"
    price = 0

    if shop_id not in purchase_info:
        status["error_msg"] = "Please add a valid [{}] field to purchase from that shop".format(
            shop_id)
        return status

    # Find the shop with the specific shop_id we requested
    shop = Shop.query.get(purchase_info[shop_id])

    # Shop does not exist
    if not shop:
        status["error_msg"] = "Shop_id [{}] does not exist. Purchase failed".format(
            purchase_info[shop_id])
        return status

    purchase_items = purchase_info.get(items, None)

    if not purchase_items:
        status["error_msg"] = "Purchase transaction has no listed items"
        return status

    shop_information = json.loads(shop.shop_info)
    shop_items = shop_information[items]
    for purchase_item in purchase_items:
        if purchase_item not in shop_items:
            status["error_msg"] = "Shop_id [{}] does not have the item [{}]. Purchase failed".format(
                purchase_info[shop_id], purchase_item)
            return status

        purchase_amount = purchase_items[purchase_item]
        shop_inventory = shop_items[purchase_item]["inventory"]

        # This allows you to purchase all at once
        if purchase_amount == 'all':
            price += shop_items[purchase_item]["price"] * \
                shop_inventory
            shop_items[purchase_item]["inventory"] = 0
            continue

        # Check if request is made in integer values
        if not isinstance(purchase_amount, int):
            status["error_msg"] = "The item [{}] has an type of [{}].Type should be a positive int. Purchase failed".format(
                purchase_item, type(purchase_amount))
            return status

        # Check if the purchase request has illegal values
        if purchase_amount <= 0:
            status["error_msg"] = "The amount of item [{}] you want to purchase is less than 1. Entered amount was [{}]. Purchase failed".format(
                purchase_item, purchase_amount)
            return status

        # Check if the purchase request is more than inventory stock
        if purchase_amount > shop_inventory:
            status["error_msg"] = "The amount of item [{}] you want to purchase is more than the available inventory in stock [{}]. Purchase failed".format(
                purchase_item, shop_inventory)
            return status
        else:
            shop_items[purchase_item]["inventory"] -= purchase_amount
            price += purchase_amount * shop_items[purchase_item]["price"]

    # Update our dictionary
    shop_information[items].update(shop_items)
    # Dump to string for shop_info to be updated to the database
    shop.shop_info = json.dumps(shop_information)

    try:
        db.session.commit()
        status["success"] = True
        status["error_msg"] = "Your purchase was $[{}] dollar. Enjoy!".format(
            price)
    except:
        status["error_msg"] = "Purchasing from shop [{}] has failed; Database may corrupted. Try resetting the database".format(
            purchase_info[shop_id])

    return status
