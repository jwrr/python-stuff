#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import sys


def get_args(required_num):
  scriptname = sys.argv[0]
  num_args    = len(sys.argv) - 1
  if num_args < required_num:
    print("Example: {} width height bitwidth".format(scriptname))
    sys.exit(1)
  return sys.argv[1:]


def gradient_h(shape, dtype, filename):
  img = np.empty(shape, dtype=dtype)
  (h,w) = shape
  row = np.linspace(0, 2**16-1, w)
  for r in range(h):
    img[r] = row
  img.tofile(filename)
  print(filename)
  return img
  
  
def gradient_v(shape, dtype, filename):
  img = np.empty(shape, dtype=dtype)
  (h,w) = shape
  vec = np.linspace(0, 2**16-1, h)
  for c in range(w):
    img[:, c] = vec
  img.tofile(filename)
  print(filename)
  return img

  
def bars_h(shape, dtype, filename):
  img = np.zeros(shape, dtype=dtype)
  (h,w) = shape
  vec1 = np.empty(w)
  vec1.fill(2**15-1) # half-scale
  for r in range(h):
    if (r // 40) % 2:
      img[r,:] = vec1
  if filename != "":
    img.tofile(filename)
    print(filename)
  return img

  
def bars_v(shape, dtype, filename=""):
  img = np.zeros(shape, dtype=dtype)
  (h,w) = shape
  vec1 = np.empty(h)
  vec1.fill(2**16-1)
  for c in range(w):
    if (c // 40) % 2:
      img[:, c] = vec1
  if filename != "":
    img.tofile(filename)
    print(filename)
  return img

def bars_vh(shape, dtype, filename=""):
  img = bars_h(shape, dtype, "")
  (h,w) = shape
  vec1 = np.empty(h)
  vec1.fill(2**16-1)
  for c in range(w):
    if (c // 40) % 2:
      img[:, c] = vec1
  if filename != "":
    img.tofile(filename)
    print(filename)
  return img


def x(shape, dtype, filename=""):
  img = np.zeros(shape, dtype=dtype)
  (h,w) = shape
  val = 2**15-1
  for r in range(h):
    img[r,r] = val
    img[r,h-r] = val
  if filename != "":
    img.tofile(filename)
    print(filename)
  return img




# =================================================================
# =================================================================

w,h,bw = get_args(3)
print("width={}, height={}, bw={}".format(w,h,bw))

shape = (int(h), int(w))
dtype = np.uint16

suffix = "_w{}xh{}x{}bit.raw".format(w, h, bw)

gradient_h(shape, dtype, "gradient_h" + suffix)
gradient_v(shape, dtype, "gradient_v" + suffix)
bars_h(shape, dtype, "bars_h" + suffix)
bars_v(shape, dtype, "bars_v" + suffix)
bars_vh(shape, dtype, "bars_vh" + suffix)
x(shape, dtype, "x" + suffix)

print("done")
sys.exit(0)


# =================================================================
# Write and read a 2d array of uint16  
w=10
h=8

# raw = np.zeros((h,w), dtype=np.uint16)
row_1d = np.arange(w, dtype=np.uint16)
imga_2d = np.empty((0,w), dtype=np.uint16)

for i in range(h):
  imga_2d = np.vstack([imga_2d, row_1d])

print(imga_2d)

imga_2d.tofile("img.raw")

# View binary files with hexdump or xxd from linux command line

imgb_2d = np.fromfile("img.raw", dtype=np.uint16).reshape((-1,w))
print(imgb_2d)

# =================================================================
# Create and display VGA grayscale gradient image of uint16

w=640
h=480
vga_row   = np.arange(0, w*100, 100, dtype=np.uint16)
vga_frame = np.empty((0,w), dtype=np.uint16)
for i in range(h):
  vga_frame = np.vstack([vga_frame, vga_row])

print(vga_frame.shape)

fig, ax = plt.subplots()
ax.imshow(vga_frame, cmap="gray", interpolation="none")

## Change default mouse-over value from float to int
def format_coord(x,y):
  val = vga_frame[int(y), int(x)]
  return "x = {}, y = {} [{}]".format(int(x), int(y), val)
ax.format_coord = format_coord

plt.show()


