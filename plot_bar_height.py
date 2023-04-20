import matplotlib.pyplot as mp
import numpy as np
mp.barh(np.array(["A","B","C","D","E"]),np.array([50,40,39,80,100]),height=0.1)
mp.show()