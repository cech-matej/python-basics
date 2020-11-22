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
            self.__a = a
            self.__b = b
            self.__c = c
        else:
            self.__a = 6
            self.__b = 6
            self.__c = 4

        self.__perimeter = self.__a + self.__b + self.__c

        s = self.__perimeter/2
        self.__area = sqrt(s*(s-self.__a)*(s-self.__b)*(s-self.__c))

        Triangle.num_of_triangles += 1
        self.__id = Triangle.num_of_triangles

    def __str__(self):
        return f'a = {self.__a}; b = {self.__b}; c = {self.__c}; O = {round(self.__perimeter, 2)}; S = {round(self.__area, 2)}'

    def __repr__(self):
        return f'{type(self).__name__}({self.__a}, {self.__b}, {self.__c})'

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

        return Triangle.validity_check(a, b, c)

    def __add__(self, other):
        return self.operation(self.__a, other.__a, self.__b, other.__b, self.__c, other.__c, operator.add)

    def __sub__(self, other):
        return self.operation(self.__a, other.__a, self.__b, other.__b, self.__c, other.__c, operator.sub)

    def __mul__(self, other):
        return self.operation(self.__a, other.__a, self.__b, other.__b, self.__c, other.__c, operator.mul)

    def __truediv__(self, other):
        return self.operation(self.__a, other.__a, self.__b, other.__b, self.__c, other.__c, operator.truediv)

    def __copy__(self):
        return Triangle(self.__a, self.__b, self.__c)

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        try:
            value = int(value)
            self.__a = value

            self.info_set()
        except ValueError:
            raise ValueError('The given value is not a number.')

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, value):
        try:
            value = int(value)
            self.__b = value

            self.info_set()
        except ValueError:
            raise ValueError('The given value is not a number.')

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, value):
        try:
            value = int(value)
            self.__c = value

            self.info_set()
        except ValueError:
            raise ValueError('The given value is not a number.')

    @property
    def perimeter(self):
        return self.__perimeter

    @property
    def size(self):
        return self.__size

    def times(self, multiple):
        self.__size = multiple
        self.__a *= multiple
        self.__b *= multiple
        self.__c *= multiple
        self.__perimeter = self.__a + self.__b + self.__c
        s = self.__perimeter / 2
        self.__area = sqrt(s * (s - self.__a) * (s - self.__b) * (s - self.__c))

    @classmethod
    def from_string(cls, triangle_str):
        a, b, c = triangle_str.split(', ')
        return cls(int(a), int(b), int(c))

    def info(self):
        print(f'{type(self).__name__} ABC, a = {self.__a}; b = {self.__b}; c = {self.__c}')

    def order(self):
        print(f'{type(self).__name__} No. {self.__id}/{Triangle.num_of_triangles}')

    def calculate(self):
        print(f'Perimeter = {self.__perimeter}; Area = {self.__area}')

    def info_set(self):
        Triangle.validity_check(self.__a, self.__b, self.__c)
        self.__perimeter = self.__a + self.__b + self.__c
        s = self.__perimeter / 2
        self.__area = sqrt(s * (s - self.__a) * (s - self.__b) * (s - self.__c))

    @staticmethod
    def validity_check(a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            raise Exception(f'The value of the triangle cannot be less than or equal to zero.\n'
                            f'The given values are: a = {a}; b = {b}; c = {c}')
        if a + b > c and a + c > b and b + c > a:
            return Triangle(a, b, c)
        else:
            raise Exception('Invalid triangle.')


class EquilateralTriangle(Triangle):
    def __init__(self, a):
        super().__init__(a, a, a)
        self.__perimeter = 3 * a
        s = self.__perimeter / 2
        self.__area = sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def __str__(self):
        return f'a = b = c = {self.a}; O = {round(self.__perimeter, 2)}; S = {round(self.__area, 2)}'


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

# triangle1.a = 4  # Invalid triangle
triangle1.a = 6
triangle1.b = 7
print(f'\ntriangle1 {triangle1}\n')

eq_triangle1 = EquilateralTriangle(5)
eq_triangle2 = EquilateralTriangle(6)
print(f'eq_triangle1                 {eq_triangle1}')
print(f'eq_triangle2                 {eq_triangle2}')
print(f'eq_triangle1 + eq_triangle2  {eq_triangle1 + eq_triangle2}')


