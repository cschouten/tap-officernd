from tap_officernd.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()


class ResourcesStream(BaseStream):
    API_METHOD = 'GET'
    TABLE = 'resources'
    KEY_PROPERTIES = ['_id']

    @property
    def path(self):
        return '/resources'
