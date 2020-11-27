from .formatter import format_heading, format_list, format_time


def pprint_heading(text, border_char, **kwargs):
    print(format_heading(text, border_char))


def pprint_list(list):
    print(format_list(list))


def pprint_time(seconds):
    print(format_time(seconds))

