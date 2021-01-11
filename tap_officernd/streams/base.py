import singer
import singer.utils
import singer.metrics

from tap_officernd.config import get_client_id, get_client_secret

from tap_framework.streams import BaseStream as base

LOGGER = singer.get_logger()


class BaseStream(base):
    KEY_PROPERTIES = ['id']

    def get_url(self):
        return 'https://app.officernd.com/api/v1/organizations/saltbox{}'.format(self.path)

    def get_body(self):
        body = {}
        # print("Get Body: ", body)
        # print("Update Body: ", body.update(self.custom_body()))
        body.update(self.custom_body())

        return body

    def custom_body(self):
        return {}

    def get_params(self):
        return {}

    def sync_data(self):
        table = self.TABLE

        LOGGER.info('Syncing data for {}'.format(table))
        access_token = self.client.oauth2()
        #print("base.py, access_token value: ", access_token)
        url = self.get_url()
        params = self.get_params()
        body = self.get_body()
        #print("Sync Data: ", body)

        while True:
            response = self.client.make_request(url, self.API_METHOD, params=params, body=body)
            transformed = self.get_stream_data(response)

            with singer.metrics.record_counter(endpoint=table) as counter:
                singer.write_records(table, transformed)
                counter.increment(len(transformed))

            # page_number = body['page_number']
            LOGGER.info('Synced page {} for {}'.format(1, table))

            # if len(transformed) == 0:
            #     break
            # else:
            #     body['page_number'] += 1
            #     self.save_state(transformed[-1])

            return

    def get_start_date(self):
        bookmark = get_last_record_value_for_table(self.state, self.TABLE)
        print("Get Start Date: ", bookmark)
        if bookmark:
            return bookmark
        else:
            return get_config_start_date(self.config)

    def save_state(self, last_record):
        if 'date_modified' in last_record:
            date_modified = last_record['date_modified']
            self.state = incorporate(self.state, self.TABLE, "date_modified", date_modified)
            save_state(self.state)

    def get_stream_data(self, response):

        transformed = []
        for record in response:
            ## removes fields with missing/wrong data type
            record = self.transform_record(record)
            transformed.append(record)

        return transformed

