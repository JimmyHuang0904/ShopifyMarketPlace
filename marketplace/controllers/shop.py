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
@shop.route("/shop/add_shop", methods=["GET", "POST"])
@login_required
def add_shop():
    if request.method == 'POST':
        shop_tasks.create_shop(request.json)
        return jsonify(request.json)
    else:
        print(request.method)
        return "HTTP request was a {} request. Try doing a POST request".format(request.method)
