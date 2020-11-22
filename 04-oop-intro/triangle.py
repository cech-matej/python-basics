from math import sqrt
import operator


class Triangle:
    __size = 1
    __perimeter = None
    __area = None
    num_of_triangles = 0
    __id = None

    def __init__(self, a, b, c):
        a = round(abs(a), 2)
        b = round(abs(b), 2)
        c = round(abs(c), 2)

        if a + b > c and a + c > b and b + c > a:
            self.a = a
            self.b = b
            self.c = c
        else:
            self.a = 6
            self.b = 6
            self.c = 4

        self.__perimeter = self.a + self.b + self.c

        s = self.__perimeter/2
        self.__area = sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))

        Triangle.num_of_triangles += 1
        self.__id = Triangle.num_of_triangles

    def __str__(self):
        return f'a = {self.a}; b = {self.b}; c = {self.c}; O = {round(self.__perimeter, 2)}; S = {round(self.__area, 2)}'

    def __repr__(self):
        return f'{type(self).__name__}({self.a}, {self.b}, {self.c})'

    def __eq__(self, other):
        return self.__perimeter == other.__perimeter and self.__area == other.__area

    def __gt__(self, other):
        return self.__area > other.__area

    def __lt__(self, other):
        return self.__area < other.__area

    @staticmethod
    def operation(a1, a2, b1, b2, c1, c2, op):
        a = op(a1, a2)
        b = op(b1, b2)
        c = op(c1, c2)

        if a <= 0 or b <= 0 or c <= 0:
            raise Exception(f'The value of the triangle cannot be less than or equal to zero.\n'
                            f'The given values are: a = {a}; b = {b}; c = {c}')

        if a + b > c and a + c > b and b + c > a:
            return Triangle(a, b, c)
        else:
            raise Exception('Invalid triangle.')

    def __add__(self, other):
        return self.operation(self.a, other.a, self.b, other.b, self.c, other.c, operator.add)

    def __sub__(self, other):
        return self.operation(self.a, other.a, self.b, other.b, self.c, other.c, operator.sub)

    def __mul__(self, other):
        return self.operation(self.a, other.a, self.b, other.b, self.c, other.c, operator.mul)

    def __truediv__(self, other):
        return self.operation(self.a, other.a, self.b, other.b, self.c, other.c, operator.truediv)

    def __copy__(self):
        return Triangle(self.a, self.b, self.c)

    @property
    def perimeter(self):
        return self.__perimeter

    @property
    def size(self):
        return self.__size

    def times(self, multiple):
        self.__size = multiple
        self.a *= multiple
        self.b *= multiple
        self.c *= multiple
        self.__perimeter = self.a + self.b + self.c
        s = self.__perimeter / 2
        self.__area = sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    @classmethod
    def from_string(cls, triangle_str):
        a, b, c = triangle_str.split(', ')
        return cls(int(a), int(b), int(c))

    def info(self):
        print(f'{type(self).__name__} ABC, a = {self.a}; b = {self.b}; c = {self.c}')

    def order(self):
        print(f'{type(self).__name__} No. {self.__id}/{Triangle.num_of_triangles}')

    def calculate(self):
        print(f'Perimeter = {self.__perimeter}; Area = {self.__area}')


triangle1 = Triangle(8, 4, 6)
triangle2 = Triangle(-55, 5, 5)
triangle3 = triangle1.__copy__()
triangle4 = Triangle(1, 1, 1)

triangle5 = Triangle.from_string('10, 10, 10')

print(f'trinagle1.__str__()        {triangle1}')
print(f'trinagle1.__repr__()       {triangle1.__repr__()}')
print('-'.ljust(65, '-'))
print(f'trinagle2.__str__()        {triangle2}')
print(f'trinagle2.__repr__()       {triangle2.__repr__()}')
print('-'.ljust(65, '-'))
print(f'trinagle3.__str__()        {triangle3}')
print(f'trinagle3.__repr__()       {triangle3.__repr__()}')
print('-'.ljust(65, '-'))
print(f'Triangle made from string  {triangle5}\n')

print(f'triangle1 == triangle2     {triangle1 == triangle2}')
print(f'triangle1 == triangle3     {triangle1 == triangle3}')
print(f'triangle1 > triangle2      {triangle1 > triangle2}')
print(f'triangle1 < triangle2      {triangle1 < triangle2}\n')

print(f'triangle1 + triangle2      {triangle1 + triangle2}')
# print(f'triangle1 - triangle2      {triangle1 - triangle2}')  # The given values are: a = 2; b = -2; c = 2
print(f'triangle1 - triangle4      {triangle1 - triangle4}')
# print(f'triangle1 * triangle2      {triangle1 * triangle2}')  # Invalid triangle
print(f'triangle1 * triangle4      {triangle1 * triangle4}')
print(f'triangle1 / traingle2      {triangle1 / triangle2}\n')
# print(f'triangle1 / traingle2      {triangle2 / triangle1}')  # Invalid triangle

triangle1.info()
triangle1.order()
triangle1.calculate()

print(f'\ntriangle1 {triangle1} | size = {triangle1.size}')
triangle1.times(2)
print(f'triangle1 {triangle1} | size = {triangle1.size}')

