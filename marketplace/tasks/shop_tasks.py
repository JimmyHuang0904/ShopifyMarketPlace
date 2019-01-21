from marketplace.models.shop import Shop
from marketplace.models import db

import json


def get_shop_items():
    # TODO: Replace with json formatted from db
    shop_items = Shop.query.all()

    print(shop_items)
    return shop_items


def create_shop(shop_info):
    try:
        shop = Shop(shop_info=json.dumps(shop_info))
        db.session.add(shop)
        db.session.commit()
    except:
        # TODO: Add better exception handling;
        # Need to handle non JSON format error
        print("create shop has failed")
        pass
