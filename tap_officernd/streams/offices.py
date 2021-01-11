from tap_officernd.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()


class OfficesStream(BaseStream):
    API_METHOD = 'GET'
    TABLE = 'offices'
    KEY_PROPERTIES = ['_id']

    @property
    def path(self):
        return '/offices'
