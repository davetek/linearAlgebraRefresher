from decimal import getcontext, Decimal, ROUND_DOWN, ROUND_UP, ROUND_HALF_DOWN, ROUND_HALF_UP

import math

# for the reduce function in python 3.x
import functools


#set precision, i.e. significant digits, for Decimal numbers
# note the it is set high to ensure that there are enough decimal places
# in the number to round down to 3 decimal places if possible using the Decimal quantize method
getcontext().prec = 20


## Edited to use decimal calculations on 11/12/2017 after Liam pointed out this can fail as a floating point 
## calculation because 0 may only be 0 to a certain number of decimal places. 
def dotProductOfVectors(listOfVectors):
	dotProductOfVectors = functools.reduce(lambda y, z: Decimal(y) + Decimal(z), [ functools.reduce(lambda a, b: Decimal(a) * Decimal(b), listOfSameCoordinate) for listOfSameCoordinate in zip(*listOfVectors)])
	dotProductOfVectors = Decimal(dotProductOfVectors).quantize(Decimal('.00001'), rounding=ROUND_DOWN)
	return Decimal(dotProductOfVectors)



## 7/23: revise function to use try block to check for zero division error
## this is also called vector normalization; it provides the unit vector,
##  also called the direction vector (Wolfram Mathworld), with length 1
def vectorDirection(vector):
	try: 
		magnitudeOfVector = vectorMagnitude(vector)
		vectorDirection = multiplyScalarAndVector(1/magnitudeOfVector, vector)
		#print('in Vector Direction function')
		#print('   vector direction (unit vector): ' + str(vectorDirection))
		return vectorDirection

	except ZeroDivisionError:
		print("Cannot normalize the zero vector")
		raise Exception('Cannot normalize the zero vector')



##created for Lesson2.1, Quiz 6

def vectorMagnitude(vector):
	#this function computes the length of a vector using the Pythagorean theorem

	## use a list comprehension to square each coordinate in the input vector
	vectorCoordinatesSquared = [coordinate**2 for coordinate in vector]

	##compute the square root of the (sum of the squared coordinates as a float)
	vectorMagnitude = math.sqrt(math.fsum(vectorCoordinatesSquared))
	vectorMagnitudeDec = Decimal(vectorMagnitude).quantize(Decimal('.00001'), rounding=ROUND_DOWN)
	
	return vectorMagnitudeDec




def multiplyScalarAndVector(scalar, vector):
	# 1/28/2018, revise function to convert the parameter values to decimal numbers with a defined precision

	#print("in multiplyScalarAndVector function")
	#print("input scalar: " + str(scalar))
	#print("input vector: " + str(vector))

	##scalarDec = Decimal(scalar).quantize(Decimal('.00001'), rounding=ROUND_DOWN)
	#scalardec = scalarDec.quantize(Decimal('.00001'), rounding=ROUND_DOWN)

	##vectorDec = [Decimal(coordinate).quantize(Decimal('.00001'), rounding=ROUND_DOWN) for coordinate in vector]

	#print("Decimal scalar: " + str(scalarDec))
	#print("Decimal vector: " + str(vectorDec))

	#productOfScalarAndVector = [(scalarDec*coordinate).quantize(Decimal('.001'), rounding=ROUND_DOWN) for coordinate in vectorDec]
	
	#productOfScalarAndVector = [Decimal('1.0826146331693060657'), Decimal('2.6717616886457058218')]
	productOfScalarAndVector = [Decimal(scalar)*Decimal(coordinate) for coordinate in vector]
	productOfScalarAndVector = [coordinate.quantize(Decimal('.001'), rounding=ROUND_UP) for coordinate in productOfScalarAndVector]

	return productOfScalarAndVector



# for Lesson 2.1, Quiz 12 - started 11/28/2017
## implement the derivation of the projection formula
# given a base vector b and another vector v that has the same origin as b
# length of parallel vector v || = dot product of v with normalization of b

def projectVectorOnBaseVector(vector, baseVector):
	v = vector
	b = baseVector

	print('\n')
	print('In projectVectorOnBaseVector function')

	bUnitVector = vectorDirection(b)
	print( "bUnitVector: " + str(bUnitVector))

	dotProdVectorWithBUnitVector = dotProductOfVectors([v, bUnitVector])
	print( "dot product of vector and bUnitVector: "  + str(dotProdVectorWithBUnitVector))

	projectionVectorBUnitVector = multiplyScalarAndVector(dotProdVectorWithBUnitVector, bUnitVector)
	#print( "projection of vector v on base vector b is: " + str(projectionVectorBUnitVector))


	return projectionVectorBUnitVector






