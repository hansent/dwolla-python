# Include the Dwolla REST Client
from dwolla import DwollaUser

# Include any required keys
import _keys

# Instantiate a new Dwolla User client
# And, Sseed a previously generated access token
DwollaUser = DwollaUser(_keys.token)

'''
    EXAMPLE 1: 
      Send money ($1.00) to a Dwolla ID 
'''
transaction = DwollaUser.send_funds(1.00, '812-626-8794', _keys.pin)
print(transaction)


'''
    EXAMPLE 2: 
      Send money ($1.00) to an email address, with a note
'''
transaction = DwollaUser.send_funds(1.00, 'michael@dwolla.com', _keys.pin, 'Everyone loves getting money', None, None, "Email")
print(transaction)