# Include the Dwolla REST Client
from dwolla import DwollaClientApp

# Include any required keys
import _keys

# Instantiate a new Dwolla User client
# And, Sseed a previously generated access token
Dwolla = DwollaClientApp(_keys.apiKey, _keys.apiSecret)

'''
    EXAMPLE 1: 
      Register a new Dwolla user
'''
user = Dwolla.register_user(email="michael@dwolla.com", password="Thr0wAwayPassword", firstName="Michael", lastName="Schonfeld", address="902 Broadway St.", address2="Floor 4", city="New York", state="NY", zip=10010, dateOfBirth="01/01/1960", phone="5551231234", pin="1234")
print(user)