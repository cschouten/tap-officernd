from tap_officernd.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()


class TeamsStream(BaseStream):
    API_METHOD = 'GET'
    TABLE = 'teams'
    KEY_PROPERTIES = ['_id']

    @property
    def path(self):
        return '/teams'
