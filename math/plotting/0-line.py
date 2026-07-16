#!/usr/bin/env python3
"""Line graph of y = x^3 as a solid red line."""
import numpy as np
import matplotlib.pyplot as plt

y = np.arange(0, 11) ** 3

plt.plot(y, 'r-')
plt.xlim(0, 10)
plt.show()