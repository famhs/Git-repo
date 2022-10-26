import math
from xml.etree.ElementTree import PI
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def Area(self):
        pass

    @abstractmethod
    def Perimeter(self):
        pass

    @abstractmethod
    def Draw(self):
        pass


class Triangle(Shape):
    def __init__(self, Tside):
        self.Tside = Tside


class Equilateral(Triangle):
    def __init__(self, Tside):
        super().__init__(Tside)

    def Area(self):
        return (1/4) * math.sqrt(3) * self.Tside**2

    def Perimeter(self):
        return self.Tside * 3

    def Draw(self):
        return drawEqu(self.Tside)

class Isosceles(Triangle):
    def __init__(self, Tside, height):
        super().__init__(Tside)
        self.height = height

    def Area(self):
        return (1/2) * self.Tside * self.height

    def Perimeter(self):
        return math.sqrt(4 * self.height*2 + self.Tside*2) + self.Tside

    def Draw(self):
        return drawIso(self.height)


class Quadrilateral(Shape):
    def __init__(self, Qside):
        self.Qside = Qside


class Square(Quadrilateral):
    def __init__(self, Qside):
        super().__init__(Qside)

    def Area(self):
        return self.Qside ** 2

    def Perimeter(self):
        return self.Qside * 4

    def Draw(self):
        return drawRectangle(self.Qside, self.Qside)


class Rectangle(Quadrilateral):
    def __init__(self, Qside, length):
        super().__init__(Qside)
        self.length = length

    def Area(self):
        return self.Qside * self.length

    def Perimeter(self):
        return 2 * (self.Qside + self.length)

    def Draw(self):
        return drawRectangle(self.Qside, self.length)


class Pentagon(Shape):
    def __init__(self, Pside):
        self.Pside = Pside

    def Area(self):
        return (5/4) * self.Pside * math.tan(3*PI/10)

    def Perimeter(self):
        return self.Pside * 5

    def Draw(self):
        return drawPentagon(self.Pside)


class Hexagon(Shape):
    def __init__(self, Hside):
        self.Hside = Hside

    def Area(self):
        return (3/2) * math.sqrt(3) * self.Hside**2

    def Perimeter(self):
        return self.Hside * 6

    def Draw(self):
        return drawHexagon(self.Hside)


class Octagon(Shape):
    def __init__(self, Oside):
        self.Oside = Oside

    def Area(self):
        return 2 * self.Oside**2 * 1/(math.tan(PI/8))

    def Perimeter(self):
        return self.Oside * 8

    def Draw(self):
        return (drawOctagon(self.Oside))


def drawEqu(height):
    for i in range(height):
        print(" " * (height - i), end="")
        print("* " * (i + 1))


def drawIso(height):
    for i in range(height):
        print(" " * (height - i), end="")
        print("*" * (i * 2+ 1))


def drawHexagon(Hside):
    for i in range(Hside):
        print(' ' * (Hside - i - 1) + '* ' * (Hside + i))
    for i in range(Hside - 2, -1, -1):
        print(' ' * (Hside - i - 1) + '* ' * (Hside + i))


def drawOctagon(Oside):
    for i in range(Oside):
        print(' ' * (Oside - i - 1) + '* ' * (Oside + i))
    for i in range(Oside - 1):
        print('* ' * (Oside + (Oside - 1)))
    for i in range(Oside-1, -1, -1):
        print(' ' * (Oside - i - 1) + '* ' * (Oside + i))


def drawPentagon(Pside):
    for i in range(Pside):
        print(" " * (Pside - i), end="")
        print("* " * (i + 1))
    for i in range(Pside-1):
        print(" "+"* " * (Pside))


def drawRectangle(Qside, length):
    for i in range(length):
        print("* " * Qside)


def mainMenu():
    print("________________________")
    print("1. Triangle")
    print("2. Quadrilateral")
    print("3. Pentagon")
    print("4. Hexagon")
    print("5. Octagon")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    return choice


def polygonMenu():
    print("________________________")
    print("1. Area")
    print("2. Perimeter")
    print("3. Draw")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    return choice 

def triangleMenu():
    print("________________________")
    print("1. Equilateral")
    print("2. Isosceles")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    return choice   


def quadrilateralMenu():
    print("________________________")
    print("1. Square")
    print("2. Rectangle")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    return choice   

def main():
    while True:
        choice = mainMenu()
        if choice == 1:
            while True:
                choice = triangleMenu()
                if choice == 1:
                    while True:
                        choice = polygonMenu()
                        if choice == 1:
                            Tside = int(
                                input("Enter the side of the triangle: "))
                            equilateral = Equilateral(Tside)
                            print("(*) Area of the equilateral triangle is: ",
                                  equilateral.Area())
                        elif choice == 2:
                            Tside = int(
                                input("Enter the side of the triangle: "))
                            equilateral = Equilateral(Tside)
                            print("(*) Perimeter of the equilateral triangle is: ",
                                  equilateral.Perimeter())
                        elif choice == 3:
                            Tside = int(
                                input("Enter the side of the triangle: "))
                            equilateral = Equilateral(Tside)
                            print("Drawing the equilateral triangle: \n\n")
                            equilateral.Draw()
                        elif choice == 4:
                            break
                        else:
                            print("Invalid choice")
                elif choice == 2:
                    while True:
                        choice = polygonMenu()
                        if choice == 1:
                            Tside = int(
                                input("Enter the base of the triangle: "))
                            height = int(
                                input("Enter the height of the triangle: "))
                            isosceles = Isosceles(Tside, height)
                            print("(*) Area of the isosceles triangle is: ",
                                  isosceles.Area())
                        elif choice == 2:
                            Tside = int(
                                input("Enter the base of the triangle: "))
                            height = int(
                                input("Enter the height of the triangle: "))
                            isosceles = Isosceles(Tside, height)
                            print("(*) Perimeter of the isosceles triangle is: ",
                                  isosceles.Perimeter())
                        elif choice == 3:
                            Tside = int(
                                input("Enter the base of the triangle: "))
                            height = int(
                                input("Enter the height of the triangle: "))
                            isosceles = Isosceles(Tside, height)
                            print("Drawing the isosceles triangle: \n\n")
                            isosceles.Draw()
                        elif choice == 4:
                            break
                        else:
                            print("Invalid choice")
                elif choice == 3:
                    break
                else:
                    print("Invalid choice")
        elif choice == 2:
            while True:
                choice = quadrilateralMenu()
                if choice == 1:
                    while True:
                        choice = polygonMenu()
                        if choice == 1:
                            Qside = int(
                                input("Enter the side of the square: "))
                            square = Square(Qside)
                            print("(*) Area of the square is: ", square.Area())
                        elif choice == 2:
                            Qside = int(
                                input("Enter the side of the square: "))
                            square = Square(Qside)
                            print("(*) Perimeter of the square is: ",
                                  square.Perimeter())
                        elif choice == 3:
                            Qside = int(
                                input("Enter the side of the square: "))
                            square = Square(Qside)
                            print("Drawing the square: \n\n")
                            square.Draw()
                        elif choice == 4:
                            break
                        else:
                            print("Invalid choice")
                elif choice == 2:
                    while True:
                        choice = polygonMenu()
                        if choice == 1:
                            Qside = int(
                                input("Enter the width of the rectangle: "))
                            length = int(
                                input("Enter the length of the rectangle: "))
                            rectangle = Rectangle(Qside, length)
                            print("(*) Area of the rectangle is: ",
                                  rectangle.Area())
                        elif choice == 2:
                            Qside = int(
                                input("Enter the width of the rectangle: "))
                            length = int(
                                input("Enter the length of the rectangle: "))
                            rectangle = Rectangle(Qside, length)
                            print("(*) Perimeter of the rectangle is: ",
                                  rectangle.Perimeter())
                        elif choice == 3:
                            Qside = int(
                                input("Enter the width of the rectangle: "))
                            length = int(
                                input("Enter the length of the rectangle: "))
                            rectangle = Rectangle(Qside, length)
                            print("Drawing the rectangle: \n\n")
                            rectangle.Draw()
                        elif choice == 4:
                            break
                        else:
                            print("Invalid choice")
                elif choice == 3:
                    break
                else:
                    print("Invalid choice")
        elif choice == 3:
            while True:
                choice = polygonMenu()
                if choice == 1:
                    Pside = int(input("Enter the side of the pentagon: "))
                    pentagon = Pentagon(Pside)
                    print("(*) Area of the pentagon is: ", pentagon.Area())
                elif choice == 2:
                    Pside = int(input("Enter the side of the pentagon: "))
                    pentagon = Pentagon(Pside)
                    print("(*) Perimeter of the pentagon is: ",
                          pentagon.Perimeter())
                elif choice == 3:
                    Pside = int(input("Enter the side of the pentagon: "))
                    pentagon = Pentagon(Pside)
                    print("Drawing the pentagon: \n\n")
                    pentagon.Draw()
                elif choice == 4:
                    break
                else:
                    print("Invalid choice")
        elif choice == 4:
            while True:
                choice = polygonMenu()
                if choice == 1:
                    Hside = int(input("Enter the side of the hexagon: "))
                    hexagon = Hexagon(Hside)
                    print("(*) Area of the hexagon is: ", hexagon.Area())
                elif choice == 2:
                    Hside = int(input("Enter the side of the hexagon: "))
                    hexagon = Hexagon(Hside)
                    print("(*) Perimeter of the hexagon is: ",
                          hexagon.Perimeter())
                elif choice == 3:
                    Hside = int(input("Enter the side of the hexagon: "))
                    hexagon = Hexagon(Hside)
                    print("Drawing the hexagon: \n\n")
                    hexagon.Draw()
                elif choice == 4:
                    break
                else:
                    print("Invalid choice")
        elif choice == 5:
            while True:
                choice = polygonMenu()
                if choice == 1:
                    Oside = int(input("Enter the side of the octagon: "))
                    octagon = Octagon(Oside)
                    print("(*) Area of the octagon is: ", octagon.Area())
                elif choice == 2:
                    Oside = int(input("Enter the side of the octagon: "))
                    octagon = Octagon(Oside)
                    print("(*) Perimeter of the octagon is: ",
                          octagon.Perimeter())
                elif choice == 3:
                    Oside = int(input("Enter the side of the octagon: "))
                    octagon = Octagon(Oside)
                    print("Drawing the octagon: \n\n")
                    octagon.Draw()
                elif choice == 4:
                    break
                else:
                    print("Invalid choice")
        elif choice == 6:
            break
        else:
            print("Invalid choice")
main()
