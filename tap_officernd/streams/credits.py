from tap_officernd.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()


class CreditsStream(BaseStream):
    API_METHOD = 'GET'
    TABLE = 'credits'
    KEY_PROPERTIES = ['_id']

    @property
    def path(self):
        return '/credits'
