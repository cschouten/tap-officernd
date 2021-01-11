from tap_officernd.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()


class FloorsStream(BaseStream):
    API_METHOD = 'GET'
    TABLE = 'floors'
    KEY_PROPERTIES = ['_id']

    @property
    def path(self):
        return '/floors'
