from tap_officernd.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()


class FeesStream(BaseStream):
    API_METHOD = 'GET'
    TABLE = 'fees'
    KEY_PROPERTIES = ['_id']

    @property
    def path(self):
        return '/fees'
