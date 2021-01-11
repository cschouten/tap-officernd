import singer


LOGGER = singer.get_logger()  # noqa


def get_client_id(config):
    client_id = config.get('client_id')
    return client_id


def get_client_secret(config):
    client_secret = config.get('client_secret')
    return client_secret


def get_organization(config):
    organization = config.get('organization')
    return organization


def get_custom_fields(config):
    fields = config.get('custom_fields')
    return fields


# data = {
#   "client_id": "wahya3SR2NN16p3V",
#   "client_secret": "7mjIVNsHInBfwgBI2eYoVE7E6GtXDjBz",
#   "organization": "saltbox",
#   "custom_fields": {"Access Pass": "Members", "License Plate":  "Members", "Parking Permit": "Members"}
# }
#
#
# fields = data['custom_fields']
# for field, category in fields:
#     print(field)

