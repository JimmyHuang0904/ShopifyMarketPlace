# Flask related imports
from flask import Blueprint, render_template, flash, request, redirect, url_for, jsonify
from flask_login import login_user, logout_user, login_required, current_user

# Expose database
from marketplace.models import db

# Tasks specific for shop
import marketplace.tasks.shop_tasks as shop_tasks

# Register routes as blueprints to be seen from our app
shop = Blueprint('shop', __name__)


# TODO: We can do a variable named shop in the future to have multiple
# shops that exist in our system's database. We will have 1 simple shop for now
# @shop.route("/shops/<shop_registered_uuid>")
@shop.route("/shop/list")
@shop.route("/shop/")
@login_required
def view_shop():
    shops = shop_tasks.get_shop_items()

    return render_template('shop/shop_list.html', shops=shops)


# Do a POST request to /shop/add_shop with a JSON formatted data
# that is defined in marketplace/models/shop.py to register a new shop
# See doc/example_add_shop/*.json
@shop.route("/shop/add_shop", methods=["GET", "POST"])
@login_required
def add_shop():
    if request.method == 'POST':
        status = shop_tasks.create_shop(request.json)

        # There was an error adding the shop to our marketplace;
        # Either it does not follow the conventional protocol we defined
        # or that there exist a negative inventory count
        if not status["success"]:
            return status["error_msg"]

        return jsonify(request.json)
    else:
        flash("HTTP request was a {} request. Try doing a POST request".format(
            request.method))
        return redirect(url_for(".view_shop"))


# Do a POST request to /shop/purchase with a JSON formatted data
# that is defined:
# {
#     "shop_id" : <#>,
#     "items"    : {
#         "tables" : "all",
#         "chairs" : "1"
#     }
# }
# See doc/example_purchase/*.json
@shop.route("/shop/purchase", methods=["GET", "POST"])
@login_required
def purchase_request():
    if request.method == 'POST':
        status = shop_tasks.purchase_request(request.json)

        if not status["success"]:
            return status["error_msg"]

        return jsonify(request.json)
    else:
        flash("HTTP request was a {} request. Try doing a POST request".format(
            request.method))
        return redirect(url_for(".view_shop"))

# NOTE: We could probably refactor purchase_request and add_shop with a callback function
# since the only difference is the shop_tasks. We choose not to do this yet because they may
# have very different protocols and methods in the future
