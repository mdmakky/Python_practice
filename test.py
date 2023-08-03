import numpy as mak
array = mak.arange(12).reshape(3,4)
# print(array[:,1:3])
for i in mak.nditer(array):
    print(i)