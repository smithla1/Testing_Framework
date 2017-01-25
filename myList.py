#!/usr/bin/env python

"""
    This python script will recursively walk the files in it's
    containing directory, creating a list of those files,
    which will then be placed in an html file and subsequently
    be displayed in a browser window.
"""

import subprocess

# Collect the results of the ls shell command
output = subprocess.check_output(['ls', '-R'])

# Replace LR EOL character with html line break tag
output = output.replace('\n', '<br />')

# Write the modified output to a text file
output_file = open("contents.html", "w")
output_file.write(output)
output_file.close()

# Open the newly created file
subprocess.check_output(['xdg-open', 'contents.html'])

