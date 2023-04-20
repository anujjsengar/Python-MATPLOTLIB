import matplotlib.pyplot as mp
import numpy as np
mp.title("Sport Watch Data")
mp.xlabel("Average Pulse")
mp.ylabel("Calorie Burnage")
mp.grid()
mp.title("GRAPH")
mp.suptitle("DATA")
mp.scatter(np.array([1,6,2,3]),np.array([3,2,4,1]),color='c')
mp.scatter(np.array([1,5,6,2,3]),np.array([6,7,8,2,1]),color='g')
mp.show()