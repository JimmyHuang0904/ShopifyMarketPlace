# ShopifyMarketPlace

#--------------------------
#   Quick Launch Guide
#--------------------------

##### SETUP ENVIRONMENT

# We use pipenv to wrap our modules nicely for other developers

pipenv install

pipenv shell


##### FLASK RELATED SETUP

#### On Linux Development

# Need to add environment variable for Flask
export FLASK_APP=manager.py

#### On Windows Development
C:\path\to\app>set FLASK_APP=manager.py

#### Running the Flask
python -m flask run
