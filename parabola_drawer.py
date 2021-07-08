# This program is used to drawing a parabola.After drawing,it will save the window into the directory 'pictures' and the
# suffix will be '.aps',which can be open with only 'photoshop'(at least among the most known apps).

from turtle import *
import math as m
import time as t
from tkinter.messagebox import *
from tkinter import *

g = 9.8     # the acceleration of gravity(m/s^2)
f = 8       # the frequency of analog refreshing (Hz) (f=frequency)
s = Screen()
__ParaVersion = "2.5.0"
__ParaAuthor = "chunk,Allen.Liu"
__ParaCopyright = "CN©2021 by Allen.Liu"

class Item(Turtle):
    def __init__(self, direction, initial_speed, hide=True):
        super().__init__()      # to make initialization of the super class stay
        self.speed(1)
        self.d = direction
        self.x_speed = initial_speed*m.sin(m.radians(self.d))
        self.y_speed = m.sqrt(initial_speed ** 2 - self.x_speed ** 2)
        self.shape('circle')
        try:
            if hide:
                self.ht()
        except TypeError:
            raise TypeError("parameter 'hide' must be a boolean value")

    def throw(self):
        slt = 1/f    #(slt=sleep time)
        _g = g/f
        while True:
            x = self.xcor()
            y = self.ycor()
            if y < 0:
                break
            self.y_speed -= _g
            self.goto(x+self.x_speed, y+self.y_speed)
            t.sleep(slt)

def setting(name, value):
    """
    :param name: used to describe which variable you want to set
    :param value: used to describe what value you want to change the variable into
    :return: None
    """
    global g, f
    if name == "g":
        g = value
    elif name == "f":
        f = value

def get_version():
    return __ParaVersion

def get_author():
    return __ParaAuthor

def get_copyright():
    return __ParaCopyright

def _main():
    global _title
    # setting("f", 32) #
    s.title("Getting the ground ready for drawing")
    # draw the ground
    gd = Turtle()
    gd.ht()
    gd.speed(0)
    gd.goto(0, 0)
    gd.goto(1000, 0)
    gd.goto(-1000, 0)
    gd.goto(0, 0)
    gd.dot(5, "Red")
    s.title("Asking for parameters.")

    # asking for direction
    try:
        d = float(numinput(title="parameter:elevation",
                           prompt="Please enter the  you want the ball be:(°)",
                           default=45,
                           minval=-89.9,
                           maxval=89.9))
        if d > 0:
            d = 90 - d
        elif d == 0:
            d += 90
        else:
            d = 89.999

        # asking for speed
        v = float(numinput(title="parameter:speed",
                           prompt="Please enter the speed you want the ball be:(m/s)",
                           default=10,
                           maxval=100))
    except TypeError:
        showerror(title="ERROR",
                  message="You cannot click the button 'cancel' because that may cause a bit of system error.")
        exit(1)
    else:
        _title = __file__+"?d="+str(d)+"&v="+str(v)
        s.title(_title)
        ball = Item(d, v)
        ball.throw()
        # tell users the drawing was end
        showinfo(title="end",
                 message='That is all for drawing.\nClick "OK"to draw again.'
                         'window.')
        i = textinput(title="",
                      prompt="do you want to draw another?")
        if str(type(i)) == "<class 'NoneType'>":
            open("number.txt", "r+").write(str(int(open("number.txt", "r").read())+1))
            eps_name = "pictures/show(No."+open("number.txt", "r+").read()+").eps"
            s.title(_title+"/"+eps_name)
            s.getcanvas().postscript(file=eps_name)
            mainloop()
        else:
            _main()

if __name__ == '__main__':
    _main()
