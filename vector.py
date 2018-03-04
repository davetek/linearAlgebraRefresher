
from functools import reduce
from decimal import Decimal, getcontext, ROUND_HALF_UP
import math


class Vector(object):

    getcontext().prec = 20


    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates



    #DL Helper method to quantize the Decimal members in a coordinate list
    #round the Decimal coordinates to three decimal places
    def quantizeList(self, list):
        list = [ item.quantize(Decimal('.001'), rounding=ROUND_HALF_UP) for item in list]
        return list


    #DL quantize a Decimal scalar value to round to three decimal places
    def quantizeScalar(self, scalar):
        scalar = scalar.quantize(Decimal('.001'), rounding = ROUND_HALF_UP)
        return scalar


    #DL Add two vectors: self and another vector
    def addVectors(self, v):
        try:
            if not self.dimension == v.dimension:
                raise ValueError

            sumOfVectors = [Decimal(x) + Decimal(y) for x,y in zip(self.coordinates, v.coordinates)]

            #quantize (round) the Decimal coordinates
            sumOfVectors = self.quantizeList(sumOfVectors)

            return Vector(sumOfVectors)

        except ValueError:
            raise ValueError('The vectors must have the same number of coordinates')



    def subtractVectorFromVector(self, v):
        try:
            if not self.dimension == v.dimension:
                raise ValueError

            #subtract each coordinate in vector v from the matching coordinate in this vector,
            # and convert the result to a Decimal
            differenceOfVectors = [ Decimal(x) - Decimal(y) for x,y in zip(self.coordinates, v.coordinates)]

            #quantize (round) the Decimal coordinates
            differenceOfVectors = self.quantizeList(differenceOfVectors)
            
            return Vector(differenceOfVectors)

        except ValueError:
            raise ValueError('The vectors must have the same number of coordinates')


    def multiplyScalarAndVector(self, scalar):

        #convert each member in this Vector object's coordinates list to a Decimal type
        productOfScalarAndVector = [Decimal(scalar) * Decimal(coordinate) for coordinate in self.coordinates]

        #quantize (round) result
        productOfScalarAndVector = self.quantizeList(productOfScalarAndVector)

        return Vector(productOfScalarAndVector)


    def vectorMagnitude(self):

        #use list comprehension to square each coordinate in the vector
        vectorSquared = [coordinate**2 for coordinate in self.coordinates]

        #sum the squared coordinates, and then compute the square root of the sum; cast result as Decimal
        vectorMagnitude = Decimal(math.sqrt(math.fsum(vectorSquared)))

        #quantize (round) the scalar magnitude value to three decimal places
        vectorMagnitude = self.quantizeScalar(vectorMagnitude)

        return vectorMagnitude


    def dotProductOfVectors(self, v):
        #dot product can be defined as the sum of the products of matching coordinates from each of n vectors

        #compute product of matching coordinates
        dotProduct = Decimal(math.fsum([ x*y for x,y in zip(self.coordinates, v.coordinates)]))

        #quantize (round) result
        dotProduct = self.quantizeScalar(dotProduct)

        return dotProduct


        


        





