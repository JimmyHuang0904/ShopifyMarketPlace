#!/usr/bin/env python3
import os
from flask_script import Manager
from flask_script.commands import ShowUrls, Clean

from marketplace import create_app
from marketplace.models import db

env = os.environ.get('MARKETPLACE_ENV', 'dev')
app = create_app('marketplace.settings.{}Config'.format(env.capitalize()))

manager = Manager(app)

# This command can be used to clean artifacts and cache files like .pyc
manager.add_command("clean", Clean())

# This command shows all the endpoints available to do HTTP requests
manager.add_command("show-urls", ShowUrls())


@manager.command
def createdb():
    """ Creates a database with all of the tables defined in
          your SQLAlchemy models
    """
    with app.app_context():
        db.create_all()


if __name__ == "__main__":
    manager.run()
