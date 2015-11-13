import math

#Returns the angle between 2 vectors in radians
def getAngleDiff(vec1, vec2):
    dist = vec1 - vec2
    return dist.getAngle()

#Returns the distance between 2 vectors
def getDistance(vec1, vec2):
    dist = vec1 - vec2
    return dist.getLen()

#Returns the dot product of 2 vectors
#|vec1|*|vec2|*cos(angleDiff(vec1, vec2))
def dotProduct(vec1, vec2):
    return vec1.getLen() * vec2.getLen() * math.cos(getAngleDiff(vec1, vec2))

def mult2(vec1, vec2):
    return vec1.x * vec2.x + vec1.y * vec2.y


class Vec2:
    x = 0
    y = 0
    def __init__(self):
        self.x = 0
        self.y = 0
    def __init__(self, x, y=None):
        if(isinstance(x, tuple)):
            self.x = x[0]
            self.y = x[1]
            return

        self.x = x
        self.y = y

    def __str__(self):
        return "[{}, {}]".format(self.x, self.y)
    
    #Add 2 vectors and return the result
    def __add__(self, other):
        return Vec2(self.x + other.x, self.y + other.y)

    #Subtract 2 vectors and return the result 
    def __sub__(self, other):
        return Vec2(self.x - other.x, self.y - other.y)

    #Multiply a vector and a number and return the result
    def __mul__(self, other):
        return Vec2(self.x * other, self.y * other)
    
    def __div__(self, other):
        return Vec2(self.x / other, self.y / other)

    def __truediv__(self, other):
        return Vec2(self.x / other, self.y / other)

    def __neg__(self):
        return Vec2(-self.x, -self.y)
    
    #Returns the length of the vector
    def getLen(self):
        return math.sqrt(self.x**2 + self.y**2)

    #Returns the angle of the vector
    def getAngle(self):
        return math.atan2(self.y, self.x)

    def normalized(self):
        return self / self.getLen()

    def __le__(self, other):
        return self.x <= other.x and self.y <= other.y
    def __ge__(self, other):
        return self.x >= other.x and self.y >= other.y

    def getTuple(self):
        return (self.x, self.y)


if __name__ == "__main__":
    vec1 = Vec2(2.0, 1.0)
    vec2 = Vec2(3.0, 3.0)

    print("Mult ", vec1 * 2)
    print("Sub ", vec1 - vec2)
    print("Add ", vec1 + vec2)
    print("Div ", vec1 / 2)
    print("GT ", vec1 >= vec2)
    print("lt", vec1 <= vec2)
