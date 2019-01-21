from flask import Flask, render_template
# Blueprints
from marketplace.controllers.main import main
from marketplace.controllers.shop import shop

from marketplace.models import db
from marketplace.extensions import login_manager


def create_app(object_name):
    app = Flask(__name__)

    app.config.from_object(object_name)

    # initialize SQLAlchemy
    db.init_app(app)

    # Login interface added, LDAP client/server support have not been incorporated
    # yet so that you can just login in with no password.
    login_manager.init_app(app)

    # Register blueprints
    app.register_blueprint(main)
    app.register_blueprint(shop)

    return app
