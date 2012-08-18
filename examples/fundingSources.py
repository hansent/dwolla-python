# Include the Dwolla REST Client
from dwolla import DwollaUser

# Include any required keys
import _keys

# Instantiate a new Dwolla User client
# And, Sseed a previously generated access token
DwollaUser = DwollaUser(_keys.token)

'''
    EXAMPLE 1: 
      Fetch all funding sources for the
      account associated with the provided
      OAuth token
'''
sources = DwollaUser.get_funding_sources()
print(sources)


'''
    EXAMPLE 2: 
      Fetch detailed information for the
      funding source with a specific ID
'''
source = DwollaUser.get_funding_source('pJRq4tK38fiAeQ8xo2iH9Q==')
print(source)
