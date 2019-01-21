#!/usr/bin/env python3

import os

from flask_script import Manager

from marketplace import create_app
from marketplace.models import db

env = os.environ.get('MARKETPLACE_ENV', 'dev')
app = create_app('marketplace.settings.{}Config'.format(env.capitalize()))

manager = Manager(app)


@manager.command
def createdb():
    """ Creates a database with all of the tables defined in
          your SQLAlchemy models
    """
    db.create_all()


if __name__ == "__main__":
    manager.run()
