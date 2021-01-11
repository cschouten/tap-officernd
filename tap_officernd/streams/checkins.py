from tap_officernd.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()


class CheckinsStream(BaseStream):
    API_METHOD = 'GET'
    TABLE = 'checkins'
    KEY_PROPERTIES = ['_id']

    @property
    def path(self):
        return '/checkins'
