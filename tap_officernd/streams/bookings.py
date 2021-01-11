from tap_officernd.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()


class BookingsStream(BaseStream):
    API_METHOD = 'GET'
    TABLE = 'bookings'
    KEY_PROPERTIES = ['_id']

    @property
    def path(self):
        return '/bookings'
