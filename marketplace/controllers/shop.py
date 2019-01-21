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


# @login_required
@shop.route("/shop/new.json")
@shop.route("/shop/new")
def view_shop():
    shop_items = shop_tasks.get_shop_items()
    return jsonify(shop_items)
    # return render_template('dashboard.html')
