# ShopifyMarketPlace

#--------------------------
#   Quick Launch Guide
#--------------------------

##### Firebase access to read and write from developmental server

<!-- You need to set your own credentials by following this instruction

GOOGLE_APPLICATION_CREDENTIALS -->

##### SETUP ENVIRONMENT

Make sure to have pipenv installed for an isolated virtual environment

pip install pipenv

# We use pipenv to wrap our modules nicely for other developers

pipenv install

pipenv shell


# Using sqlite
sudo apt-get install sqlite

##### FLASK RELATED SETUP

#### On Linux Development

# Need to add environment variable for Flask
export FLASK_APP=manager

#### On Windows Development
C:\path\to\app>set FLASK_APP=manager.py

##### Running the Flask App
#### On Development Server Locally
flask run

#### Externally Visible Server to Local Network
flask run --host=0.0.0.0





##### KNOWN ISSUES
If you ever encounter an error running the server due to accessing the database with sqlite3 import error like so:
![png]

This means that either your python version has been corrupted and an installation is needed (since by default
sqlite3 should be included). It is recommended to follow these steps:
https://stackoverflow.com/questions/27470530/how-to-import-sqlite3-in-my-python3-4-successfully
