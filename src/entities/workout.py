from ..helpers.filehelper import read_list


class Workout(object):

    def __init__(self, workout_filepath):
        # Read each filepath and convert to Sequence object.
        workout_data = read_list(workout_filepath)

        # Read first line for Name, Work, Rest, and Sets
        workout_config = workout_data[0].split()
        self.name = " ".join(workout_config[:-4])
        self.work = int(workout_config[-4])
        self.rest = int(workout_config[-3])
        self.sets = int(workout_config[-2])
        self.rounds = int(workout_config[-1])

        # Read the rest of the lines as the Exercise list.
        self.exercises = workout_data[1:]

