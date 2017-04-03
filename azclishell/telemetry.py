""" use telemetry to measure ux key bindings """

import datetime

from applicationinsights import TelemetryClient
from applicationinsights.exceptions import enable

from azclishell import __version__

from azure.cli.core._profile import Profile

INSTRUMENTATION_KEY = '762871d5-45a2-4d67-bf47-e396caf53d9d'


def my_context(tel_client):
    """ context for the application """
    tel_client.context.application.id = 'Azure CLI Shell'
    tel_client.context.application.ver = __version__
    tel_client.context.user.id = Profile().get_installation_id()
    tel_client.context.instrumentation_key = INSTRUMENTATION_KEY


class Telemetry(TelemetryClient):
    """ base telemetry sessions """

    start_time = None
    end_time = None

    def track_ssg(self, gesture, cmd):
        """ track shell specific gestures """
        self.track_event('Shell Specific Gesture', {gesture : cmd})

    def track_key(self, key):
        """ tracks the special key bindings """
        self.track_event('Key Press', {"key": key})

    def start(self):
        """ starts recording stuff """
        self.start_time = str(datetime.datetime.now())

    def conclude(self):
        """ concludings recording stuff """
        self.end_time = str(datetime.datetime.now())
        self.track_event('Run', {'start time' : self.start_time,
                                 'end time' : self.end_time})
        self.flush()


TC = Telemetry(INSTRUMENTATION_KEY)
enable(INSTRUMENTATION_KEY)
my_context(TC)
