"""
main.py - shifter, implements the contextual shift function
"""

import subprocess

def shift(origin, destination, filename=None):
    """
    Shifts the value of 'origin' to the specified 'destination'.

    If 'destination' is 'stdout', the 'origin' value is printed to the standard output.
    If 'destination' is 'exec', the 'origin' value is executed as a command using subprocess.
    If 'destination' is 'file', the 'origin' value is written to a file.
    If 'destination' is 'return', the 'origin' is simply returned.
    If 'destination' is any other value, the 'origin' value is assigned to a variable.

    Args:
        origin: Any value to be shifted.
        destination: The target for shifting the 'origin' value.
        filename (optional): The filename to use when 'destination' is 'file'.

    Returns:
        None, if destination is 'stdout', 'exec', or 'file'.
        The 'origin' value, if destination is any other value.
    """

    if destination == 'stdout':
        print(origin)
    elif destination == 'exec':
        subprocess.run(origin, shell=True, check=True)
    elif destination == 'file':
        if filename is None:
            raise ValueError("Missing 'file' parameter.")
        with open(filename, 'w', encoding="UTF-8") as file:
            file.write(str(origin))
    else:
        globals()[destination] = origin
