#pythonTestV2

import vectorOperationsV2 as vo2
#from decimal import Decimal

#TESTS

# test values
v = [3.039, 1.879]
b = [0.825, 2.036]

bUnitVector = vo2.vectorDirection(b)
print('b unit vector: ' + str(bUnitVector))

vectorLength = vo2.vectorMagnitude(b)
print('vector b magnitude: ' + str(vectorLength))


productOfScalarAndVector = vo2.multiplyScalarAndVector(vectorLength, bUnitVector)
print('product of scalar and vector: ' + str(productOfScalarAndVector))

dotProductOfVectors = vo2.dotProductOfVectors([v, bUnitVector])
print('dot product of v and bUnitVector: ' + str(dotProductOfVectors))
print(type(dotProductOfVectors))


print('\n')
vectorProjection = vo2.projectVectorOnBaseVector(v, b)
print('vector projection of v on b:' + str(vectorProjection))
