import matplotlib.pyplot as mp
import numpy as np
y=np.array([50,40,39,80,100])
l=["Apple","Banana","Mango","Grapes","Dates"]
mp.pie(y,labels=l)
mp.legend(title="FIVE FRUITS")
mp.show()