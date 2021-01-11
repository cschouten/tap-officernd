from tap_officernd.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()


class ChargesStream(BaseStream):
    API_METHOD = 'GET'
    TABLE = 'charges'
    KEY_PROPERTIES = ['_id']

    @property
    def path(self):
        return '/charges'
