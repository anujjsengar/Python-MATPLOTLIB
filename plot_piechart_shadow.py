import matplotlib.pyplot as mp
import numpy as np
m=[0.2,0,0.3,0,0]
mp.pie(np.array([50,40,39,80,100]),explode=m,label=["MADHU","DIBYA","HARSH","PRINCE","ANUJ"],shadow=True)
mp.show()