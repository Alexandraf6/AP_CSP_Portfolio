# Import the CMU Graphics Package:
from cmu_graphics import *

#Ears
Circle(100,100,75,fill='cornSilk')
Circle(300,100,75,fill='cornSilk')

#inner ears
Oval(290,115,170,130,rotateAngle=130, fill=gradient(rgb(242, 235, 220),rgb(235, 226, 206)))
Oval(110,115,170,130,rotateAngle=50,fill=gradient(rgb(242, 235, 220),rgb(235, 226, 206)))

#Head
Circle(200,200,150, fill='cornSilk')



#nose

#eyes
Rect(100,100,10,10)

#hairs

#snout

#mouth

#stars



# Run program:
cmu_graphics.run()
