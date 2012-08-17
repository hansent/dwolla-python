import os
from pprint import pprint
from dwolla import DwollaClientApp, DwollaUser

DWOLLA_APP_ID = os.environ['DWOLLA_APP_ID']
DWOLLA_APP_SECRET = os.environ["DWOLLA_APP_SECRET"]
ACCESS_TOKEN = os.environ['DWOLLA_ACCESS_TOKEN']

client = DwollaClientApp(DWOLLA_APP_ID, DWOLLA_APP_SECRET)
print("ACCOUNT LOOKUP:")
pprint(client.get_account_info("thomas.hansen@gmail.com"))
print("NEARBY SPOTS:")
pprint(client.get_nearby_spots())

user = DwollaUser(ACCESS_TOKEN)
print("\n\nACCOUNT INFO:")
pprint(user.get_account_info())
print("\n\nBALANCE:")
pprint(user.get_balance())
print("\n\nCONTACTS:")
pprint(user.get_contacts())
print("\n\nTRANSACTIONS:")
pprint(user.get_transaction_list())
print("\n\nTRANSACTION STATS:")
pprint(user.get_transaction_stats())
