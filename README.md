# Shopify MarketPlace

This web app is created using Python with Flask. It utilizes **pipenv** to create a isolated virtual env for nicely packaging between different environments. There is also an example.db in this directory that can be inspected and used.

This app utilizes **RESTful API** to create transactions we call a "shopping cart" between multiple shops that are defined in the example.db. Specifically, POST requests can be used to add new shops, and do purchases with any valid amount of each item in a given shop.

There are example valid JSON POST requests for adding new shops in doc/example_add_shop_json/ *, and example valid JSON POST requests for making purchases in doc/example_purchase/ *



##   Quick Launch Guide

##### SETUP ENVIRONMENT

Make sure to have pipenv installed for an isolated virtual environment.

```
pip install pipenv
```

##### We use pipenv to wrap our modules nicely for other developers

You can install the packages listed in the Pipfile into the virtual env by running: 

```
pipenv install
```

To launch your virtual env so that you can launch the app,

```
pipenv shell
```



### FLASK RELATED SETUP

##### On Linux

We need to add environment variable to tell Flask what app we are running.

```
export FLASK_APP=manager.py
```

##### On Windows
```
C:\path\to\app>set FLASK_APP=manager.py
```



##### Switching Between Development/Production Server

By default, running the app will be on development server. You can change to production server by

```
export MARKETPLACE_ENV=prod
```

or back to development server:

```
export MARKETPLACE_ENV=dev
```

### Running the App

To see all the possible commands usage, use this command

```
python manager.py --help
```

Which will display the options and run using:

```
python manager.py <command>
```

| Command   | Description                                                  |
| --------- | ------------------------------------------------------------ |
| clean     | Remove *.pyc and other collateral artifacts generated for caching |
| show-urls | Display all of the URL matching routes for the project (Routes explained more in details later) |
| createdb  | Generates the minimum blank database. By default, it will create an empty Users and no Shops table in the database. Shops will have to be populated through add shops POST requests (explained later). You do not need to use this command, I have created an example.db that you can further append to. |
| runserver | This runs the Flask server in development/production mode    |

### File Hierarchy



### Recommended Installs for Testing

#### Inspecting the example.db file
We can inspect the database with a gui easily with sqlitebrowser. To install,

```
sudo apt-get install sqlitebrowser
```

Then, you can run

```
sqlitebrowser example.db
```

This will allow you to be able to see values clearly in the database.



#### Installing Boomerang on your Google Extension

I use 

[Boomerang]: https://chrome.google.com/webstore/detail/boomerang-soap-rest-clien/eipdnjedkpcnlmmdfdkgfpljanehloah?hl=en

To test my HTTP Requests and mostly to send JSON POST requests really fast.



### Known Issues and Fixes

If you ever encounter an error running the server due to accessing the database with sqlite3 import error like the one shown in the picture below:
![](/home/jimmy/GitHub/ShopifyMarketPlace/doc/img/database_error.png)

This means that either your python version has been corrupted and an installation is needed (since by default
sqlite3 should be included). It is recommended to follow these steps:
https://stackoverflow.com/questions/27470530/how-to-import-sqlite3-in-my-python3-4-successfully