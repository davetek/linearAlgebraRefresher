#test vector class

import vector

v = [3.039, 1.879]
b = [0.825, 2.036]


vVector = vector.Vector(v)
bVector = vector.Vector(b)

sumOfVectors = bVector.addVectors(vVector)
print('sum: ' + str(sumOfVectors.coordinates))


differenceOfVectors = bVector.subtractVectorFromVector(vVector)
print('difference: ' + str(differenceOfVectors.coordinates))


s = 4

productOfVectorAndScalar = vVector.multiplyScalarAndVector(s)
print('product of vector and scalar: ' + str(productOfVectorAndScalar.coordinates))
