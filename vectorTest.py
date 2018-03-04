#test vector class

import vector

v = [3.039, 1.879]
b = [0.825, 2.036]


vVector = vector.Vector(v)
bVector = vector.Vector(b)

sumVectors = bVector.addVectors(vVector)
print(sumVectors)


differenceOfVectors = bVector.subtractVectorFromVector(vVector)
print(differenceOfVectors)
