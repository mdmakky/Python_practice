import time
a = range(100000000)
b = range(100000000,200000000)
start_time= time.time()
c=[(a+b) for a,b in zip(a,b)]
time1=(time.time()-start_time)

import numpy as np
d= np.arange(100000000)
e = np.arange(100000000,200000000)
start_time2=time.time()
f=d+e
time2=(time.time()-start_time2)
print(time1/time2)

