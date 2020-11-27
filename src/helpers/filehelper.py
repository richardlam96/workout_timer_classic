

def read_list(file_path):
    """
    Read each line in the file and return them as a list.
    """
    with open(file_path) as f:
        file_lines = f.read().splitlines()
    return file_lines


def read_table(file_path):
    """
    Read values in each line in the file and return as a 2D list.
    """
    with open(file_path) as f:
        file_lines = f.read().splitlines()
    return [read_line_values(line) for line in file_lines]


def read_line_values(file_line):
    """
    Read a string of values where the last three are individual elements.
    This requires the lines to end with three numbers.
    """
    file_line = file_line.strip().split()
    name = ' '.join(file_line[:-3])
    numbers = file_line[-3:]
    return [name, *numbers]