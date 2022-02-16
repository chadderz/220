"""
Name: <Margaux Walz>
lab5.py

Problem: This program uses graphics to create shapes and print lists

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


from graphics import GraphWin, Point, Text, Circle, Entry, color_rgb, Line
from math import sqrt

def triangle():
    win = GraphWin("Triangle", 400, 400)
    num_clicks = 3
    shape = Point(200, 200)
    xy1 = win.getMouse()
    xy1.draw(win)
    xy2 = win.getMouse()
    xy2.draw(win)
    xy3 = win.getMouse()
    xy3.draw(win)
    line12 = Line(xy1, xy2)
    line23 = Line(xy2, xy3)
    line31 = Line(xy3, xy1)
    line12.draw(win)
    line23.draw(win)
    line31.draw(win)
    p1x = xy1.getX()
    p1y = xy1.getY()
    p2x = xy2.getX()
    p2y = xy2.getY()
    p3x = xy3.getX()
    p3y = xy3.getY()
    dx12 = p2x - p1x
    dy12 = p2y - p1y
    dx23 = p3x - p2x
    dy23 = p3y - p2y
    dx31 = p1x - p3x
    dy31 = p1y - p3y
    a = (dx12 ** 2) + (dy12 ** 2)
    a = sqrt(a)
    b = (dx23 ** 2) + (dy23 ** 2)
    b = sqrt(b)
    c = (dx31 ** 2) + (dy31 ** 2)
    c = sqrt(c)
    perimeter = a + b + c
    print(perimeter)
    perilabel = Text(Point(200, 300), perimeter)
    perilabel.draw(win)
    sp = perimeter / 2
    areaeq = sp * (sp - a) * (sp - b) * (sp - c)
    area1 = sqrt(areaeq)
    arealabel = Text(Point(200, 330), area1)
    arealabel.draw(win)
    win.getMouse()
    win.close()


def color_shape():

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")
    inputred = Entry(Point(200, 250), 3)
    inputred.draw(win)

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")
    inputgrn = Entry(Point(200, 270), 3)
    inputgrn.draw(win)

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")
    inputblu = Entry(Point(200, 290), 3)
    inputblu.draw(win)

    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    inputredentry = inputred.getText()
    inputredstr = eval(inputredentry)
    inputgrnentry = inputgrn.getText()
    inputgrnstr = eval(inputgrnentry)
    inputbluentry = inputblu.getText()
    inputblustr = eval(inputbluentry)

    shape.undraw()

    for i in range(6):
        win.getMouse()
        shape.setFill(color_rgb(inputredstr, inputgrnstr, inputblustr))
        shape.draw(win)

    # Wait for another click to exit
    win.close()


def process_string():
    string1 = input("Input a string: ")
    list1 = list(string1)
    firstletter = string1[0]
    print(len(string1))


    print(firstletter)





def process_list():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]





def another_series():
    list1 = [2, 4, 6]
    i = 0
    terms = eval(input("How many terms? "))
    for i in range(terms):
        print(list1[i % 3], end=' ')
    listp = list1[i % 3]
    listsum = sum(listp)
    print(listsum)




def target():
    win = GraphWin('Target', 500, 500)
    white = Circle(Point(250, 250), 250)
    white.setFill('white')
    black = Circle(Point(250, 250), 200)
    black.setFill('black')
    blue = Circle(Point(250, 250), 150)
    blue.setFill('cyan')
    red = Circle(Point(250, 250), 100)
    red.setFill('red')
    yellow = Circle(Point(250, 250), 50)
    yellow.setFill('yellow')
    white.draw(win)
    black.draw(win)
    blue.draw(win)
    red.draw(win)
    yellow.draw(win)
    clickclose = Text(Point(250, 300), "Click to close")
    clickclose.draw(win)
    win.getMouse()
    win.close()



