import os
from config import WORKOUT_FILES, ROUNDS_MODE, SETS_MODE
from src.screens.menu_screen import MenuScreen
from src.entities.workout import Workout


class Engine(object):

    def __init__(self):
        pass

    def start(self):
        workout_list = os.listdir(WORKOUT_FILES)
        intro_menu = MenuScreen("Interval Timer!", "My App", workout_list)
        workout_filename = intro_menu.get_selection()

        selected_workout = Workout(workout_filename)
        self.start_workout(selected_workout)

    def start_workout(self, workout):

        # Show Workout Preview.
        self.preview_workout(workout)

        for sequence in workout.sequences:
            # Show Sequence Preview (?).
            self.preview_sequence(sequence)

            if sequence.mode == ROUNDS_MODE:
                self.start_rounds(sequence)
            elif sequence.mode == SETS_MODE:
                self.start_sets(sequence)
            else:
                # TODO: Better error handling here and elsewhere.
                print("Error! Mode not declared! Exiting...")
                exit()

    def start_rounds(self, sequence):
        for _ in range(sequence.time_configuration.rounds):
            # Show timed Round Preview.

            # Start Exercises in Round.
            for exercise in sequence.exercises:
                self.start_exercise(exercise)

            # Start Round Rest.
            self.start_timer("Round", "Rest", sequence.time_configuration.round_rest)

    def start_sets(self, sequence):
        for exercise in sequence.exercises:
            # Show timed Exercise Preview.

            # Start Exercise Sets.
            for _ in range(sequence.time_configuration.rounds):
                self.start_exercise(exercise)

            # Start Set Rest.
            self.start_timer("Set", "Rest", sequence.time_configuration.round_rest)

    def start_exercise(self, exercise):
        self.start_timer(exercise.name, "Work", exercise.time_configuration.work)
        self.start_timer(exercise.name, "Rest", exercise.time_configuration.rest)
        pass

    def start_timer(self, heading, subheading, seconds):
        # Temporary "screen"
        print("{} - {} - {}".format(heading, subheading, seconds))
        # for _ in seconds:
        #     print(seconds)

    def preview_workout(self, workout):
        print(workout.name)
        input()

    def preview_sequence(self, sequence):
        print(sequence.name)
        print('\tMode' + str(sequence.mode))
        print('\tWork' + str(sequence.time_configuration.work))
        print('\tRest' + str(sequence.time_configuration.rest))
        print('\tRounds' + str(sequence.time_configuration.rounds))
        print('\tRound Rest' + str(sequence.time_configuration.round_rest))
        input()

