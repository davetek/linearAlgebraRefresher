
from functools import reduce
from decimal import Decimal, getcontext, ROUND_HALF_UP

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


    #DL Add two vectors: self and another vector
    def addVectors(self, v):
        try:
            if not self.dimension == v.dimension:
                raise ValueError

            sumOfVectors = [Decimal(x) + Decimal(y) for x,y in zip(self.coordinates, v.coordinates)]

            #quantize (round) the Decimal coordinates to three decimal places
            sumOfVectors = self.quantizeList(sumOfVectors)

            return Vector(sumOfVectors)

        except ValueError:
            raise ValueError('The vectors must have the same number of coordinates')



    def subtractVectorFromVector(self, v):
        try:
            if not self.dimension == v.dimension:
                raise ValueError

            #subtract the indicated vector v from this vector, and convert each resulting coordinate to a Decimal
            differenceOfVectors = [ Decimal(x) - Decimal(y) for x,y in zip(self.coordinates, v.coordinates)]

            #quantize (round) the Decimal coordinates to three decimal places
            differenceOfVectors = self.quantizeList(differenceOfVectors)
            
            return Vector(differenceOfVectors)

        except ValueError:
            raise ValueError('The vectors must have the same number of coordinates')



