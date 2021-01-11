from tap_officernd.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()


class PaymentsStream(BaseStream):
    API_METHOD = 'GET'
    TABLE = 'payments'
    KEY_PROPERTIES = ['_id']

    @property
    def path(self):
        return '/payments'
