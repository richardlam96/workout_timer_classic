import os
import time
import simpleaudio as sa
from config import *
from src.entities.workout import Workout
from src.screens.screen import Screen
from src.screens.menu_screen import MenuScreen
from src.screens.timer_screen import TimerScreen
from src.screens.splash_screen import SplashScreen


class Engine(object):

    def __init__(self):
        pass

    def start(self):
        try:
            workout_list = os.listdir(WORKOUT_FILES)
            intro_menu = MenuScreen("Interval Timer!", "Ready?", "Choose a workout:", workout_list)
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
        for round_num in range(sequence.time_configuration.rounds):
            # Show timed Round Preview.
            self.start_splash_screen("Round {} of {}".format(str(round_num + 1),
                                                             sequence.time_configuration.rounds))

            # Start Exercises in Round.
            for exercise in sequence.exercises:
                self.start_timer(exercise.name, "Get Ready", GET_READY_SCREEN_DURATION)
                self.start_exercise(exercise)

            # Start Round Rest.
            self.start_timer("Round Rest", "Rest", sequence.time_configuration.round_rest)

    def start_sets(self, sequence):
        for exercise in sequence.exercises:
            # Start Exercise Sets.
            for round_num in range(sequence.time_configuration.rounds):
                self.start_splash_screen("{}: Set {} of {}".format(exercise.name,
                                                                  str(round_num + 1),
                                                                  sequence.time_configuration.rounds))
                self.start_timer(exercise.name, "Get Ready", GET_READY_SCREEN_DURATION)
                self.start_exercise(exercise)

            # Start Set Rest.
            self.start_timer("Set Rest", "Rest", sequence.time_configuration.round_rest)

    def start_exercise(self, exercise):
        self.start_timer(exercise.name, "Work", exercise.time_configuration.work, "red")
        self.start_timer("Exercise Rest", "Rest", exercise.time_configuration.rest, "yellow")
        pass

    def start_timer(self, heading, subheading, seconds, border_color="white"):
        timer_screen = TimerScreen(heading, subheading)
        for second in reversed(range(seconds + 1)):
            timer_screen.draw(second, border_color)
            time.sleep(1)
            if second == 0:
                self.play_beep()

    def start_splash_screen(self, text):
        splash_screen = SplashScreen(text)
        splash_screen.draw()
        time.sleep(SPLASH_SCREEN_DURATION)

    def play_beep(self):
        sound = sa.WaveObject.from_wave_file('./audio/beep-1.wav')
        sound.play()
        sa.stop_all()

    def preview_workout(self, workout):
        # Temporary Preview.
        workout_name = workout.name.replace('_', ' ').upper()
        workout_preview = Screen(heading="Workout Preview", subheading=workout_name)
        workout_preview.draw()

        print("Selected: " + workout.name.replace('_', ' ').upper())

        for sequence in workout.sequences:
            self.show_sequence_info(sequence)

        time.sleep(1)
        input("Press 'Enter' to continue...")

    def preview_sequence(self, sequence):
        # Temporary Preview.
        sequence_name = sequence.name.replace('_', ' ').upper()
        sequence_preview = Screen(heading="Sequence Preview", subheading=sequence_name)
        sequence_preview.draw()
        self.show_sequence_info(sequence)

        time.sleep(1)
        input("Press 'Enter' to continue...")

    def show_sequence_info(self, sequence):
        sequence_name = sequence.name.replace('_', ' ').upper()
        print("Configuration: " + sequence_name)
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


