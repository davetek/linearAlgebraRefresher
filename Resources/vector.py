class Vector(object):
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


    #DL overload the + operator to sum two vectors: self and another vector
    def addVectors(self, v):
        try:
            if not self.dimension == v.dimension:
                raise ValueError

            sumVectors = [sum(listOfSameCoordinate) for listOfSameCoordinate in zip(self, v)]
            return sumVectors


