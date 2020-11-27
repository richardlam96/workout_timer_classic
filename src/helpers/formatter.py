import shutil
from art import text2art


def format_heading(text, char, **kwargs):
    terminal_width = shutil.get_terminal_size().columns
    spacer = char * terminal_width
    heading = text2art(text, "wizard", **kwargs)
    centered_heading = format_center(heading)
    return join_to_string([spacer, centered_heading, spacer])


def format_time(seconds):
    mins, secs = divmod(seconds, 60)
    timeformat = '{:02d}:{:02d}'.format(mins, secs)
    time_art = text2art(timeformat, font='block', chr_ignore=True)
    return time_art  # Block doesn't need centering.


def format_list(item_list):
    numbered_list = add_numbering(item_list)
    padded_list = format_center(numbered_list)
    return join_to_string(padded_list)


def format_center(multiline_text, pad_char=' '):
    """ Centers entire message using padding. """
    # Split text into lines if applicable.
    multiline_text.splitlines()

    # Calculate padding to apply.
    terminal_width = shutil.get_terminal_size().columns
    padding = min(terminal_width - len(str(item)) for item in multiline_text)
    left_pad = (padding // 2) * pad_char
    return list(map(lambda item: left_pad + str(item), multiline_text))


def add_numbering(list_of_string):
    return ["{}) {}".format(index + 1, item)
            for index, item in enumerate(list_of_string)]


def join_to_string(list_of_string):
    return '\n'.join(list_of_string)

