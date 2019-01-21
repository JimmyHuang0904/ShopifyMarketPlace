# ShopifyMarketPlace

#--------------------------
#   Quick Launch Guide
#--------------------------

##### SETUP ENVIRONMENT

Make sure to have pipenv installed for an isolated virtual environment

pip install pipenv

# We use pipenv to wrap our modules nicely for other developers

pipenv install

pipenv shell


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
