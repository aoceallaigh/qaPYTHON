#! usr/bin/env
import matplotlib.pyplot as plt
import numpy as np

x = np.zeros(9)

for i in range(0,9):
    x[i] = i

plt.plot(x,'o')
plt.show()


