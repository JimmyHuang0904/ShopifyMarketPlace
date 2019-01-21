##
# Expose database to models
##

from firebase_admin import db
import firebase_admin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# We are going to use cloud database instead to store
# shop items so that we can access it anywhere easily
# through a generic protocol.

firebase_admin.initialize_app(options={
    'databaseURL': 'https://shopify-market-ba24f.firebaseio.com/'
})
