import os
import time
import simpleaudio as sa
from config import WORKOUT_FILES, ROUNDS_MODE, SETS_MODE
from src.screens.menu_screen import MenuScreen
from src.screens.timer_screen import TimerScreen
from src.entities.workout import Workout


class Engine(object):

    def __init__(self):
        pass

    def start(self):
        try:
            workout_list = os.listdir(WORKOUT_FILES)
            intro_menu = MenuScreen("Interval Timer!", "Workout App", "Choose a workout:", workout_list)
            workout_filename = intro_menu.get_selection()

            selected_workout = Workout(workout_filename)
            self.start_workout(selected_workout)
        except KeyboardInterrupt:
            print("Forced exit. Bye!")
        finally:
            print("Workout Completed. Nice!")

    def start_workout(self, workout):

        # Show Workout Preview.
        self.preview_workout(workout)
        input()

        for sequence in workout.sequences:
            # Show Sequence Preview (?).
            self.preview_sequence(sequence)
            input()

            if sequence.mode == ROUNDS_MODE:
                self.start_rounds(sequence)
            elif sequence.mode == SETS_MODE:
                self.start_sets(sequence)
            else:
                # TODO: Better error handling here and elsewhere.
                print("Error! Mode not declared! Exiting...")
                exit()

    def start_rounds(self, sequence):
        for round_num in range(sequence.time_configuration.rounds):
            # Show timed Round Preview.
            self.start_timer("Round", str(round_num + 1), 3)

            # Start Exercises in Round.
            for exercise in sequence.exercises:
                self.start_timer(exercise.name, "Get Ready", 5)
                self.start_exercise(exercise)

            # Start Round Rest.
            self.start_timer("Round Rest", "Rest", sequence.time_configuration.round_rest)

    def start_sets(self, sequence):
        for exercise in sequence.exercises:
            # Show timed Exercise Preview.

            # Start Exercise Sets.
            for _ in range(sequence.time_configuration.rounds):
                self.start_exercise(exercise)

            # Start Set Rest.
            self.start_timer("Set Rest", "Rest", sequence.time_configuration.round_rest)

    def start_exercise(self, exercise):
        self.start_timer(exercise.name, "Work", exercise.time_configuration.work, "red")
        self.start_timer("Exercise Rest", "Rest", exercise.time_configuration.rest, "yellow")
        pass

    def start_timer(self, heading, subheading, seconds, color="white"):
        timer_screen = TimerScreen(heading, subheading)
        for second in reversed(range(seconds + 1)):
            timer_screen.draw(second, color)
            time.sleep(1)
            if second == 0:
                self.play_beep()

    def play_beep(self):
        sound = sa.WaveObject.from_wave_file('./audio/beep-1.wav')
        sound.play()
        sa.stop_all()

    def preview_workout(self, workout):
        # Temporary Preview.
        print("Selected: "+ workout.name.replace('_', ' ').upper())
        print()

        for sequence in workout.sequences:
            self.preview_sequence(sequence)

    def preview_sequence(self, sequence):
        # Temporary Preview.
        print("[[ " + sequence.name.replace('_', ' ').upper() + " ]]")
        print("Configuration:")
        print('\tMode: ' + str(sequence.mode))
        print('\tWork: ' + str(sequence.time_configuration.work))
        print('\tRest: ' + str(sequence.time_configuration.rest))
        print('\tRounds: ' + str(sequence.time_configuration.rounds))
        print('\tRound Rest: ' + str(sequence.time_configuration.round_rest))

        # Exercise List Preview.
        print("Exercises:")
        for exercise in sequence.exercises:
            print('\t' + exercise.name)
        print()

