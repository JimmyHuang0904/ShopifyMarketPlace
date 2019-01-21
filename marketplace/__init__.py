from flask import Flask, render_template
# Blueprints
from marketplace.controllers.main import main
from marketplace.controllers.shop import shop

from marketplace.models import db
from marketplace.extensions import login_manager


def create_app(object_name):
    app = Flask(__name__)

    # print(object_name))
    # TODO: Fix this
    # app.config.from_object('marketplace.settings.ProdConfig')
    # app.config['DEBUG'] = True
    # app.config['TESTING'] = True

    # TODO: NEED TO FIX THIS WITH CONFIG
    # Set the secret key to some random bytes. Keep this really secret!
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://///home/jimmy/GitHub/ShopifyMarketPlace/example.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # initialize SQLAlchemy
    db.init_app(app)

    login_manager.init_app(app)

    # Register blueprints
    app.register_blueprint(main)
    app.register_blueprint(shop)

    return app


class ExampleTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
