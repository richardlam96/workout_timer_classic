from config import WORKOUT_FILES
from src.entities.sequence import Sequence
from src.helpers.filehelper import read_list


class Workout(object):

    def __init__(self, filename):

        # Read filepath as name.
        self._filepath = WORKOUT_FILES + filename
        self.name = filename.split('.')[0].replace('_', ' ').upper()

        # Read file data as list of Sequence files.
        self.sequences = [Sequence(sequence_file) for sequence_file in read_list(self._filepath)]

        # TODO: Implement calculated Time Configuration based on nested items.

