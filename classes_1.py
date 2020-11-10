# classes for animals and shapes, abstraction, encapsulation, public private access specifiers


class Animal(object):
    species = ' '                       # public access modifier

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._habitat = ' '             # protected access modifier (can be accessed in subclasses)
        self.__kingdom = 'Animalia'     # private access modifier (cannot be accessed outside class)

    def description(self):
        print('My name is {} and my age is {}!'.format(self.name, self.age))
        if self.species == 'insect':
            print('I am an invertebrate')
        else:
            if self.species == 'mammal' or self.species == 'bird':
                print('I am a vertebrate and warm-blooded')
            else:
                print('I am a vertebrate and cold-blooded')

    def move(self):
        print('Animals can move')

    def eat(self):
        print('Eating...')

    def sleep(self):
        print('Sleeping...')


# subclass of base class Animal
class Dog(Animal):
    species = 'mammal'

    def __init__(self, name, age):
        super().__init__(name, age)
        self._habitat = 'Land'          # accessing protected attribute from base class

    def move(self):
        print('Walking...')

    def sound(self):
        print('Barking!')


class Lion(Animal):
    species = 'mammal'

    def __init__(self, name, age):
        super().__init__(name, age)

    def move(self):
        print('Chasing a deer...')

    def sound(self):
        print('Roaring!')


class Fish(Animal):
    species = 'fish'

    def __init__(self, name, age):
        super().__init__(name, age)

    def move(self):
        print('Swimming...')

    def sound(self):
        print('Bloop Bloop!')


class Crow(Animal):
    species = 'bird'

    def __init__(self, name, age):
        super().__init__(name, age)

    def move(self):
        print('Flying...')

    def sound(self):
        print('Caw!')


class Frog(Animal):
    species = 'amphibian'

    def __init__(self, name, age):
        super().__init__(name, age)

    def move(self):
        print('Jumping...')

    def sound(self):
        print('Croaking!')


class Snake(Animal):
    species = 'reptile'

    def __init__(self, name, age):
        super().__init__(name, age)

    def move(self):
        print('Gliding...')

    def sound(self):
        print('Hisssss!')


class Bee(Animal):
    species = 'insect'

    def __init__(self, name, age):
        super().__init__(name, age)

    def move(self):
        print('Flying...')

    def sound(self):
        print('Humming!')


class Cow(Animal):
    species = 'mammal'

    def __init__(self, name, age):
        super().__init__(name, age)

    def move(self):
        print('Walking slowly...')

    def sound(self):
        print('Moo!')


class Mouse(Animal):
    species = 'rodent'

    def __init__(self, name, age):
        super().__init__(name, age)

    def move(self):
        print('Running...')

    def sound(self):
        print('Squeaking!')


class Ostrich(Animal):
    species = 'bird'

    def __init__(self, name, age):
        super().__init__(name, age)

    def move(self):
        print('Sprinting...')

    def sound(self):
        print('Whistling!')


dog1 = Dog('Mike', 3)
dog1.description()
print(dog1._habitat)
print(dog1._Animal__kingdom)                # Name Mangling

snake = Snake('Naagin', '5 years')
snake.sleep()
snake.sound()

frog1 = Frog('Toady', '2 months')
print(frog1.species)

crow1 = Crow('Blackie', '5 months')
print(crow1.name)
print(crow1.age)

insect1 = Bee('Hummer', '1 month')
insect1.description()
insect1.move()

fish1 = Fish('Goldie', '2 months')
fish1.eat()
fish1.description()

mouse = Mouse('Mickey', '1 month')
print(mouse.species)

# Shapes

import math


class Shapes(object):
    # Constructor
    def __init__(self):
        print('Shape has been created!')

    # Destructor
    def __del__(self):
        print('The shape has been destructed!')


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


class Triangle(Shapes):
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


class Equilateral(Shapes):
    def __init__(self, side):
        super().__init__()
        self.n = 3
        self.a = side

    def getPerimeter(self) :
        return 3*self.a

    def getArea(self):
        return round((3**0.5)*(self.a ** 2)/4, 2)


class Rectangle(Shapes):
    def __init__(self, length, breadth):
        super().__init__()
        self.n = 4
        self.length = length
        self.breadth = breadth

    def getArea(self):
        return self.length * self.breadth

    def getPerimeter(self):
        return 2*(self.length + self.breadth)


class Rhombus(Shapes):
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


# derived from the subclass Rhombus
class Square(Rhombus):

    def getArea(self):
        return self.length * self.length

    def getPerimeter(self):
        return 4*self.length

    def angle(self):
        print("Angle between sides in degrees : ")
        total = 180 * (self.n - 2)
        return total / self.n


class Pentagon(Shapes):
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


class Hexagon(Shapes):
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


class Parallelogram(Shapes):
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


cir = Circle(10)
print(cir.getCircumference())

tri = Triangle(2, 3, 4)
print(tri.getArea())

rect = Rectangle(3, 4)
print(rect.getPerimeter())

rm = Rhombus(5)
print(rm.getAngle(5))
print(rm.getArea())

sq = Square(5)
print(sq.getArea())
print(sq.angle())

pn = Pentagon(3)
print(pn.getArea())