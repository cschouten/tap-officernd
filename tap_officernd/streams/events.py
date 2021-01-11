from tap_officernd.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()


class EventsStream(BaseStream):
    API_METHOD = 'GET'
    TABLE = 'events'
    KEY_PROPERTIES = ['_id']

    @property
    def path(self):
        return '/events'
