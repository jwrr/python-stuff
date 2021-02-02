#!/usr/bin/env python3
# 
# Each column of csv is a Y sequence. All Y sequences are plotted on the same
# chart.

import numpy as np
import matplotlib.pyplot as plt
import sys

if len(sys.argv) < 2:  # requires 1 arg
  scriptname = sys.argv[0]
  print("Example: {} filename.csv".format(scriptname))
  sys.exit(1)

# ====================================================

filename = sys.argv[1]
data1 = np.genfromtxt(filename,delimiter=",")
data = np.transpose(data1)

num_rows, num_cols = data.shape
print("num sequences={}, num items per sequence={}".format(num_rows, num_cols))

plt.title("y vs i")
plt.xlabel("i")
plt.ylabel("y")
for y in data:
  plt.plot(y)
plt.show()

