# Import the CMU Graphics package:
from cmu_graphics import *

def penguin(x,color):
    Oval(x,250,200,300,fill=color)
    Oval(x-70,250,100,150,fill=color)
    Oval(x+75,250,100,150,fill=color)

    Label('- -',x,160,size=100,fill='darkGrey')
    Polygon(x-20,160,x+20,160,x,180,fill='salmon')
    Oval(x,260,100,150,fill='white')


    Oval(x-40,390,60,60, fill='gold')
    Oval(x+50,390,60,60, fill='gold')

penguin(200,'lightBlue')
penguin(300,'purple')
penguin(100,'lightGreen')

#When you comment out a function call nothing will happen,
#this is because when you do this you are turning the function call
#into a comment, these comments won't appear in display and will
#stay in your code to orginize your code.

# Run program:
cmu_graphics.run()

