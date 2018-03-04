
from functools import reduce
from decimal import Decimal, getcontext, ROUND_UP

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


    #DL Add two vectors: self and another vector
    def addVectors(self, v):
        try:
            if not self.dimension == v.dimension:
                raise ValueError

            sumVectors = [sum(listOfSameCoordinate) for listOfSameCoordinate in zip(self.coordinates, v.coordinates)]
            return sumVectors

        except ValueError:
            raise ValueError('The vectors must have the same number of coordinates')


    def subtractVectorFromVector(self, v):
        try:
            if not self.dimension == v.dimension:
                raise ValueError

            #subtract the indicated vector v from this vector, and convert each resulting coordinate to a Decimal
            differenceOfVectors = [ (Decimal(listOfSameCoordinate[0]) - Decimal(listOfSameCoordinate[1])) \
            for listOfSameCoordinate in zip(self.coordinates, v.coordinates)]

            #round the Decimal coordinates to three decimal places
            differenceOfVectors = [ coordinate.quantize(Decimal('.001'), rounding=ROUND_UP) for coordinate in differenceOfVectors]
            
            return differenceOfVectors

        except ValueError:
            raise ValueError('The vectors must have the same number of coordinates')



