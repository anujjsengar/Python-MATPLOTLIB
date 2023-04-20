import matplotlib.pyplot as mp
import numpy as np
#mp.plot(np.array([0,5,8,10]),np.array([20,13,20,0]),np.array([0,5,8,10]),np.array([0,13,16,20]))
mp.title("Sport Watch Data")
mp.xlabel("Average Pulse")
mp.ylabel("Calorie Burnage")
mp.grid()
mp.title("GRAPH")
mp.suptitle("DATA")
size=np.array([20,50,80])
x=np.array(['y','g','c'])
c=np.array(['y','r','c'])
mp.scatter(np.array([1,2,3]),np.array([3,2,1]),s=size,alpha=0.5,c=c)
mp.show()