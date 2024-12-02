import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt
A=[]
b=[]
with open("max") as f:
    n=f.readline()
    for i in range(0,int(n)):
        A.append(f.readline().split())
    b.append(f.readline().split())
A=np.array(A,dtype=np.float64)
b=np.array(b,dtype=np.float64)
x = linalg.solve(A, b.reshape(int(n),1))
c=[0]*int(n)
for i in range(0,int(n)):
    c[i]=x[i][0]
y=np.arange(0, int(n))
plt.bar(y,c,width=0.2)
plt.grid(True)
plt.savefig("bar")
