#!/usr/bin/python

"""
Rename files starting with digit to files starting with alpha
The output is a script that does the rename.
format:
    $ ls | rename-files.py > rename.bash
    $ cat rename.bash # make sure it's right'
    $ source rename.bash 
"""

import sys
offset = 1 # change to 0 if first file is 0.xxx
cmd = "git mv"
for line in sys.stdin:
    line = line.rstrip()
    pieces = line.split('-')
    if len(pieces) == 2 and pieces[0].isdigit():
        i = int(pieces[0])
        pieces[0] = chr(ord('a') + (i-offset) )
        filename = "-".join(pieces)
        print("{} {} {}".format(cmd, line, filename))

