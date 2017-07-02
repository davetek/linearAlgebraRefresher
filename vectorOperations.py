#functions module for Linear Algebra Refresher course
# created for Lesson 2, ex. 4 Quiz
# covering vector addition, subtraction, and multiplication


#import decimal module to retain significant decimal places in operations
from decimal import *
import math


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

	productOfScalarAndVector = [ scalar*coordinate for coordinate in vector]
	return productOfScalarAndVector



##created for Lesson2.1, Quiz 6

def vectorMagnitude(vector):

	## use a list comprehension to square each coordinate in the input vector
	vectorCoordinatesSquared = [coordinate**2 for coordinate in vector]

	##compute the square root of the (sum of the squared coordinates as a float)
	vectorMagnitude = math.sqrt(math.fsum(vectorCoordinatesSquared))
	return vectorMagnitude


def vectorDirection(vector):
	magnitudeOfVector = vectorMagnitude(vector)
	if magnitudeOfVector != 0:
		scalar = 1/magnitudeOfVector
		vectorDirection = multiplyScalarAndVector(scalar, vector)
		return vectorDirection
	else:
		return []



