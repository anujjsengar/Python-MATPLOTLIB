import matplotlib.pyplot as mp
import numpy as np
m=[0.2,0,0.3,0,0]
x=["black","hotpink","b"]
mp.pie(np.array([50,40,39,80,100]),explode=m,color=x)
mp.show()