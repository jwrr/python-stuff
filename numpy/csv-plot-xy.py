#!/usr/bin/env python3
# 
# First column is X, second column is Y.

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
x = data[0]
y = data[1]

num_rows, num_cols = data.shape
print("num items={}".format(num_cols))

plt.title("x vs y")
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x, y)
plt.show()

