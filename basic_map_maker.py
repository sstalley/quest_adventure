import numpy as np


lmap = np.array([[0, 1, 2, 3], [0, 2, 2, 3]])
np.save("world.npy", lmap)

temps = np.array([[90, 81, 72, 68], [70, 82, 32, 42]])
np.save("temps.npy", temps)

assert lmap.shape == temps.shape
