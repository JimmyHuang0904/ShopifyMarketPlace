##
# This file models a shop
##

from . import db
import json


# We want to model a shop like this JSON example:
# {"shop":
#     {
#         "items":{
#             "table" : 1,
#             "chair" : 2
#         },
#         "name": "<name_of_shop>",
#         "description": "<description>"
#     }
# }


class Shop(db.Model):

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    shop_info = db.Column(db.String())

    # TODO: Try to test using constructor to create new shops
    def __init__(self, shop_info):
        self.shop_info = shop_info
        print(shop_info)
        print(type(shop_info))

    def __shop_info(self):
        return json.loads(self.shop_info)

    def name(self):
        return self.__shop_info().get("name")

    def description(self):
        return self.__shop_info().get("description")

    def items(self):
        return self.__shop_info().get("items")
