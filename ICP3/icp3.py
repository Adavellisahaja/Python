import numpy as np
s = np.random.randint(0, 20, 15)
print(s)
a= s.reshape((3,5))
x = a[0]
x[np.where(x==np.max(x))] = 0
print(x)
y = a[1]
y[np.where(y==np.max(y))] = 0
print(y)
z = a[2]
z[np.where(z==np.max(z))] = 0
print(z)
b = np.vstack([x,y,z])
print(b)



