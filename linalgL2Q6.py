#for lesson 2 of Linear Algebra Refresher course, part 1, Quiz 6
# covering vector magnitude and direction

#import support module containing vector operation functions
import vectorOperations


print "Lesson 2: 1.6 Quiz ex 1"
#declare the vectors to perform operations on
inputVectorQ6ex1 = [-0.221, 7.437]

print "magnitude of " + str(inputVectorQ6ex1) + ":"

#get and print the vector magnitude
print vectorOperations.vectorMagnitude(inputVectorQ6ex1)
print ""



print "Lesson 2: 1.6 Quiz ex 2"
#declare the vectors to perform operations on
inputVectorQ6ex2 = [8.813, -1.331, -6.247]

print "magnitude of " + str(inputVectorQ6ex2) + ":"

#get and print the vector magnitude
print vectorOperations.vectorMagnitude(inputVectorQ6ex2)
print ""



print "Lesson 2: 1.6 Quiz ex 3"
#declare the vectors to perform operations on
inputVectorQ6ex3 = [5.581, -2.136]

print "direction of " + str(inputVectorQ6ex3) + ":"

#get and print the vector magnitude
print vectorOperations.vectorDirection(inputVectorQ6ex3)
print ""



print "Lesson 2: 1.6 Quiz ex 4"
#declare the vectors to perform operations on
inputVectorQ6ex4 = [1.996, 3.108, -4.554]

print "direction of " + str(inputVectorQ6ex4) + ":"

#get and print the vector magnitude
print vectorOperations.vectorDirection(inputVectorQ6ex4)
print ""



print "Lesson 2: 1.6 Quiz 6 (test of zero vector)"
#declare the vectors to perform operations on
inputVectorQ6testzero = [0, 0, 0]

print "direction of " + str(inputVectorQ6testzero) + ":"

#get and print the vector magnitude
print vectorOperations.vectorDirection(inputVectorQ6testzero)
print ""


