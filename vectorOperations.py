#functions module for Linear Algebra Refresher course
# created for Lesson 2, ex. 4 Quiz
# covering vector addition, subtraction, and multiplication


#import decimal module to retain significant decimal places in operations
from decimal import *


def addVectors(vector1, vector2):

	#create empty sum list
	sumVector = []


	for i in range(len(vector1)):
		#set the number of significant digits. For some reason 4 means 3 decimal places
		getcontext().prec = 10
		sum = Decimal(vector1[i]) + Decimal(vector2[i])
		sumVector.append(sum)

	print"***VECTOR ADDITION***"
	print "vector 1 is:"
	for coord in vector1:
		print coord

	print ""

	print "vector 2 is:"
	for coord in vector2:
		print coord

	print ""

	print "vector 1 + vector 2 is "
	for coord in sumVector:
		print round(coord,3)


def subtractVectors(vector1, vector2):

	#create empty difference list
	differenceVector = []


	for n in range(len(vector1)):
		#set the number of significant digits. For some reason 4 means 3 decimal places
		getcontext().prec = 10
		difference = Decimal(vector1[n]) - Decimal(vector2[n])
		differenceVector.append(difference)

	print"***VECTOR SUBTRACTION***"
	print "vector 1 is:"
	for coord in vector1:
		print coord

	print ""

	print "vector 2 is:"
	for coord in vector2:
		print coord

	print ""

	print "vector 1 - vector 2 is "
	for coord in differenceVector:
		print round(coord,3)


def multiplyScalarAndVector(scalar, vector):

	#create empty product list
	productVector = []


	for n in range(len(vector)):
		#set the number of significant digits. For some reason 4 means 3 decimal places
		product = (scalar) * (vector[n])
		productVector.append(product)

	print"***VECTOR MULTIPLICATION***"
	print "scalar is:"
	print scalar

	print ""

	print "vector:"
	for coord in vector:
		print coord

	print ""

	print "scalar * vector:"
	for coord in productVector:
		print round(coord,3)
