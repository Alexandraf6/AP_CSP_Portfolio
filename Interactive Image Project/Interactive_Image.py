# Import the CMU Graphics Package:
from cmu_graphics import *

# Grid
for i in range(16):  # 16 rows
    for j in range(16):  # 16 columns
        # Calculate the top-left corner of each cell
        x = j * 25
        y = i * 25
        # Draw the rectangle for each cell
        Rect(x, y, 25, 25, fill=None, border='grey', borderWidth=1)
        
#Background
sky=Rect(0,0,400,300, fill='lightSteelBlue')
Rect(0,300,400,300, fill='darkSeaGreen')
Label('SETTINGS:',200,15,font='monospace',bold=True)
Day= Rect(250,4,50,25,border='black',borderWidth=2,opacity=7)
Label('DAY',275,15, italic=True)
Night= Rect(325,4,50,25,border='black',borderWidth=2,opacity=7)
Label('NIGHT',350,15,italic=True)

def onMousePress(mouseX, mouseY):
    if Night.hits(mouseX, mouseY):
        sky.fill=rgb(105, 105, 138)
        
    elif Day.hits(mouseX, mouseY):
        sky.fill='lightSteelBlue'


def onMouseMove(mouseX,mouseY):
    if Sword.hits(mouseX, mouseY):
        HIT1.visible=True
        HIT2.visible=True
        HIT3.visible=True
        HIT4.visible=True
        HIT5.visible=True
        Label('GET CROWN',150,325,size=15,font='monospace',)

def onMouseRelease        
#Sword
Sword = Circle(325,300,45,border='black',borderWidth=2,opacity=7)
Line(350,275,325,300, lineWidth=5)
Line(325,275,350,300, lineWidth=4)
Polygon(330,280,345,295,320,320,300,320,fill='darkGrey')


#label
Label('CLICK', 325,360,size=15, font='monospace', bold=True)


#Bear Arms
Arm1=Rect(100,215,30,50, rotateAngle=45,fill='burlyWood')
Arm2=Rect(170,215,30,50, rotateAngle=-45,fill='burlyWood')

#BearEars
Circle(175,160,20, fill='burlyWood')
Circle(125,160,20,fill='burlyWood')
Circle(175,160,15, fill='wheat')
Circle(125,160,15,fill='wheat')

#Bear
Oval(150,185,80,70,fill='wheat')
Oval(150,250,90,100,fill='wheat')

#Bear Face
Label(' -   - ',150,180,size=35, italic=True )

#Bear Snout
Oval(150,195,45,30,fill='burlyWood')

#Bear nose
Oval(150,190,15,10)

#Bear Feet
Oval(175,275,35,50,fill='burlyWood')
Oval(125,275,35,50,fill='burlyWood')
Oval(175,275,25,40,fill='wheat')
Oval(125,275,25,40,fill='wheat')

#Crown
Rect(150,150,40,10, rotateAngle=25,fill=rgb(217, 174, 48))
Polygon(153,143,165,135,165,149,fill=rgb(217, 174, 48))
Polygon(165,149,177,141,177,155,fill=rgb(217, 174, 48))
Polygon(177,155,189,147,189,167,fill=rgb(217, 174, 48))
Circle(165,135,3,fill='lavender')
Circle(177,141,3,fill='lavender')
Circle(189,147,3,fill='lavender')


#Win Stars
HIT1=Star(50,175,15,5,fill='lemonChiffon', visible=False)
HIT2=Star(75,100,15,5,fill='lemonChiffon', visible=False)
HIT3=Star(150,75,15,5,fill='lemonChiffon', visible=False)        
HIT4=Star(225,100,15,5,fill='lemonChiffon', visible=False)
HIT5=Star(250,175,15,5,fill='lemonChiffon', visible=False)

    


# Run program:
cmu_graphics.run()

