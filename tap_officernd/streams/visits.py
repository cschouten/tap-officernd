from tap_officernd.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()


class VisitsStream(BaseStream):
    API_METHOD = 'GET'
    TABLE = 'visits'
    KEY_PROPERTIES = ['_id']

    @property
    def path(self):
        return '/visits'
