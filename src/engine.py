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
        # Initialize Screen (template) instances to use.
        self.screen = Screen()
        self.menu_screen = MenuScreen()
        self.splash_screen = SplashScreen()
        self.timer_screen = TimerScreen()
        self.work_screen = TimerScreen(WORK_COLOR)
        self.rest_screen = TimerScreen(REST_COLOR)

    def start(self):
        try:
            workout_list = os.listdir(WORKOUT_FILES)
            self.menu_screen.draw("Interval Timer", workout_list)
            workout_filename = self.menu_screen.get_selection("Interval Timer", workout_list)

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
            self.splash_screen.draw("Round {} of {}".format(str(round_num + 1),
                                                            sequence.time_configuration.rounds))

            # Start Exercises in Round.
            for exercise in sequence.exercises:
                self.start_timer(self.timer_screen, exercise.name, "Get Ready", GET_READY_SCREEN_DURATION)
                self.start_exercise(exercise)

            # Start Round Rest.
            self.start_timer(self.timer_screen, "Round Rest", "Rest", sequence.time_configuration.round_rest)

    def start_sets(self, sequence):
        for exercise in sequence.exercises:
            # Start Exercise Sets.
            for round_num in range(sequence.time_configuration.rounds):
                self.splash_screen.draw("{}: Set {} of {}".format(exercise.name,
                                                                  str(round_num + 1),
                                                                  sequence.time_configuration.rounds))
                self.start_timer(self.timer_screen, exercise.name, "Get Ready", GET_READY_SCREEN_DURATION)
                self.start_exercise(exercise)

            # Start Set Rest.
            self.start_timer(self.timer_screen, "Set Rest", "Rest", sequence.time_configuration.round_rest)

    def start_exercise(self, exercise):
        self.start_timer(self.work_screen, exercise.name, "Work", exercise.time_configuration.work)
        self.start_timer(self.rest_screen, "Exercise Rest", "Rest", exercise.time_configuration.rest)

    def start_timer(self, screen, heading, subheading, seconds):
        for second in reversed(range(seconds + 1)):
            screen.draw(heading, subheading, second)
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
        self.screen.clear()
        self.screen.draw_heading("Workout Preview")
        self.screen.draw_subheading(workout.name)

        for sequence in workout.sequences:
            self.print_sequence_info(sequence)

        time.sleep(1)
        input("Press 'Enter' to continue...")

    def preview_sequence(self, sequence):
        # Temporary Preview.
        self.screen.clear()
        self.screen.draw_heading("Sequence Preview")
        self.screen.draw_subheading(sequence.name)
        self.print_sequence_info(sequence)

        time.sleep(1)
        input("Press 'Enter' to continue...")

    def print_sequence_info(self, sequence):
        summary_list = []
        summary_list.append("Configuration: " + sequence.name)
        summary_list.append('\tMode: ' + str(sequence.mode))
        summary_list.append('\tWork: ' + str(sequence.time_configuration.work))
        summary_list.append('\tRest: ' + str(sequence.time_configuration.rest))
        summary_list.append('\tRounds: ' + str(sequence.time_configuration.rounds))
        summary_list.append('\tRound Rest: ' + str(sequence.time_configuration.round_rest))

        # Exercise List Preview.
        summary_list.append("Exercises:")
        for exercise in sequence.exercises:
            summary_list.append('\t' + exercise.name)
        summary_list.append('\n')

        self.screen.draw_border()
        print(self.screen.formatter.format_list(summary_list).center().get_as_string())


