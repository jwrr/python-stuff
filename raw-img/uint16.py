#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt


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


