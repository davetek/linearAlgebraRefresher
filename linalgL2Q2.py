

#for lesson 2 of Linear Algebra Refresher course, Quiz 2
# covering vector addition, subtraction, and multiplication

#import support module containing vector operation functions
import vectorOperations


##Lesson 2: 1.4 Quiz ex 1

#declare list of vectors
vectorList = [[8.218, -9.341], [-1.129, 2.111]]

#add the vectors
vectorOperations.addVectors(vectorList)

print ""


#Lesson 2: 1.4 Quiz ex 2
#declare list of vectors
vectorList = [[7.119, 8.215], [-8.223, 0.878]]

#subtract the vectors
vectorOperations.subtractVectors(vectorList)



#Lesson 2: 1.4 Quiz ex 3
#declare the scalar and vector on which to perform the operation
scalar = 7.41
vector = [1.671, -1.012, -0.318]

#multiply the scalar times the vector
vectorOperations.multiplyScalarAndVector(scalar, vector)

