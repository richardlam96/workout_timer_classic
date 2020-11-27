from src.screens.menu_screen import MenuScreen


def main():
    workout_list = ["monday", "tuesday", "wednesday"]
    intro_menu = MenuScreen("Interval Timer!", "My App", workout_list)


if __name__ == '__main__':
    main()

