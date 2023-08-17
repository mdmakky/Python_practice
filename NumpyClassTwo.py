# Time difference between Numpy and list in python


# a=[i for i in range(100000000)]
# b=[i for i in range(100000000,200000000)]
c=[]
import time
# start=time.time()
# for i in range(len(a)):
#     c.append(a[i]+b[i])
    
# print(time.time()-start)

import numpy as np
d=np.arange(100000000)
e=np.arange(100000000,200000000)
startAgain=time.time()
f=d+e
print(time.time()-startAgain)