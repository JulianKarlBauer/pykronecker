import numpy as np
from pykronecker import KroneckerProduct

A = np.random.normal(size=(5, 5))
B = np.random.normal(size=(6, 6))
C = KroneckerProduct([A, B])

###################################

x = np.random.normal(size=5 * 6)
X = np.random.normal(size=(5, 6))
print(C @ x)
print(C @ X)

###################################

from pykronecker import KroneckerSum

D = KroneckerSum([A, B])
print(D @ x)

###################################

from pykronecker import KroneckerDiag

E = KroneckerDiag(np.random.normal(size=(5, 6)))
print(E @ x)

###################################

from pykronecker import KroneckerIdentity

I1 = KroneckerIdentity(like=E)
I2 = KroneckerIdentity(tensor_shape=(5, 6))
print(I1 @ x, I2 @ x)

###################################

F = C @ D + C @ E
print(F @ x)

###################################

G = 2 * F.T + E / 5 
print(G @ x)

###################################

H = C * D
print(H @ x)

###################################

from pykronecker import KroneckerBlock

# Block of pure KroneckerOperators
M = KroneckerBlock([[C, D], 
                    [E, F]])

print(M @ np.random.normal(size=5 * 6 * 2))

# Block with mixture of KroneckerOperators and ndarrays
N11 = E
N12 = np.ones((5 * 6, 5))
N21 = np.random.normal(size=(5, 5 * 6))
N22 = np.eye(5)

N = KroneckerBlock([[N11, N12], 
                    [N21, N22]])

print(N @ np.random.normal(size=5 * 6 + 5 ))

###################################

from pykronecker import KroneckerBlockDiag

J = KroneckerBlockDiag([E, F])
print(M @ np.random.normal(size=5 * 6 * 2))

###################################

H = (C @ E).inv()
print(H @ x)

###################################

print(F.sum(0))
print(F.sum(1))
print(F.sum())

###################################

print(H.to_array())

###################################

print(C ** 2)

###################################

print(C.diag())

###################################

print(C.H)
