import matplotlib.pyplot as plt
import numpy as np
import math

print(math.e)
x = np.arange(-20, 20, 0.1, dtype=np.float32)
y = 1 / (1 + np.power((1 / math.e), x))

plt.figure()
plt.plot(x, y)
plt.show()
