import shutil
from art import text2art
from termcolor import colored


def format_heading(text, **kwargs):
    heading = text2art(text, **kwargs)
    centered_heading = format_center(heading)
    return join_to_string(centered_heading)


def format_time(seconds):
    mins, secs = divmod(seconds, 60)
    timeformat = '{:02d}:{:02d}'.format(mins, secs)
    time_art = text2art(timeformat, font='block', chr_ignore=True)
    return time_art  # Block doesn't need centering.


def format_list(item_list):
    numbered_list = add_numbering(item_list)
    padded_list = format_center(join_to_string(numbered_list))
    return join_to_string(padded_list)


def format_center(multiline_text, pad_char=' '):
    """ Centers entire message using padding. """
    # Split text into lines if applicable.
    lines = multiline_text.split('\n')

    # Calculate padding to apply.
    terminal_width = shutil.get_terminal_size().columns
    padding = min([terminal_width - len(item) for item in lines])
    left_pad = (padding // 2) * pad_char
    return list(map(lambda item: left_pad + item, lines))


def add_selection_indicator(multiline_text, selection_index):
    lines = multiline_text.split('\n')
    selected_line = colored(lines[selection_index], 'red', attrs=['reverse', 'blink'])
    lines[selection_index] = selected_line
    return join_to_string(lines)


def add_numbering(list_of_string):
    return ["{}) {}".format(index + 1, item)
            for index, item in enumerate(list_of_string)]


def join_to_string(list_of_string):
    return '\n'.join(list_of_string)

