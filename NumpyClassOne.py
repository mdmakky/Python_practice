import numpy as np
# Creation of numpy array
a = np.array([1, 2, 3, 4])
b = np.arange(12)
c = np.arange(12).reshape(4, 3)
d = np.zeros((3, 4))
e = np.ones((5, 5))
f = np.identity(5)
g = np.linspace(0, 10, 6).reshape(3, 2)
g1=np.random.random((3,4))*100
###################################################

# Attribute of numpy array

'''print(e.ndim)
print(e.shape)
print(b.size)
print(b.itemsize)
print(g.dtype)'''

####################################################

# Changing data type
h = np.arange(12).reshape(4, 3).astype(np.int32)

# print(h,h.dtype)

####################################################
# Array operation
# ==>Scalara operation
i = np.arange(24, 36).reshape(3, 4)
# print(a+i)
# print(a-i)
# print(a*i)
# print(a/i)
# print(a**i)

# ==>Lelational operation
# print(i>15)


# ==> Vector operation

# print(np.dot(c,i))

###################################################

# Array function

# ===>max,min,sum,prod function
# print(i)
''''print(np.max(i,axis=0))
print(np.min(i,axis=0))
print(np.sum(i,axis=0))
print(np.prod(i,axis=0))'''

# ===>mean,median,std,var function
'''print(np.mean(i,axis=1))
print(np.median(i,axis=1))
print(np.std(i,axis=1))
print(np.var(i,axis=1))'''


# ===>Trigonmetric function

# print(np.tan(i))

# ===>log,exponential function

'''print(np.log(i))
print(np.exp(i))'''

# ===>ceil,flore,round function
# print(np.round(np.random.random((3,4))*100))
# .......



