#######################################
# This file models a shop
#######################################

from . import db
import json


# We want to model a shop like this JSON example:
# {
#     "items":{
#         "table" : {
#             "inventory" : 1,
#             "price"     : 3
#         },
#         "chair" : {
#             "inventory" : 3,
#             "price"     : 10
#         }
#     },
#     "name": "<name_of_shop>",
#     "description": "<description>"
# }


class Shop(db.Model):

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    shop_info = db.Column(db.String())

    def __init__(self, shop_info):
        self.shop_info = shop_info

    def __shop_info(self):
        return json.loads(self.shop_info)

    def name(self):
        return self.__shop_info().get("name")

    def description(self):
        return self.__shop_info().get("description")

    def items(self):
        return self.__shop_info().get("items")
