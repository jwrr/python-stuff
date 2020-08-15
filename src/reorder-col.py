#!/usr/bin/python3

example = """
Example: cat filename | reorder-col.py '2 0 1'
   a b c -> c a b
"""

import sys
if len(sys.argv) != 2:
    print(example)
    sys.exit(1)

reorder_list = [ int(s) for s in sys.argv[1].split() ]

for line in sys.stdin:
    pieces = line.split()
    pieces_reordered = []
    for i in range(len(reorder_list)):
        i_old = reorder_list[i]
        piece_old = pieces[ reorder_list[i] ]
        pieces_reordered.append(piece_old)
    line_reordered = " ".join(pieces_reordered)
    print(line_reordered)
    



