from tap_officernd.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()


class MembershipsStream(BaseStream):
    API_METHOD = 'GET'
    TABLE = 'memberships'
    KEY_PROPERTIES = ['_id']

    @property
    def path(self):
        return '/memberships'
