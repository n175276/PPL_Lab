# classes for animals and shapes with virtual functions, abstract classes, interfaces, polymorphism, hierarchy

from abc import ABCMeta, abstractmethod


# Abstract Base Class
class Animal(metaclass=ABCMeta):
    species = 'Animal'

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__kingdom = 'Animalia'

    def description(self):
        print('My name is {} and my age is {}!'.format(self.name, self.age))
        if self.species == 'insect':
            print('I am an invertebrate')
        else:
            if self.species == 'mammal' or self.species == 'bird':
                print('I am a vertebrate and warm-blooded')
            else:
                print('I am a vertebrate and cold-blooded')

    # Virtual function
    @abstractmethod
    def move(self):
        print('Animals can move')

    # Pure virtual function or abstract method
    @abstractmethod
    def sound(self):
        pass


class Terrestrial(Animal):

    def habitat(self):
        print('I live on land!')


class Aquatic(Animal):

    def habitat(self):
        print('I live in water!')


class Aerial(Animal):

    def habitat(self):
        print('I spend most of the time in air!')


class Amphibian(Animal):

    def habitat(self):
        print('I live on land as well as water!')


# Interface
class Pets(Animal):
    def feature(self):
        print('I can be tamed')


# Subclasses
class Dog(Pets, Terrestrial):
    species = 'mammal'

    def __init__(self, name, age):
        super().__init__(name, age)
        self._habitat = 'Land'

    def move(self):
        print('Walking...')

    def sound(self):
        print('Barking!')


class Lion(Terrestrial):
    species = 'mammal'

    def __init__(self, name, age):
        super().__init__(name, age)

    def move(self):
        print('Chasing a deer...')

    def sound(self):
        print('Roaring!')


class Fish(Aquatic):
    species = 'fish'

    def __init__(self, name, age):
        super().__init__(name, age)

    def move(self):
        print('Swimming...')

    def sound(self):
        print('Bloop Bloop!')


class Crow(Aerial):
    species = 'bird'

    def __init__(self, name, age):
        super().__init__(name, age)

    def move(self):
        print('Flying...')

    def sound(self):
        print('Caw!')


class Frog(Amphibian):
    species = 'amphibian'

    def __init__(self, name, age):
        super().__init__(name, age)

    def move(self):
        print('Jumping...')

    def sound(self):
        print('Croaking!')


class Snake(Terrestrial):
    species = 'reptile'

    def __init__(self, name, age):
        super().__init__(name, age)

    def move(self):
        print('Gliding...')

    def sound(self):
        print('Hisssss!')


class Bee(Aerial):
    species = 'insect'

    def __init__(self, name, age):
        super().__init__(name, age)

    def move(self):
        print('Flying...')

    def sound(self):
        print('Humming!')


class Cow(Pets, Terrestrial):
    species = 'mammal'

    def __init__(self, name, age):
        super().__init__(name, age)

    def move(self):
        print('Walking slowly...')

    def sound(self):
        print('Moo!')


class Mouse(Terrestrial):
    species = 'rodent'

    def __init__(self, name, age):
        super().__init__(name, age)

    def move(self):
        print('Running...')

    def sound(self):
        print('Squeaking!')


class Ostrich(Terrestrial):
    species = 'bird'

    def __init__(self, name, age):
        super().__init__(name, age)

    def move(self):
        print('Sprinting...')

    def sound(self):
        print('Whistling!')


dog1 = Dog('Mike', 3)
dog1.description()
print(isinstance(dog1, Pets))
dog1.feature()

frog1 = Frog('Toady', '3 months')
print(issubclass(Frog, Aerial))
frog1.habitat()

# use of virtual function
fish1 = Fish('Goldie', '2 months')
fish1.move()

# use of abstract method
insect1 = Bee('Hummer', '1 month')
insect1.sound()

# Shapes

import math


# Abstract class
class Shapes(metaclass= ABCMeta):
    def __init__(self):
        print('Shape has been created!')

    @abstractmethod
    def getArea(self):
        pass


class Polygon:
    def type(self):
        print('I am a Polygon. I am 2-dimensional formed from straight lines.')


# Quadrilateral derived from polygon
class Quadrilateral(Polygon):
    def type(self):
        print("I am a Quadrilateral with 4 sides.")


class Ellipse(Shapes):
    def __init__(self, major_axis, minor_axis):
        super().__init__()
        self.a = major_axis
        self.b = minor_axis

    def getArea(self):
        return round(3.14 * self.a * self.b, 2)


class Circle(Shapes):
    def __init__(self, a):
        super().__init__()
        self.radius = a

    def getArea(self):
        return round(3.14 * self.radius * self.radius, 2)

    def getCircumference(self):
        return round(2 * 3.14 * self.radius, 2)


# Triangle class derived from Shapes and Polygon class
class Triangle(Shapes, Polygon):
    def __init__(self, side1, side2, side3):
        super().__init__()
        self.n = 3
        self.a = side1
        self.b = side2
        self.c = side3
        self.per = self.a + self.b + self.c

    def getPerimeter(self):
        return self.per

    def getArea(self):
        p = self.per /2
        return round((p*(p - self.a)*(p - self.b)*(p - self.c))**0.5, 2)


class Equilateral(Shapes, Polygon):
    def __init__(self, side):
        super().__init__()
        self.n = 3
        self.a = side

    def getPerimeter(self) :
        return 3*self.a

    def getArea(self):
        return round((3**0.5)*(self.a ** 2)/4, 2)


class Parallelogram(Shapes, Quadrilateral):
    def __init__(self, length, breadth):
        super().__init__()
        self.n = 4
        self.length = length
        self.breadth = breadth

    def getAngle(self, angle):
        self.angle = math.radians(angle)
        return round(self.angle, 2)

    def getPerimeter(self):
        return 2*(self.length + self.breadth)

    def getArea(self):
        return round(self.breadth * math.sin(self.angle) * self.length, 2)


# Rectangle class derived from Parallelogram
class Rectangle(Parallelogram):
    def __init__(self, length, breadth):
        super().__init__(length, breadth)

    def getArea(self):
        return self.length * self.breadth


class Rhombus(Shapes, Quadrilateral):
    def __init__(self, side):
        super().__init__()
        self.n = 4
        self.length = side

    def getAngle(self, angle):
        self.angle = math.radians(angle)
        return round(self.angle, 2)

    def getArea(self):
        return round(self.length * math.sin(self.angle) * self.length, 2)

    def getPerimeter(self):
        return 4*self.length


# Square class derived from Rhombus class
class Square(Rhombus):

    def getArea(self):
        return self.length * self.length

    def getPerimeter(self):
        return 4*self.length

    def angle(self):
        print("Angle between sides in degrees : ")
        total = 180 * (self.n - 2)
        return total / self.n


class Pentagon(Shapes, Polygon):
    def __init__(self, length):
        super().__init__()
        self.n = 5
        self.length = length

    def getArea(self):
        return round((((5 * (5 + 2*(5**0.5))) ** 0.5) * (self.length ** 2)) / 4, 2)

    def angle(self):
        print("Angle between sides in degrees : ")
        total = 180 * (self.n - 2)
        return total


class Hexagon(Shapes, Polygon):
    def __init__(self, length):
        super().__init__()
        self.n = 6
        self.length = length

    def getArea(self):
        return (3 * (3 ** 0.5) * (self.length ** 2)) / 2

    def angle(self):
        print("Angle between sides in degrees : ")
        total = 180 * (self.n - 2)
        return total


ell = Ellipse(4, 5)
print(ell.getArea())                # use of abstract methods

tri = Triangle(3, 7, 10)
tri.type()

rec = Rectangle(10, 20)
print(rec.getArea())
print(issubclass(Rectangle, Parallelogram))     # checking inheritance
print(isinstance(rec, Quadrilateral))

sq = Square(5)
sq.type()

