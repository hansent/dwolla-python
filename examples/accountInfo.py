# Include the Dwolla REST Client
from dwolla import DwollaClientApp, DwollaUser

# Include any required keys
import _keys

# Instantiate a new Dwolla User client
# And, Sseed a previously generated access token
Dwolla = DwollaClientApp(_keys.apiKey, _keys.apiSecret)
DwollaUser = DwollaUser(_keys.token)

'''
    EXAMPLE 1: 
      Fetch account information for the
      account associated with the provided
      OAuth token
'''
me = DwollaUser.get_account_info()
print(me)


'''
    EXAMPLE 2: 
      Fetch basic account information
      for a given Dwolla ID
'''
me = Dwolla.get_account_info('812-626-8794')
print(me)


'''
    EXAMPLE 3: 
      Fetch basic account information
      for a given Email address
'''
me = Dwolla.get_account_info('michael@schonfeld.org')
print(me)
