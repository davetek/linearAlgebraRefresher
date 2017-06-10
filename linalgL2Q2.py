

#for lesson 2 of Linear Algebra Refresher course, Quiz 2
# covering vector addition, subtraction, and multiplication

#import support module containing vector operation functions
import vectorOperations

#Lesson 2: 1.4 Quiz ex 1
#declare the vectors to perform operations on
inputVector1 = [8.218, -9.341]
inputVector2 = [-1.129, 2.111]


#add the vectors
vectorOperations.addVectors(inputVector1, inputVector2)

print ""

#Lesson 2: 1.4 Quiz ex 2
#declare the vectors to perform operations on
inputVector1 = [7.119, -8.223]
inputVector2 = [-8.215, 0.878]

vectorOperations.subtractVectors(inputVector1, inputVector2)


#Lesson 2: 1.4 Quiz ex 3
#Declare the scalar and vector on which to perform the operation
scalar1 = 7.41
inputVector1 = [1.671, -1.012, -0.318]

vectorOperations.multiplyScalarAndVector(scalar1, inputVector1)

