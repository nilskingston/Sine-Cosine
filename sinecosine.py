"""
sinecosine.py
Author: Nils Kingston
Credit: none

Assignment:

In this assignment you must use *list comprehensions* to generate sprites that show the behavior
of certain mathematical functions: sine and cosine. 

The sine and cosine functions are provided in the Python math library. These functions are used
to relate *angles* to *rectangular* (x,y) coordinate systems and can be very useful in computer
game design.

Unlike the last assignment using ggame`, this one will not provide any "skeleton" code to fill
in. You should use your submission for the Picture assignment 
(https://github.com/HHS-IntroProgramming/Picture) as a reference for starting this assignment. 

See:
https://github.com/HHS-IntroProgramming/Sine-Cosine/blob/master/README.md
for a detailed list of requirements for this assignment.

https://github.com/HHS-IntroProgramming/Standards-and-Syllabus/wiki/Displaying-Graphics
for general information on how to use ggame.

https://github.com/HHS-IntroProgramming/Standards-and-Syllabus/wiki/Programmed-Graphics
for general information on using list comprehensions to generate graphics.

http://brythonserver.github.io/ggame/
for detailed information on ggame.
"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset
from math import sin, cos, radians

red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
purple = Color(0xA020F0, 1.0)

thinline = LineStyle(1, black)
mycircle = CircleAsset(5, thinline, blue)
xcoordinates = range(0, 360, 10)
sprites = [Sprite(mycircle, (x, 100+100*sin(radians(x)))) for x in xcoordinates]

mycircle2 = CircleAsset(5, thinline, red)
sprites2 = [Sprite(mycircle2, (x, 100+100*cos(radians(x)))) for x in xcoordinates]

mycircle3 = CircleAsset(5, thinline, purple)
sprites3 = [Sprite(mycircle3, (100+100*cos(radians(x)), 400+100*sin(radians(x)))) for x in xcoordinates]




myapp = App()
myapp.run()
