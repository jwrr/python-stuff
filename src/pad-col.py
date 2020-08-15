#!/usr/bin/python3

example = """
Example: pad-col.py filename.txt
   a b c
   12 34 56
   aaa bbb ccc
   ----
   a   b   c
   12  34  56
   aaa bbb ccc
"""

import sys
if len(sys.argv) != 2:
    print(example)
    sys.exit(1)

# slurp file
with open( sys.argv[1]  ) as f: lines = f.readlines()

# find max length of each column
col_maxs = []
for line in lines:
    for i, col in enumerate( line.split() ):
        if i >= len(col_maxs):
            col_maxs.append(0)
        col_maxs[i] = max( len(col), col_maxs[i]  )

# pad each column and print resulting line
for line in lines:
    newline = ""
    for i, col in enumerate( line.split() ):
        newline += col.ljust( col_maxs[i]+1, ' ')
    print(newline)



