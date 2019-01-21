from marketplace.models.shop import Shop
from marketplace.models import db

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
    error = ""
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
        item_type = type(shop_info["items"][items])
        item_count = shop_info["items"][items]

        if not isinstance(shop_info["items"][items], int):
            status["error_msg"] = "The item [{}] has an inventory type of [{}].Type should be a positive int".format(
                items, item_type)
            return status

        if int(item_count) < 0:
            status["error_msg"] = "The item [{}] has a negative inventory count. Please have a positive inventory".format(
                items)
            return status

    # Adding shop to database
    try:
        shop = Shop(shop_info=json.dumps(shop_info))

        db.session.add(shop)
        db.session.commit()

        status["success"] = True
        return status
    except:
        # TODO: Add better exception handling;
        # Need to handle non JSON format error
        error = "create shop has failed"
        status["error_msg"] = error
        print(error)
        pass

    return status

# TODO: Create a task to update shop inventory count from the vendor side
