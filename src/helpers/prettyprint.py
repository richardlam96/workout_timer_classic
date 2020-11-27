from .formatter import *


def pprint_heading(text, border_char="*", **kwargs):
    pprint_border(border_char)
    for line in format_heading(text, **kwargs):
        print(line)
    pprint_border(border_char)


def pprint_list(item_list):
    print(format_list(item_list))


def pprint_menu_list(item_list, selection=0):
    formatted_list = format_list(item_list)
    print(add_selection_indicator(formatted_list, selection))


def pprint_time(seconds):
    print(format_time(seconds))


def pprint_border(border_char):
    terminal_width = shutil.get_terminal_size().columns
    border = border_char * terminal_width
    print(border)
