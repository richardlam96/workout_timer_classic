from .time_configuration import TimeConfiguration
from .exercise import Exercise
from ..helpers.filehelper import read_list


class Sequence(object):

    def __init__(self, filepath):

        # Read file data and add as private members for later processing.
        self._sequence_data = read_list(filepath)
        self._config_line = self._sequence_data[0].split()

        # Read filepath as name (better way later).
        self.name = filepath.split('.')[0]

        # Read first line as the Time Configuration.
        self.mode = self._config_line[0]
        self.time_configuration = TimeConfiguration(work=self._config_line[1],
                                                    rest=self._config_line[2],
                                                    rounds=self._config_line[3])

        # Read the rest of the file as a list of Exercises.
        self.exercises = [Exercise(exercise, self.time_configuration)
                          for exercise in self._sequence_data[1:]]

        # TODO: Implement an override in the case that
        # self.exercises = [Exercise(data.split()) for data in self._sequence_data[1:]]

