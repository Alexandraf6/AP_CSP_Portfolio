# Import the CMU Graphics package:
from cmu_graphics import *


def onMousePress(x,y):
    Rect(x-200,y-200,500,500)
    Circle(x-10,y-10,60,fill='grey')
    Label('| _ |', x-10,y-10,size=20)
    


def onMouseRelease(x,y):
    Rect(x-200,y-200,500,500, fill='lightBlue')
    Star(x-10,y-10,100,9,fill='lightSalmon')
    Circle(x-10,y-10,60,fill='lightYellow')
    Label('| - |', x-10,y-10,size=20)
    
# Run program:
cmu_graphics.run()

