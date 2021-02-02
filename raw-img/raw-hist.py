#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import sys

from scipy import stats


def get_args(required_num=1):
  scriptname = sys.argv[0]
  num_args    = len(sys.argv) - 1
  if num_args < required_num:
    print("Example: {} width height bitwidth img.raw".format(scriptname))
    sys.exit(1)
  return sys.argv[1:]

  
# =================================================================
# =================================================================

args = get_args(4)
w = int(args[0])
h = int(args[1])
bw = int(args[2])
filename1    = args[3]
filelist     = args[4:]

print("width={}, height={}, bw={}, file1={}".format(w,h,bw, filename1))

if bw==16:
  dtype = np.uint16
else:
  print("Unsupported bitwidth. Only 16 bit is currently supported")
  sys.exit(1)

img1 = np.fromfile(filename1, dtype=dtype).reshape((h,w))
img1_32 = img1.astype(np.int32) # has range 0 to 64K-1

minval    = np.min(img1)
maxval    = np.max(img1) 
meanval   = np.mean(img1)
medianval = np.median(img1)
modearray   = stats.mode(img1, axis=None)
mode_val    = modearray[0][0]
mode_cnt    = np.count_nonzero(img1 == mode_val)
print("min={} max={} mean={:.2f} median={:0.0f} mode={} mode_cnt={}".
  format(minval, maxval, meanval, medianval, mode_val, mode_cnt))

plt.hist(img1.flatten())
plt.title("Histogram")
plt.show()
#

