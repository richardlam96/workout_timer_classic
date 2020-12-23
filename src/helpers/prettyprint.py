from .formatter import *


def pprint_heading(text, border_char="=", **kwargs):
    pprint_border(border_char)
    for line in format_heading(text, **kwargs):
        print(line)
    pprint_border(border_char)
    print()


def pprint_subheading(text, **kwargs):
    for line in format_heading(text, **kwargs):
        print(line)

def pprint_list(item_list):
    print(format_list(item_list))


def pprint_menu_list(item_list, selection=0):
    formatted_list = format_list(item_list)
    print(add_selection_indicator(formatted_list, selection))


def pprint_time(seconds):
    print(join_to_string(format_center(format_time(seconds))))


def pprint_border(border_char):
    terminal_width = shutil.get_terminal_size().columns
    border = border_char * terminal_width
    print(border)


def pprint_center(message):
    print(join_to_string(format_center(message)))

