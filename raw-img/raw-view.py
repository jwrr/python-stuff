#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import sys


def get_args(required_num=1):
  scriptname = sys.argv[0]
  num_args    = len(sys.argv) - 1
  if num_args < required_num:
    print("Example: {} width height bitwidth".format(scriptname))
    sys.exit(1)
  return sys.argv[1:]

  
# =================================================================
# =================================================================

args = get_args(4)
w = int(args[0])
h = int(args[1])
bw = int(args[2])
filelist = args[3:]

print("width={}, height={}, bw={}".format(w,h,bw))

dtype = np.uint16

for filename in filelist:
  img = np.fromfile(filename, dtype=dtype).reshape((h,w))
  
  fig, ax = plt.subplots()
  ax.imshow(img, interpolation="none")
  
  ## Change default mouse-over value from float to int
  def format_coord(x,y):
    val = img[int(y), int(x)]
    return "x = {}, y = {} [{}]".format(int(x), int(y), val)
  ax.format_coord = format_coord
  
  plt.show()


