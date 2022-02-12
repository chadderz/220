"""
Name: <Margaux Walz>
lab4.py

Problem: This program uses graphics to create a greeting card

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


from graphics import *


def squares():
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Clicks", width, height)

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to move square")
    instructions.draw(win)

    # builds a circle
    shape = Rectangle(Point(70, 70), Point(20, 20))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to move the circle
    for i in range(num_clicks):
        click = win.getMouse()
        center = shape.getCenter()  # center of circle

        # move amount is distance from center of circle to the
        # point where the user clicked
        change_x = click.getX() - center.getX()
        change_y = click.getY() - center.getY()
        cloned = shape.clone()
        cloned.draw(win)
        shape.move(change_x, change_y)

    clickclose = Text(Point(200, 200), "Click anywhere to close")
    clickclose.draw(win)
    win.getMouse()
    win.close()


def rectangle():
    win = GraphWin("Rectangle", 400, 400)
    instructions = Text(Point(200, 300), "click two opposite corner points to make a rectangle!")
    instructions.draw(win)
    y1 = 0
    x1 = 0
    y2 = 0
    x2 = 0
    num_clicks = 2
    for i in range(1, 3):
        click1 = win.getMouse()
        y1 = click1.getY()
        x1 = click1.getX()
        print(x1 + y1)

    rectanglepts = rectangle()


def circle():
    win = GraphWin("Rectangle", 400, 400)
    instructions = Text(Point(200, 300), "click twice to make a circle")
    instructions.draw(win)



def pi2():
    terms = eval(input("How many terms to sum?"))
    sum1 = 1
    frac = 0
    num = 4
    den = 1
    for i in range(0, terms+1):
        frac = 2 * (i % 2) - 1
        num *= -1
        sum1 = sum1 + frac
    sum1 = sum1 * 4

    print("pi approximation: " + sum1)


if __name__ == '__main__':
    pass
