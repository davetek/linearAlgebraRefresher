#for lesson 2 of Linear Algebra Refresher course, part 1, Quiz 10
# covering checks for vector parallelism and orhogonality

from decimal import * 

#import support module containing vector operation functions
import vectorOperations

# only enabled if dot product != 0
checkAngleBetweenVectors = False

print "Lesson 2: 1.10 Quiz exc 1"
#declare the vectors to perform operations on

v1 = [-7.579, -7.88]
w1 = [22.737, 23.64]

#check if vectors are parallel and report results
result = vectorOperations.checkForParallelVectors(v1, w1)

#check if vectors are orthogonal by computing the dot product
vectors1 = [v1, w1] # make a list of vectors for the dotProduct function
dotProduct = vectorOperations.dotProductOfVectors(vectors1)
if dotProduct == 0:
	print "vectors are orthogonal; dot product is " + str(dotProduct)
else:
	print "vectors are not orthogonal; dot product is " + str(dotProduct)

print ""


print "Lesson 2: 1.10 Quiz exc 2"
#declare the vectors to perform operations on
v2 = [-2.029, 9.97, 4.172]
w2 = [-9.231, -6.639, -7.245]

#check if vectors are parallel and report results
result = vectorOperations.checkForParallelVectors(v2, w2)

vectors2 = [v2, w2] # make a list of vectors for the dotProduct function
dotProduct = vectorOperations.dotProductOfVectors(vectors2)
if dotProduct == 0:
	print "vectors are orthogonal; dot product is " + str(dotProduct)
else:
	print "vectors are not orthogonal; dot product is " + str(dotProduct)

print ""


print "Lesson 2: 1.10 Quiz exc 3"
#declare the vectors to perform operations on
v3 = [-2.328, -7.284, -1.214]
w3 = [-1.821, 1.072, -2.94]

#check if vectors are parallel and report results
result = vectorOperations.checkForParallelVectors(v3, w3)

vectors3 = [v3, w3] # make a list of vectors for the dotProduct function
dotProduct = vectorOperations.dotProductOfVectors(vectors3)
if dotProduct == 0:
	print "vectors are orthogonal; dot product is " + str(dotProduct)
else:
	print "vectors are not orthogonal; dot product is " + str(dotProduct)

print ""




print "Lesson 2: 1.10 Quiz exc 4"
#declare the vectors to perform operations on
v4 = [2.118, 4.827]
w4 = [0, 0]

#check if vectors are parallel and report results
result = vectorOperations.checkForParallelVectors(v4, w4)

vectors4 = [v4, w4] # make a list of vectors for the dotProduct function
getcontext().prec = 3
dotProduct = vectorOperations.dotProductOfVectors(vectors4)
if dotProduct == 0:
	print "vectors are orthogonal; dot product is " + str(dotProduct)
else:
	print "vectors are not orthogonal; dot product is " + str(dotProduct)

print ""



print "Lesson 2: 1.10 Quiz exc - extra 1"
#declare the vectors to perform operations on
vx1 = [2.118, 0]
wx1 = [1.059, 2.41]

#check if vectors are parallel and report results
result = vectorOperations.checkForParallelVectors(vx1, wx1)

vectorsx1 = [vx1, wx1] # make a list of vectors for the dotProduct function
dotProduct = vectorOperations.dotProductOfVectors(vectorsx1)
if dotProduct == 0:
	print "vectors are orthogonal; dot product is " + str(dotProduct)
else:
	print "vectors are not orthogonal; dot product is " + str(dotProduct)

print ""

