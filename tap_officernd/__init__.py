#!/usr/bin/env python3

import singer

import tap_framework

from tap_officernd.client import OfficerndClient
from tap_officernd.streams import AVAILABLE_STREAMS

LOGGER = singer.get_logger()  # noqa


class OfficerndRunner(tap_framework.Runner):
    pass


@singer.utils.handle_top_exception(LOGGER)
def main():
    args = singer.utils.parse_args(required_config_keys=[
        'client_id',
        'client_secret',
        'organization',
        'custom_fields'])
    client = OfficerndClient(args.config)
    runner = OfficerndRunner(args, client, AVAILABLE_STREAMS)

    if args.discover:
        runner.do_discover()
    else:
        runner.do_sync()


if __name__ == '__main__':
    main()
