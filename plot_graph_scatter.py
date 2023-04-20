import matplotlib.pyplot as mp
import numpy as np
#mp.plot(np.array([0,5,8,10]),np.array([20,13,20,0]),np.array([0,5,8,10]),np.array([0,13,16,20]))
mp.title("Sport Watch Data")
mp.xlabel("Average Pulse")
mp.ylabel("Calorie Burnage")
mp.grid()
mp.title("GRAPH")
mp.suptitle("DATA")
x=np.array(['y','g','c'])
mp.scatter(np.array([1,2,3,4,6,7,4,8,6]),np.array([3,6,8,5,2,5,6,8,1]),c=x,s=np.array([20,100,150,60,90,80,48,52,35]))
mp.show()