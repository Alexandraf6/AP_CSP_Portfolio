# Import the CMU Graphics Package:
from cmu_graphics import *

# Paste this code above your project to draw the grid underneath your emoji
for i in range(16):  # 16 rows
    for j in range(16):  # 16 columns
        # Calculate the top-left corner of each cell
        x = j * 25
        y = i * 25
        # Draw the rectangle for each cell
        Rect(x, y, 25, 25, fill=None, border='grey', borderWidth=1)
        
#Ears
Circle(100,100,75,fill='cornSilk')
Circle(300,100,75,fill='cornSilk')

#inner ears
Oval(290,115,170,130,rotateAngle=130, fill=gradient(rgb(242, 235, 220),rgb(235, 226, 206)))
Oval(110,115,170,130,rotateAngle=50,fill=gradient(rgb(232, 211, 231),rgb(242, 235, 220),rgb(235, 226, 206)))

#Head
Circle(200,200,150, fill='cornSilk')



#nose

#eyes
Rect(100,175,65,20, fill=gradient('black','black','gray', start='top'))

#hairs

#snout

#mouth

#stars



# Run program:
cmu_graphics.run()

