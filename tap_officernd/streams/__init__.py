from tap_officernd.streams.bookings import BookingsStream
from tap_officernd.streams.charges import ChargesStream
from tap_officernd.streams.checkins import CheckinsStream
from tap_officernd.streams.credits import CreditsStream
from tap_officernd.streams.events import EventsStream
from tap_officernd.streams.fees import FeesStream
from tap_officernd.streams.floors import FloorsStream
from tap_officernd.streams.members import MembersStream
from tap_officernd.streams.memberships import MembershipsStream
from tap_officernd.streams.offices import OfficesStream
from tap_officernd.streams.payments import PaymentsStream
from tap_officernd.streams.plans import PlansStream
from tap_officernd.streams.posts import PostsStream
from tap_officernd.streams.resource_types import ResourceTypesStream
from tap_officernd.streams.resources import ResourcesStream
from tap_officernd.streams.teams import TeamsStream
from tap_officernd.streams.visits import VisitsStream


AVAILABLE_STREAMS = [
   BookingsStream,
   CheckinsStream,
   ChargesStream,
   CreditsStream,
   EventsStream,
   FeesStream,
   FloorsStream,
   MembersStream,
   MembershipsStream,
   OfficesStream,
   PaymentsStream,
   PlansStream,
   PostsStream,
   ResourceTypesStream,
   ResourcesStream,
   TeamsStream,
   VisitsStream
]

__all__ = [
   'BookingsStream',
   'ChargesStream',
   'CheckinsStream',
   'CreditsStream',
   'EventsStream',
   'FeesStream',
   'FloorsStream',
   'MembersStream',
   'MembershipsStream',
   'OfficesStream',
   'PaymentsStream',
   'PlansStream',
   'PostsStream',
   'ResourceTypesStream',
   'ResourcesStream',
   'TeamsStream',
   'VisitsStream'
]
