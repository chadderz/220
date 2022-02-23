"""
Name: Margaux Walz
lab6.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import GraphWin, Text, Entry, Point, Rectangle


def vigenere():
    win = GraphWin("Vigenere", 500, 300)
    msg = Text(Point(80, 80), "Message to code")
    msg.draw(win)
    msginput = Entry(Point(300, 80), 30)
    msginput.draw(win)
    ntrkey = Text(Point(80, 130), "Enter Keyword")
    ntrkey.draw(win)
    keyinput = Entry(Point(230, 130), 15)
    keyinput.draw(win)
    msginputstr = msginput.getText()
    msginputstr = msginputstr.upper()
    keyinputstr = keyinput.getText()
    keyinputstr = keyinputstr.upper()
    buttonsq = Rectangle(230, 150)
    encodebutton = Text(Point(230, 150), "Encode")
    lentext = len(msginputstr)
    buttonsq.draw(win)
    encodebutton.draw(win)
    win.getMouse()
    buttonsq.undraw()
    encodebutton.undraw()
    ordinput = ord(keyinputstr)
    keylistnum = ord(keyinputstr)
    keylen = len(keyinputstr)
    ordinal = []
    textoutput = ""
    for i in range(lentext):
        val = (ordinput + keylistnum) % 26
        textoutput += chr(val + 65)
    outputwin = Text(Point(250, 250), textoutput)
    outputwin.draw(win)
    resulttext = Text(Point(250, 200), "Resulting Message")
    resulttext.draw(win)
    clickclose = Text(Point(250, 280), "Click to close")
    clickclose.draw(win)
    win.getMouse()
    win.close()


