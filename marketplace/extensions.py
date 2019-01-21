#!/usr/bin/env python

######################################################################################################
# Description: This file is to add on extra extensions for flask operations
#              such as login and celery
######################################################################################################

from flask_login import LoginManager
from marketplace.models.user import User


###################################################
### Using Flask_login to create a Login Manager ###
###################################################

# TODO look for generation of good secret key,
# By default Flask-Login uses sessions for authentication
login_manager = LoginManager()
login_manager.login_view = "main.login"
login_manager.login_message_category = "warning"


@login_manager.user_loader
def load_user(userid):
    return User.query.get(userid)
