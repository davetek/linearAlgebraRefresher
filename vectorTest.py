#test vector class

import vector

v = [3.039, 1.879]
b = [0.825, 2.036]

v2 = [3.00034, 4.00035]

vVector = vector.Vector(v)
bVector = vector.Vector(b)
v2Vector = vector.Vector(v2)

sumOfVectors = bVector.addVectors(vVector)
print('sum: ' + str(sumOfVectors.coordinates))


differenceOfVectors = bVector.subtractVectorFromVector(vVector)
print('difference: ' + str(differenceOfVectors.coordinates))


s = 4

productOfVectorAndScalar = vVector.multiplyScalarAndVector(s)
print('product of vector and scalar: ' + str(productOfVectorAndScalar.coordinates))


magnitudeOfvVector = v2Vector.vectorMagnitude()
print('magnitude of vVector: ' + str(magnitudeOfvVector))

dotProductOfVectors = bVector.dotProductOfVectors(vVector)
print('dot product of bVector and vVector: ' + str(dotProductOfVectors))