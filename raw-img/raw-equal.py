#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import sys


def get_args(required_num=1):
  scriptname = sys.argv[0]
  num_args    = len(sys.argv) - 1
  if num_args < required_num:
    print("Example: {} width height bitwidth img1.raw img2.raw [diff.raw]".format(scriptname))
    sys.exit(1)
  return sys.argv[1:]

  
# =================================================================
# =================================================================

args = get_args(5)
w = int(args[0])
h = int(args[1])
bw = int(args[2])
filename1    = args[3]
filename2    = args[4]
outfilename  = args[5] if len(args)>5 else None
filelist     = args[6:]

print("width={}, height={}, bw={}, file1={}, file2={}".format(w,h,bw, filename1, filename2))

if bw==16:
  dtype = np.uint16
else:
  print("Unsupported bitwidth. Only 16 bit is currently supported")
  sys.exit(1)

img1 = np.fromfile(filename1, dtype=dtype).reshape((h,w))
img2 = np.fromfile(filename2, dtype=dtype).reshape((h,w))

img1_32 = img1.astype(np.int32)
img2_32 = img2.astype(np.int32)

diff_32 = img2_32 - img1_32
abs_32  = np.abs(diff_32)
abs_clipped = np.clip(diff_32, 0, 1)
abs_offset = abs_clipped * 2**15


if outfilename != None:
  print(f"Creating: {outfilename}")
  abs_offset.astype(np.uint16).tofile(outfilename)
  print(f"./raw-view.py {w} {h} {bw} {outfilename}")
  sys.exit(0)

# ======================================================
# Show difference if outfile isn't defined
# ======================================================

img = abs_offset.astype(int)
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








