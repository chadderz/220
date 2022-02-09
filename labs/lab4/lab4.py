"""
Name: <Margaux Walz>
lab4.py

Problem: This program uses graphics to create a greeting card

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import graphics, time
from graphics import GraphWin, Circle, Polygon, Rectangle, Point, Text


def greeting_card():
    window = GraphWin("Greeting Card", 700, 700)
    window.setBackground('black')
    l_circle = Circle(Point(440, 300), 70)
    l_circle.setFill('red')
    l_circle.setOutline('red')
    r_circle = Circle(Point(300, 300), 70)
    r_circle.setFill('red')
    r_circle.setOutline('red')
    l_circle.draw(window)
    r_circle.draw(window)
    what = Polygon(Point(510, 320), Point(440, 300), Point(230, 320), Point(370, 500))
    what.setFill('red')
    what.setOutline('red')
    what.draw(window)
    label = Text(Point(350, 600), "Happy Valentines Day")
    label.setFace('courier')
    label.setTextColor('red')
    label.draw(window)
    stick = Rectangle(Point(20, 300), Point(80, 304))
    head = Polygon(Point(70, 290), Point(90, 302), Point(70, 314))
    head.setFill('white')
    head.setOutline('white')
    head.draw(window)
    stick.setFill('white')
    stick.setOutline('white')
    stick.draw(window)
    for i in range(70):
        head.undraw()
        stick.undraw()
        head.move(10, 0)
        stick.move(10, 0)
        head.draw(window)
        stick.draw(window)
        time.sleep(.1)
    clickclose = Text(Point(350, 650), "Click anywhere to close")
    clickclose.setTextColor('white')
    clickclose.draw(window)
    window.getMouse()
    window.close()
