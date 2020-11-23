from math import sqrt
from math import cos

"""
Common 3D Vector class for arithmetical uses or game development
"""


class Vector:
    # constant for infinity vector
    __INF = float('Infinity')

    # constant for dot product results
    DotProductResult = {-1: 'Opposite', 0: 'Perpendicular', 1: 'Identical'}

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'Vector(x: {self.x}, y: {self.y}, z: {self.z})'

    # operator-
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    # operator+
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    # operator*
    def __mul__(self, other):
        return Vector(self.x * other.x, self.y * other.y, self.z * other.z)

    # operator/
    def __truediv__(self, other):
        return Vector(self.x / other.x, self.y / other.y, self.z / other.z)

    # operator==
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    # operator**
    def __pow__(self, power, modulo=None):
        result = Vector(1, 1, 1)
        for i in range(power):
            result.x *= self.x
            result.y *= self.y
            result.z *= self.z
        return result

    # ----------------Methods----------------
    # calculate magnitude of Vector
    def Length(self):
        return sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    # normalize Vector to unit length 1
    def Normalized(self):
        magnitude = self.Length()
        self.x /= magnitude
        self.y /= magnitude
        self.z /= magnitude
        return self

    # return angle between two Vectors
    def Angle(self, other):
        return cos((Vector.DotProduct(self, other) / self.Length() + other.Length()))

    # ---------------Static-Methods----------------
    # Negates all Vector's components
    @staticmethod
    def OppositeVector(v):
        return Vector(-v.x, -v.y, -v.z)

    @staticmethod
    def DotProduct(a, b):
        return a.x * b.x + a.y * b.y + a.z * b.z

    # ---------------Class-Methods----------------
    #     shortcut for creating common Vectors
    @classmethod
    def NullVector(cls):
        return cls(0, 0, 0)

    @classmethod
    def InfinityVector(cls):
        return cls(Vector.__INF, Vector.__INF, Vector.__INF)

    @classmethod
    def UpVector(cls):
        return cls(0, 1, 0)

    @classmethod
    def DownVector(cls):
        return cls(0, -1, 0)

    @classmethod
    def RightVector(cls):
        return cls(1, 0, 0)

    @classmethod
    def LeftVector(cls):
        return cls(-1, 0, 0)

    @classmethod
    def ForwardVector(cls):
        return cls(0, 0, 1)

    @classmethod
    def BackVector(cls):
        return cls(0, 0, -1)

class Rectangle(Vector):
    def __init__(self, x, y, z, w):
        super().__init__(x, y, z)
        self.w = w
        # obdelnik XYZW

    def Area(self):
        XY = Vector(self.x, self.y, 0).Length()
        YZ = Vector(self.z, self.w, 0).Length()

        #S = a * b
        S = (XY * YZ)
        print("Area S = ", round(S, 2), "cm.")


# ------------------------------------------------------------------------------------------------------------------
#                                                 praktická část
# ------------------------------------------------------------------------------------------------------------------
v1 = Vector(5, 6, 9)
print(v1)
print(type(v1))
print("Is v1 an instance of vector? ", isinstance(v1, Vector))

right = Vector.RightVector()
up = Vector.UpVector()

print(f'\nRight: {right} and up: {up}\n'
      f'Dot product of {right} and {up} is: {Vector.DotProductResult[Vector.DotProduct(right, up)]}\n'
      f'Normalized {v1} = {v1.Normalized()} of length: {v1.Length()}')

v2 = Vector(4, 2, 5)
v3 = Vector(1, 2, 7)
v4 = v3
print(f'\nOperators:\n'
      f'(v3**2 == v4 * v3) is {v3**2 == v4 * v3}\n'
      f'v2 + v4 = {v2 + v4}\n'
      f'v2 - v4 = {v2 - v4}\n')

vINF = Vector.InfinityVector()
print(vINF, "with infinity values")

v2_Opposite = Vector.OppositeVector(v2)
print("Opposite vector to", v2, " is:", v2_Opposite)

a = Vector(1, 2, 0)
b = Vector(2, 4, 0)

r = Rectangle(a.x, a.y, b.x, b.y)

r.Area()