from .time_configuration import TimeConfiguration


class Exercise(object):

    def __init__(self, name, time_configuration):
        self.name = name
        self.time_configuration = time_configuration
