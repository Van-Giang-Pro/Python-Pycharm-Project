import turtle
from random import randint

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def fall_in_retangle(self, rectangle):
        if rectangle.point1.x < self.x < rectangle.point2.x \
                and rectangle.point1.y < self.y < rectangle.point2.y:
            return True
        else:
            return False

class Rectangle:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
    def area(self):
        return (self.point1.x - self.point2.x) * \
               (self.point1.y - self.point2.y)

class GuiRectangle(Rectangle):
    def draw(self, canvas):
        canvas.penup()
        canvas.goto(self.point1.x, self.point1.y)
        canvas.pendown()
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)
        canvas.left(90)
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)

class GuiPoint(Point):
    def draw(self, canvas, size=5, color='green'):
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(size, color)

rectangle = GuiRectangle(Point(randint(0, 400), randint(0, 400)), Point(randint(10, 400), randint(10, 400)))
print("Rectangle Coordinates : ", rectangle.point1.x, ",", rectangle.point2.y, " And ", rectangle.point1.x, ",", rectangle.point2.y)
user_point = GuiPoint(float(input("Guess X: ")), float(input("Guess Y: ")))
print("Your Point Is Inside Rectangle :", user_point.fall_in_retangle(rectangle))
user_area = float(input("Guess Rectangle Area: "))
print("The Error Of Your Area : ", rectangle.area() - user_area)
myturtle = turtle.Turtle()
rectangle.draw(canvas=myturtle)
user_point.draw(canvas=myturtle)
turtle.done()
