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

```
example.db										// Database
manager.py										// Main app server
Pipfile											// Dependencies for pipenv
Pipfile.lock
README.md
marketplace/
	__init__.py									// create_app instantiation
	settings.py									// config settings
	controllers/								// app routes
		__init__.py
		main.py									// main login and dashboard
		shop.py									// shop dashboard
	tasks/
		__init__.py								// main related tasks
		shop_tasks.py							// shop related back-end tasks
	models/
		__init__.py
		shop.py									// models the shop database
		user.py									// models a user for database
	templates/
		shop/
			shop_list.html
			shop_template.html
		base.html
		dashboard.html
		login.html
		marketplace.html
		nav.html
	static/
	extensions.py								// extra extensions
	forms.py									// forms
doc/
	example_add_shop_json/				// Example POST Requests to /shop/add_shop
		example1.json
		example2.json
	example_purchase_json/				// Example POST Requests to /shop/purchase
		example3.json
		example4.json
		example5.json
```



### JSON Requests

#### Example.db

The example.db in the repo should allow you to see 4 shops by default. It should look something like this:

![](/home/jimmy/GitHub/ShopifyMarketPlace/doc/img/list_of_shops.png)

#### Adding Shops with Inventory and Prices

You can easily add a new shop to the database through a POST request onto /shop/add_shop. There are several fields that have to be set, otherwise the Response will throw an error regarding the bad request to add shop.

```
{
    "items": {
        "mercedes": {
            "inventory": 5,
            "price": 15000
        },
        "volkswagen": {
            "inventory": 21,
            "price": 10000
        },
        "BMW": {
            "inventory": 13,
            "price": 30000
        }
    },
    "name": "Local Car Dealer",
    "description": "Cars for Sale"
}
```

In this example, we can describe which fields are needed. A shop would not be a shop without items to sell, so there has to be at least one field item in **"items"**. 

Also, **"prices"** and **"inventory"** numbers have to be set to a positive number. If any of these are set to negative numbers, the response from the request will tell you the exact error and the shop will not be created.

Lastly, the shop needs a **"name"**, because it doesn't make sense to have a shop with no names.

#### Purchasing Items at Different Stores

Looking at the list of shops at /shop/list, you can now decide what you want to purchase! As long as there are 1 or more outstanding shops that has at least 1 positive inventory count, you should be able to make a purchase. To purchase, you need to send a POST request to /shop/purchase. Here are some example fields that you need in order to complete the handshake:

```
{
    "shop_id": 1,
    "items": {
        "table": "all",
        "chair": 2
    }
}
```

We need a way to determine which shop we are purchasing items from. We have a **"shop_id"** tag to determine the shop; these will be listed on /shop/list. Then, you will need at least 1 item in the **"items"** field  that corresponds to the shop_id's items (otherwise the purchase will not go through). You can specify a quantity less than or equal to the inventory of the shop, or **"all"** to purchase the remaining inventory of that product. If you try to purchase more than the stock inventory or a negative amount, an error will be thrown and purchase will be nulled. Upon success, the response should tell you the price of the purchase and update the database to reflect the purchase. Refreshing the list of shops will show the newly updated inventory count.

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