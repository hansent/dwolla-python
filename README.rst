=============================
Python wrapper for Dwolla API
=============================
A simple python wrapper for `Dwolla's <http://www.dwolla.com>`_ `API's <https://www.dwolla.com/developers>`_.

Usage
=====

Basic Usage::

        from dwolla import DwollaClientApp
        
        client =  DwollaClientApp(APP_ID, APP_SECRET)
        
        #get some basic info on an account
        client.get_account_info("thomas.hansen@gmail.com") 
        client.get_account_info("812-451-5647") 

        #returns a list of nearby dwolla spots
        client.get_nearby_spots(lat='41.59', lon='-93.62')  


Examples
-----------

You can also check out the examples for more usage examples.  To try flask-app
just install flask, edit settings.cfg (or copy it to local file 
"settings.cfg.local") and run::
        
        $ python examples/flask-app/main.py



Getting OAuth Tokens
----------------------

The flask-app shows you how to get OAuth tokens and use them.  The basic
steps are as follows::
    
        from dwolla import DwollaClientApp
        client =  DwollaClientApp(APP_ID, APP_SECRET)
        
        #redirect your user to dwolla oauth url
        auth_url = app.init_oauth_url(scope="AccountInfoFull")
        redirect(auth_url)


Then when the user is redirected back to your page::

        code = request.args.get("code")
        access_token = dwolla_app.get_oauth_token(code)


With a valid access token, you can do anything your scope allows::

        #create user object with access token
        user = DwollaUser(access_token)

        #get account info, balance, etc
        info = user.get_account_info()
        balance = user.get_balance()

        #send some money to thomas :P specifying amount, receiverID and PIN
        user.send_funds(10.0, "812-647-0748", '1234')


TODO 
====
Documentation & Packaging
-------------------------
 - sphynx documentation

Endpoints
---------
Register
 - Register User

Examples
--------
 - flask or appengine exmaple with oauth flow
 - qr code checkout?



REFERENCES
==========
https://www.dwolla.com/developers



LICENSE
=======
This code is licensed under the MIT license.  For a copy of the license,
check the LICENSE file.

