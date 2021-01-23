#!/usr/bin/env python3

# catfilename [list of files]
# Print filename followed by file contents

import sys

# for arg in sys.argv[1:]:
#     fh = open(arg)
#     text = fh.read()
#     fh.close()
#     print(f"# ===== {arg} =====")
#     print(text)


for arg in sys.argv[1:]:
    with open(arg) as fh:
        text = fh.read() # slurp entire file into string
    print(f"# ===== {arg} =====")
    print(text)

  
  

  
  



