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
        

#Sword
Circle(325,300,45,border='black',borderWidth=2,opacity=5)
Line(350,275,325,300, lineWidth=5)
Line(325,275,350,300, lineWidth=4)
Polygon(330,280,345,295,320,320,300,320,fill='darkGrey')

#Bear Arms
Rect(100,215,30,50, rotateAngle=45,fill='burlyWood')
Rect(170,215,30,50, rotateAngle=-45,fill='burlyWood')

#BearEars
Circle(175,160,20, fill='burlyWood')
Circle(125,160,20,fill='burlyWood')
Circle(175,160,15, fill='wheat')
Circle(125,160,15,fill='wheat')


#Bear
Oval(150,185,80,70,fill='wheat')
Oval(150,250,90,100,fill='wheat')

#Bear Feet
Oval(175,275,35,50,fill='burlyWood')
Oval(125,275,35,50,fill='burlyWood')




# Run program:
cmu_graphics.run()
