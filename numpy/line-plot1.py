#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(100)
y = np.arange(100)
plt.plot(2*x)
# plt.plot(x, y)
plt.title("x vs y")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

