import numpy as np
from math import sqrt

A=np.array(
[
[5,3,5],
[4,2,1],
[0,3,3],
]
,dtype = 'float64')

print "input:\n",A,"\n\n"

l = np.matmul(A, A.T)
r = np.matmul(A.T, A)

print l
print "\n"
print r

sU, U = np.linalg.eigh(l)
sV, V = np.linalg.eigh(r)

print "\n"

for i in sU:
	print sqrt(i),

#print sU
#print sV

print "\n"
print U
print V
