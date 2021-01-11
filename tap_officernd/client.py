import requests
import json
import singer
import singer.metrics

LOGGER = singer.get_logger()


class OfficerndClient:

    MAX_TRIES = 5

    def __init__(self, config):
        self.config = config

    def oauth2(self):
        url = 'https://identity.officernd.com/oauth/token'
        data = {
            'client_id': self.config['client_id'],
            'client_secret': self.config['client_secret'],
            'grant_type': 'client_credentials',
            'scope': 'officernd.api.read'
        }
        # TODO Import client_id and client_secret values from client.py
        response = requests.post(url, data=data)
        access_token = response.json()['access_token']
        #print("client.py, access_token: ", access_token)
        return access_token

    def make_request(self, url, method, params=None, body=None):
        LOGGER.info("Making {} request to {}".format(method, url, params))

        response = requests.request(
            method,
            url,
            headers={
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + self.oauth2(),
            },
            params=params,
            json=body)

        if response.status_code != 200:
            LOGGER.info('status={}'.format(response.status_code))
            raise RuntimeError(response.text)
        return response.json()

