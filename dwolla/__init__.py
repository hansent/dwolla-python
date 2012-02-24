import json
import urllib
import requests
import datetime


class DwollaAPIError(Exception):
    pass


class DwollaClientApp(object):

    def __init__(self, client_id, client_secret, scope="accountinfofull"):
        self.client_id = client_id
        self.client_secret = client_secret
        self.api_url = "https://www.dwolla.com/oauth/rest/"
        self.auth_url = "https://www.dwolla.com/oauth/v2/authenticate"
        self.scope = "balance|contacts|transactions|request|send|accountinfofull"

    def init_oauth_url(self, redirect_uri=None, scope=None, response_type='token'):
        params = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'response_type': response_type,
            'scope' : self.scope
        }
        if redirect_uri: params['redirect_uri'] = redirect_uri
        return "%s?%s" % (self.auth_url, urllib.urlencode(params))

    def api_request(self, resource, **params):
        params['client_id'] = self.client_id
        params['client_secret'] = self.client_secret
        url = "%s/%s" % (self.api_url, resource)
        return requests.get(url, params=params)

    def get(self, resource, **params):
        resp = self.api_request(resource, **params)
        resp = json.loads(resp.content)
        if resp['Success'] == False:
            raise DwollaAPIError(resp['Message'])
        return resp['Response']

    def get_account_info(self, account_id):
        return self.get("users/%s" % account_id)

    def get_spots_nearby(self, lat='41.59', lon='-93.62', range=10, limit=10):
        return self.get("contacts/nearby",
            latitude = lat,
            longitude = lon,
            range = range,
            limit  = limit )


class DwollaUser(object):

    def __init__(self, access_token):
        self.api_url = "https://www.dwolla.com/oauth/rest"
        self.access_token = access_token

    def api_get(self, resource, **params):
        url = "%s/%s" % (self.api_url, resource)
        params['oauth_token'] = self.access_token
        return requests.get(url, params=params)

    def api_post(self, resource, data):
        url = "%s/%s"(self.api_url, resource)
        headers = {'Content-Type': 'application/json'}
        data['oauth_token'] = self.access_token
        data=json.dumps(data)
        return requests.post(url, data=data, headers=headers)

    def get(self, resource, **params):
        resp = self.api_get(resource, **params)
        resp = json.loads(resp.content)
        if resp['Success'] == False:
            raise DwollaAPIError(resp['Message'])
        return resp['Response']

    def get_account_info(self):
        return self.get("users")

    def get_balance(self):
        return self.get("balance")

    def get_contacts(self, search=None, types=None, limit=None):
        params = {}
        if search: params['search'] = search
        if types:  params['types'] = types
        if limit:  params['limit'] = limit
        return self.get("contacts", **params)

    def get_transaction(self, transaction_id):
        return self.get("transactions/%s" % int(transaction_id))

    def get_transaction_list(self, since=None, types=None, limit=None, skip=None):
        if type(since) == datetime.datetime:
            since = since.strformat("%m-%d-%Y")
        params = {}
        if since: params['sinceDate'] = since
        if types: params['types'] = types
        if limit: params['limit'] = limit
        if skip:  params['skip'] = skip
        return self.get("transactions", **params)

    def get_transaction_stats(self, types=None, start_date=None, end_date=None):
        if type(start_date) == datetime.datetime:
            start_date = start_date.strformat("%m-%d-%Y")
        if type(end_date) == datetime.datetime:
            end_date = end_date.strformat("%m-%d-%Y")
        params = {}
        if types: params['types'] = types
        if types: params['startDate'] = start_date
        if types: params['endDate'] = end_date
        self.get("transactions/stats", **params)




