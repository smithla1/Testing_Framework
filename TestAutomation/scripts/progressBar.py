#!/usr/bin/env python

import sys
import os

"""
    This program will create a progress bar to give a visual representation of
    the calling program's progress.

    update_progress(progress): Displays or updates a console progress bar
        Accepts a float or int greater than or equal to 0.
        An int will be converted to a float.
        Values between 0 and 1 (inclusive) are understood to represent the
            proportion of progress currently completed.
        A value greater than or equal to 1 represents 100%.
"""
def update_progress(progress):
    # This will make the progress bar's length dependent on the width of the
    # console. The 28 that is subtracted from the length accounts for the
    # length of 'Progress: ', status, and the percentage of task completed.
    barLength = eval(os.popen("stty size", "r").read().split()[1])-28
    status = ""
    if isinstance(progress, int):
        progress = float(progress)
    if progress >= 1:
        progress = 1.0
        status = "Complete\r\n"
    block = int(round(barLength*progress))
    text = ("\rProgress: [{0}] {1}% {2}".format("#"*block + "-"*(barLength-block),
            round(progress*100.0, 1), status))
    sys.stdout.write(text)
    sys.stdout.flush()


if __name__ == "__main__":
    import time
    for i in range(101):
        time.sleep(0.1)
        update_progress(i/100.0)
