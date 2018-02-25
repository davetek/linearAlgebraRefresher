#for lesson 2 of Linear Algebra Refresher course, part 1, Quiz 8
# covering vector magnitude and direction

#import support module containing vector operation functions
import vectorOperations

print "Lesson 2: 1.8 Quiz exc 1"
#declare the vectors to perform operations on
inputVectors = [[7.887, 4.138], [-8.802, 6.776]]

print "dot product of " + str(inputVectors) + ":"

#get and print the vector magnitude
print vectorOperations.dotProductOfVectors(inputVectors)
print ""


print "Lesson 2: 1.8 Quiz exc 2"
#declare the vectors to perform operations on
inputVectors = [[-5.955, -4.904, -1.874], [-4.496, -8.755, 7.103]]

print "dot product of " + str(inputVectors) + ":"

#get and print the vector magnitude
print vectorOperations.dotProductOfVectors(inputVectors)
print ""


print "Lesson 2: 1.8 Quiz exc 3"
#declare the vectors to perform operations on
inputVector3a = [3.183, -7.627]
inputVector3b = [-2.668, 5.319]

print "angle between " + str(inputVector3a) + " and " + str(inputVector3b) + ":"

#compute and print the angle between the input vectors
print "radians: " + str(vectorOperations.angleBetweenVectors(inputVector3a, inputVector3b))
print ""

print "Lesson 2: 1.8 Quiz exc 4"
#declare the vectors to perform operations on
inputVector4a = [7.35, 0.221, 5.188]
inputVector4b = [2.751, 8.259, 3.985]

print "angle between " + str(inputVector4a) + " and " + str(inputVector4b) + ":"

#compute and print the angle between the input vectors, passing True for optional third parameter to output degrees
print "degrees: " + str(vectorOperations.angleBetweenVectors(inputVector4a, inputVector4b, True))
print ""

#test zero vector
#declare the vectors to perform operations on
inputVectorZero = [0, 0, 0]
inputVector4b = [2.751, 8.259, 3.985]

print "angle between " + str(inputVectorZero) + " and " + str(inputVector4b) + ":"

#compute and print the angle between the input vectors, passing True for optional third parameter to output degrees
print "degrees: " + str(vectorOperations.angleBetweenVectors(inputVectorZero, inputVector4b, True))
print ""


