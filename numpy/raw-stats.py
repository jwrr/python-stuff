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
# modeval   = stats.mode(img1)
# modelen   = len(modeval)
print("min={} max={} mean={} median={}".
  format(minval, maxval, meanval, medianval))



sys.exit(0)

combined_32 = img2_32 + img1_32  # has range 0 to 128K-2
combined_clipped = np.clip(combined_32, 0, 2**16-1) ## clip to range 0 to 64K-1


if outfilename != None:
  print(f"Creating: {outfilename}")
  combined_clipped.astype(np.uint16).tofile(outfilename)
  print(f"./raw-view.py {w} {h} {bw} {outfilename}")
  sys.exit(0)

# ======================================================
# Display combined image if outfile isn't defined
# ======================================================

img = combined_clipped.astype(int)
#img = img_32.astype(int)

fig, ax = plt.subplots()
# ax.imshow(img, cmap="gray", interpolation="none")
ax.imshow(img, interpolation="none")

## Change default mouse-over value from float to int
def format_coord(x,y):
  val = img[int(y), int(x)]
  return "x = {}, y = {} [{}]".format(int(x), int(y), val)
ax.format_coord = format_coord

plt.show()








