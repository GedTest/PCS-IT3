from math import sqrt
from math import cos

"""
Common 3D Vector class for arithmetical uses or game development
"""


class Vector:
    # constant for infinity vector
    __INF = float('Infinity')

    # constant for dot product results
    DOT_PRODUCT_RESULT = {
        -1: 'Opposite',
        0: 'Perpendicular',
        1: 'Identical'
    }

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
    def length(self):
        return sqrt(self.x**2 + self.y**2 + self.z**2)

    # normalize Vector to unit length 1
    def normalized(self):
        magnitude = self.length()
        self.x /= magnitude
        self.y /= magnitude
        self.z /= magnitude
        return self

    # return angle between two Vectors
    def angle(self, other):
        return cos((Vector.dot_product(self, other) / self.length()+other.length()))

    # ---------------Static-Methods----------------
    # Negates all Vector's components
    @staticmethod
    def opposite_vector(v):
        return Vector(-v.x, -v.y, -v.z)

    @staticmethod
    def dot_product(a, b):
        return (a.x*b.x) + (a.y*b.y) + (a.z*b.z)

    # ---------------Class-Methods----------------
    #     shortcut for creating common Vectors
    @classmethod
    def null_vector(cls):
        return cls(0, 0, 0)

    @classmethod
    def infinity_vector(cls):
        return cls(Vector.__INF, Vector.__INF, Vector.__INF)

    @classmethod
    def up_vector(cls):
        return cls(0, 1, 0)

    @classmethod
    def down_vector(cls):
        return cls(0, -1, 0)

    @classmethod
    def right_vector(cls):
        return cls(1, 0, 0)

    @classmethod
    def left_vector(cls):
        return cls(-1, 0, 0)

    @classmethod
    def forward_vector(cls):
        return cls(0, 0, 1)

    @classmethod
    def back_vector(cls):
        return cls(0, 0, -1)

    # ---------------Set/Get-Methods----------------
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        try:
            if value is Vector.__INF:
                self.__x = Vector.__INF

            else:
                value = int(value)
                self.__x = value

        except ValueError:
            raise ValueError("Zadejte pouze ciselne znaky")

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        try:
            if value is Vector.__INF:
                self.__y = Vector.__INF

            else:
                value = int(value)
                self.__y = value

        except ValueError:
            raise ValueError("Zadejte pouze ciselne znaky")

    @property
    def z(self):
        return self.__z

    @z.setter
    def z(self, value):
        try:
            if value is Vector.__INF:
                self.__z = Vector.__INF

            else:
                value = int(value)
                self.__z = value

        except ValueError:
            raise ValueError("Zadejte pouze ciselne znaky")


class Rectangle(Vector):
    def __init__(self, x, y, z, w):
        super().__init__(x, y, z)
        self.w = w
        # obdelnik XYZW

    def area(self):
        xy = Vector(self.x, self.y, 0).length()
        yz = Vector(self.z, self.w, 0).length()

        # S = a * b
        S = (xy * yz)
        print("Area S = ", round(S, 2), "cm.")

    @property
    def w(self):
        return self.__w

    @w.setter
    def w(self, value):
        try:
            value = int(value)
            self.__w = value

        except ValueError:
            raise ValueError("Zadejte pouze ciselne znaky")


# ------------------------------------------------------------------------------------------------------------------
#                                                 praktická část
# ------------------------------------------------------------------------------------------------------------------
v1 = Vector(5, 6, 9)
print(v1)
print(type(v1))
print("Is v1 an instance of vector? ", isinstance(v1, Vector))

right = Vector.right_vector()
up = Vector.up_vector()

print(f'\nRight: {right} and up: {up}\n'
      f'Dot product of {right} and {up} is: {Vector.DOT_PRODUCT_RESULT[Vector.dot_product(right, up)]}\n'
      f'Normalized {v1} = {v1.normalized()} of length: {v1.length()}')

v2 = Vector(4, 2, 5)
v3 = Vector(1, 2, 7)
v4 = v3
print(f'\nOperators:\n'
      f'(v3**2 == v4 * v3) is {v3**2 == v4*v3}\n'
      f'v2 + v4 = {v2 + v4}\n'
      f'v2 - v4 = {v2 - v4}\n')

inf_vector = Vector.infinity_vector()
print(inf_vector, "with infinity values")

v2_opposite = Vector.opposite_vector(v2)
print("Opposite vector to", v2, " is:", v2_opposite)


a = Vector(1, 2, 0)
b = Vector(2, 4, 0)

r = Rectangle(a.x, a.y, b.x, b.y)
r.area()
