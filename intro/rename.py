#!/usr/bin/env python3

"""
rename.pl from to [filelist]
    Change part of filename
example:
    rename.pl template prjname *
"""


import sys
import os

num_argv = len(sys.argv)
if num_argv < 4:
    sys.exit("Example: rename.pl 'from_str' 'to_str' file1 file2 file3 ")

from_str = sys.argv[1]
to_str   = sys.argv[2]

rename_all = False
quit = False
for filename in sys.argv[3:]:
    newname = filename.replace(from_str, to_str)
    change = newname != filename
    if change:

        ans = 'n'
        if quit:
            print(f"skipping {filename} {newname}")
        elif rename_all:
            print(f"renaming {filename} {newname}")
        else:
            ans = input(f"rename {filename} {newname} <y/n/a/q>? ")

        if ans == 'q':
            quit = True

        if ans == 'a':
            rename_all = True

        if ans == "y" or rename_all:
            os.rename(filename, newname)


