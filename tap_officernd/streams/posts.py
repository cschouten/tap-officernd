from tap_officernd.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()


class PostsStream(BaseStream):
    API_METHOD = 'GET'
    TABLE = 'posts'
    KEY_PROPERTIES = ['_id']

    @property
    def path(self):
        return '/posts'
