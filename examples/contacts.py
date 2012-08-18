# Include the Dwolla REST Client
from dwolla import DwollaClientApp, DwollaUser

# Include any required keys
import _keys

# Instantiate a new Dwolla User client
# And, Sseed a previously generated access token
DwollaUser = DwollaUser(_keys.token)

'''
    EXAMPLE 1: 
      Fetch last 10 contacts from the 
      account associated with the provided
      OAuth token
'''
contacts = DwollaUser.get_contacts()
print(contacts)


'''
    EXAMPLE 2: 
      Search through the contacts of the
      account associated with the provided
      OAuth token
'''
contacts = DwollaUser.get_contacts('Ben')
print(contacts)