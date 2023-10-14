# 1 Implement PrintIndexMatrix function size nxm to print a matrix includes index of rows and index of coloumn as format Space bettween elements is a TAB
def PrintIndexMatrix(n, m):
    for i in range(n):
        print(f"{i}:", end='\t')
        for j in range(m):
            print(f"{j}", end='\t' if j < m - 1 else '\n')
            
# 2 Implement MultiplicationTable function promt value n, we generate n the multiplication tables
def MultiplicationTable(n):
    for i in range(1, n + 1):
        for j in range(1, 10):
            result = i * j
            print(f"{i} * {j} = {result:2}", end=' | ')
        print()

# 3 Given Matrix's size, implement MatrixXUD function to display a tile on the screen where the main diagonal is represented by X, the lower part by D and the upper part by U.
def MatrixXUD(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                print("X", end=" ")
            elif i > j:
                print("D", end=" ")
            else:
                print("U", end=" ")
        print()

# 4 MatrixQ04 Implement MatrixIndexs funtion to display pairs include row index, column column f. Each element in pair have width is 2.
def MatrixIndexs(m, n):
    for i in range(m):
        for j in range(n):
            # Format the row and column indices with a width of 2 and enclose in parentheses
            index_pair = f"({i:2}, {j:2})"
            print(index_pair, end=' ')
        print()

MatrixIndexs(3, 4)

# 5 Implement a MatrixZ function to display Z figure, known value n is size of square
def MatrixZ(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == n - i - 1:
                print("X", end=" ")
            else:
                print(" ", end=" ")
        print()

# 6 Declaring a class named Point, and two coordinate fields x, y, then defining function has prototype: __init__(self,x,y) is used to initial those coordinates
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# 7 Declaring a class named Point in 2D space, and two coordinate fields x, y, then defining three methods:
# DistanceOrigin method to calculate the distance of the point to origin 0,0
# Distance method to calculate the distance between two points
# Translate method to move the point to new coordinates in 2D space

import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def DistanceOrigin(self):
        return math.sqrt(self.x**2 + self.y**2)

    def Distance(self, other_point):
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)

    def Translate(self, dx, dy):
        self.x += dx
        self.y += dy

# 8 Declaring a class named Point in 2D space, then write override the built-in function __str__(self) -> str to return string as the following format for displaying point:
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({},{})".format(self.x,self.y)

 
# 9 Write a definition for a class named Circle with attributes center and radius, inherited from Point class
# where the center is a Point object in 2D space and the radius is a number
# Write a function named PointInCircle that takes a Circle and a Point and returns True if the
# point lies in or on the boundary of the circle.

import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

class Circle(Point):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def PointInCircle(self, point):
        distance = math.sqrt((point.x - self.x)**2 + (point.y - self.y)**2)
        return distance <= self.radius


# 10 eclare a Rectangle class inherit form Point class in 2D space. A rectangle is defined with its coordinates, width, and height. Implement the following functions:
# Define a function has prototype def __init__(self, p, w, h), know p is a point 2D, weight, and height to initial value for the rectangle
# Define a function named Corner return point object
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle(Point):
    def __init__(self, p, w, h):
        super().__init__(p.x, p.y)
        self.width = w
        self.height = h

    def Corner(self):
        return Point(self.x, self.y)

# 11 Hệ số tương quan
import numpy as np

# Tạo hai mảng dữ liệu mẫu
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 3, 4, 5, 6])

# Tính hệ số tương quan sử dụng hàm corrcoef
r = np.corrcoef(x, y)[0, 1]

print("Correlation Coefficient (r) =", r)






