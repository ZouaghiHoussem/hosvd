import numpy as np
import numpy.linalg as la
from numpy.linalg import matrix_rank as mrank

a = np.zeros((2,2,2))
a[0,0,0] = a[0,1,1] = a[1,0,0] = 1
#a[0,0,0] = a[1,1,0] = a[0,0,1] = 1

print "a"
print a

print

print "orders CFKA"
print a.ravel(order='C').reshape(2,4),"\n"
print a.ravel(order='F').reshape(2,4),"\n"
print a.ravel(order='K').reshape(2,4),"\n"
print a.ravel(order='A').reshape(2,4),"\n"

print

print mrank(a.ravel(order='C').reshape(2,4))
print mrank(a.ravel(order='F').reshape(2,4))
print mrank(a.ravel(order='K').reshape(2,4))
print mrank(a.ravel(order='A').reshape(2,4))
