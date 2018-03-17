import numpy as np
import scipy.linalg as lng
import time

N=500
A = np.random.random((N,N))
k =np.arange(N)


start_time = time.time()
for t in  np.linspace(0.,10.,100):
    b = k/(1.+k*t)
    r1 = lng.solve(A,b)
#    print(r1)
print(time.time()-start_time)

start_time = time.time()
lu,piv = lng.lu_factor(A)
for t in  np.linspace(0.,10.,100):
    b = k/(1.+k*t)
    r2 = lng.lu_solve((lu,piv), b)
#    print(r2)
print(time.time()-start_time)

start_time = time.time()
Ainv = lng.inv(A)
for t in  np.linspace(0.,10.,100):
    b = k/(1.+k*t)
    r3 = np.dot(Ainv, b)
#    print(r3)
print(time.time()-start_time)
