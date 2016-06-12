# Matrix Algebra

import numpy as np
import math
# 2. Vector Operations


u = np.array([6, 2, -3, 5])
v = np.array([3, 5, -1, 4])

# 2.1
print(u + v)

# 2.2
print(u - v)

# 2.3
print(6 * u)

# 2.4
print(u * v)

# 2.5
print(np.linalg.norm(u))

# 3. Matrix Operations

A = np.matrix([[1,2,3], [2,7,4]])
B = np.matrix([[1,-1], [0,1]])
C = np.matrix([[5, -1], [9, 1], [6, 0]])
D = np.matrix([[3,-2,-1], [1,2,3]])

# 3.1 "not defined"

# 3.2
print(A - C.T)

# 3.3
print(C.T + 3*D)

# 3.4
print(B*A)

# 3.5 not defined


