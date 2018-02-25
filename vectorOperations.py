#functions module for Linear Algebra Refresher course
# created for Lesson 2, ex. 4 Quiz
# covering vector addition, subtraction, and multiplication


#import decimal module to retain significant decimal places in operations
from decimal import getcontext, Decimal, ROUND_UP
getcontext().prec = 20

import math

# for the reduce function in python 3.x
import functools


# for Lesson 2, Quiz 4

## inside a list comprehension, unpack the list of lists (vectors) parameter
## and zip the unpacked lists to produce new lists, one list for each coordinate (item#)
##  then use a list comprehension with sum() to sum each of the zipped lists
##  and return the resulting list which is the sum of the input vectors
def addVectors(listOfVectors):
	
	sumVectors = [ sum(listOfSameCoordinate) for listOfSameCoordinate in zip(*listOfVectors)]
	return sumVectors



## inside a list comprehension, unpack the list of lists (vectors) parameter
## and zip the unpacked lists to produce new lists, one list for each coordinate (item#)
##  then use a list comprehension with with reduce() to get the difference of the items in each zipped list
##  by computing (item 1 - item 2, then result - item 3, and so on)
##  and return the resulting list which is the difference of the input of the input vectors
def subtractVectors(listOfVectors):

	differenceOfVectors = [ reduce(lambda a, b: a - b, listOfSameCoordinate) for listOfSameCoordinate in zip(*listOfVectors)]
	return differenceOfVectors



def multiplyScalarAndVector(scalar, vector):
	# 1/28/2018, revise function to convert the parameter values to decimal numbers with a defined precision

	print("in multiplyScalarAndVector function")
	print("input scalar: " + str(scalar))
	print("input vector: " + str(vector))

	scalarDec = Decimal(scalar)
	scalardec = scalarDec.quantize(Decimal('.001'), rounding=ROUND_UP)

	vectorDec = [Decimal(coordinate) for coordinate in vector]

	print("Decimal scalar: " + str(scalarDec))
	print("Decimal vector: " + str(vectorDec))

	productOfScalarAndVector = [ scalarDec*coordinate for coordinate in vectorDec]

	return productOfScalarAndVector



##created for Lesson2.1, Quiz 6

def vectorMagnitude(vector):
	#this function computes the length of a vector using the Pythagorean theorem

	## use a list comprehension to square each coordinate in the input vector
	vectorCoordinatesSquared = [coordinate**2 for coordinate in vector]

	##compute the square root of the (sum of the squared coordinates as a float)
	vectorMagnitude = math.sqrt(math.fsum(vectorCoordinatesSquared))
	return vectorMagnitude



## 7/23: revise function to use try block to check for zero division error
## this is also called vector normalization; it provides the unit vector,
##  also called the direction vector (Wolfram Mathworld), with length 1
def vectorDirection(vector):
	try: 
		magnitudeOfVector = vectorMagnitude(vector)
		vectorDirection = multiplyScalarAndVector(1/magnitudeOfVector, vector)
		print('in Vector Direction function')
		print('   vector direction (unit vector): ' + str(vectorDirection))
		return vectorDirection

	except ZeroDivisionError:
		print("Cannot normalize the zero vector")
		raise Exception('Cannot normalize the zero vector')



## created for Lesson 2.1, Quiz 8

## inside a list comprehension, unpack the list of lists (vectors) parameter
## and zip the unpacked lists to produce new lists, one list for each coordinate (item#)
##  then use a list comprehension with with reduce() to get the product of the items in each zipped list
##  by computing (item 1 * item 2, then result * item 3, and so on)
##  and return the resulting list of the product of each like coordinate in the input vectors
##  (added 7/22) then use another reduce() to sum the computed vector 
##  (chose to use reduce() instead of sum() as an exercise

## Edited to use decimal calculations on 11/12/2017 after Liam pointed out this can fail as a floating point 
## calculation because 0 may only be 0 to a certain number of decimal places. 
def dotProductOfVectors(listOfVectors):
	getcontext().prec = 3
	dotProductOfVectors = functools.reduce(lambda y, z: Decimal(y) + Decimal(z), [ functools.reduce(lambda a, b: Decimal(a) * Decimal(b), listOfSameCoordinate) for listOfSameCoordinate in zip(*listOfVectors)])
	return Decimal(dotProductOfVectors)


## Takes two vectors of the same dimension (same number of coordinates in each),
## and computes the angle between them; note that math.acos returns the arc cosine of x, in radians
## so the output of this function is in radians unless the optional 3rd parameter is True

def angleBetweenVectors(vector1, vector2, *outputDegrees):
	
	try:
		listOfVectors = [vector1, vector2]

		dotProduct = dotProductOfVectors(listOfVectors)
		#print "dot product = " + str(dotProduct)

		magnitudeOfVector1 = vectorMagnitude(vector1)
		#print "magnitude of vector 1 = " + str(magnitudeOfVector1)

		magnitudeOfVector2 = vectorMagnitude(vector2)
		#print "magnitude of vector 2 = " + str(magnitudeOfVector2)

		angleBetweenVectors = math.acos(dotProduct/(magnitudeOfVector1 * magnitudeOfVector2))

		#check for optional third parameter is True; if if is, convert angle from radians to degrees
		if outputDegrees:
			angleBetweenVectors = math.degrees(angleBetweenVectors)

		return angleBetweenVectors

	except Exception as e:
		if str(e) == 'Cannot normalize the zero vector':
			raise Exception('Cannot calculate an angle with a zero vector')
		else:
			raise e

	
## for Lesson 2.1, Quiz 10 (Sep 2017, picked up in Oct 2017)
## Check if two vectors v and w are parallel ()
## Given two vectors of the same dimension (same number of coordinates in each),
## Check if either vector is the zero vector (all items are zero). If so, the vectors are parallel. Stop here.
## Check if either has vector contains a zero item (but not all zero's). If so, the vectors are not parallel. Stop here.
## Divide the first element of one of the vectors by the first element of the second vector (first/second is arbitrary)
## and record the resulting number
## Then do the same for the second element, and so on. 
## Compare the dividends. If equal, the vectors are parallel.


## created for Lesson 2.1, Quiz 10  (Nov 2017)
## check if two vectors are parallel

def checkForParallelVectors(vector1, vector2):

	results = []
	vectorsAreParallel = False
	reasonForResult = ''

	
	if 0 in vector1:
		# if the vector contains a zero value,
		# check if all values in vector1 are the same
		# because all members of a set must be unique, if set has only one member,
		# then the vector contains all zeros - it is a 'zero vector' so vectors are parallel
		if len(set(vector1)) == 1:
			reasonForResult =  "one of the vectors is a zero vector"
			vectorsAreParallel = True
		else:
			reasonForResult = "some but not all elements in a vector are zero"
			vectorsAreParallel = False
			# if not all values are zero, then the vetors are not parallel

	elif 0 in vector2:
		# check if all values in vector2 are the same
		# because all members of a set must be unique, if set has only one member,
		# then the vector members were all equal to each other
		if len(set(vector2)) == 1:
			reasonForResult = "one of the vectors is a zero vector"
			vectorsAreParallel = True
		else:
			reasonForResult = "some but not all elements in a vector are zero"
			vectorsAreParallel = False

	else: 
		# set the precision of decimal precision to limit to 3 places. If not done, the result of divisions 
		# may be arbitrarily long, so that dividends that would be equal to for example, 4 decimal places
		# are not equal when each has 10 decimal places
		getcontext().prec = 3
		for i in range(len(vector2)):
			dividend = Decimal(vector2[i]) / Decimal(vector1[i])
			results.append(dividend)		

		reasonForResult = "dividend of each coordinate pair in vectors: " + str(results)

		#if all of the resulting dividends are equal, the resultings set has only one member
		# and the vectors are parallel, else they are not parallel.
		if len(set(results)) == 1:
			vectorsAreParallel = True
		else:
			vectorsAreParallel = False

	if vectorsAreParallel:
		print(str(vector1) + " and " + str(vector2) + " are parallel")
		print('because ' + reasonForResult)
	else:
		print(str(vector1) + " and " + str(vector2) + " are not parallel")
		print('because ' + reasonForResult)
	
	return vectorsAreParallel

	


	

## for Lesson 2.1, Quiz 12 - started 11/28/2017
## implement the derivation of the projection formula
# given a base vector b and another vector v that has the same origin as b
# length of parallel vector v || = dot product of v with normalization of b

def projectVectorOnBaseVector(vector, baseVector):
	v = vector
	b = baseVector

	print('\n')
	print('In projectVectorOnBaseVector function')

	bUnitVector = vectorDirection(b)
	#print( "bUnitVector: " + str(bUnitVector))

	dotProdVectorWithBUnitVector = dotProductOfVectors([v, bUnitVector])
	print( "dot product of vector and bUnitVector: "  + str(dotProdVectorWithBUnitVector))

	projectionVectorBUnitVector = multiplyScalarAndVector(dotProdVectorWithBUnitVector, bUnitVector)
	print( "projection of vector v on base vector b is: " + str(projectionVectorBUnitVector))


	return projectionVectorBUnitVector





