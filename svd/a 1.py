import numpy as np
from numpy.linalg import norm

from random import normalvariate
from math import sqrt

A=np.array(
[
[9,1,5,9,7,3],
[10,3,6,9,8,2],
[8,2,5,9,6,2],
[7,6,6,9,7,2],
[8,1,5,9,6,3],
[9,5,6,10,8,4],
[10,4,5,2,8,1],
]
,dtype = 'float64')

print "input:\n",A,"\n\n"

#print "transpose:\n", np.matrix.transpose(A) #works fine

l = np.dot(A, np.matrix.transpose(A))
r = np.dot(np.matrix.transpose(A), A)

print "A AT"
print l

print "\n"
print "AT A"
print r

print "\n"
print "\n"
print np.linalg.eigvals(l)
print np.linalg.eigvals(r)
