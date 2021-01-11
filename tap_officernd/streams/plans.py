from tap_officernd.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()


class PlansStream(BaseStream):
    API_METHOD = 'GET'
    TABLE = 'plans'
    KEY_PROPERTIES = ['_id']

    @property
    def path(self):
        return '/plans'
