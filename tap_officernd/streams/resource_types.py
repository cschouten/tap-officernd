from tap_officernd.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()


class ResourceTypesStream(BaseStream):
    API_METHOD = 'GET'
    TABLE = 'resource_types'
    KEY_PROPERTIES = ['_id']

    @property
    def path(self):
        return '/resource-types'
