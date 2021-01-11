from tap_officernd.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()


class MembersStream(BaseStream):
    API_METHOD = 'GET'
    TABLE = 'members'
    KEY_PROPERTIES = ['_id']

    @property
    def path(self):
        return '/members'
