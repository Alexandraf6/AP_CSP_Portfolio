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
clicker=Circle(200,325,5,opacity=40,visible=False)



def onMousePress(mouseX, mouseY):
    if Night.hits(mouseX, mouseY):
        sky.fill=rgb(105, 105, 138)
        
    elif Day.hits(mouseX, mouseY):
        sky.fill='lightSteelBlue'


def onMouseMove(mouseX,mouseY):
    if Sword.hits(mouseX, mouseY):
        HIT1=Star(50,175,15,5,fill='lemonChiffon', opacity=7)
        HIT2=Star(75,100,15,5,fill='lemonChiffon', opacity=7)
        HIT3=Star(150,75,15,5,fill='lemonChiffon', opacity=7)        
        HIT4=Star(225,100,15,5,fill='lemonChiffon',opacity=7)
        HIT5=Star(250,175,15,5,fill='lemonChiffon',opacity=7)
        Crown=Label('GET CROWN',150,325,size=15,font='monospace',opacity=7)
        clicker.visible=True



def onMouseRelease(mouseX,mouseY):
    if clicker.hits(mouseX,mouseY):
        Arm1.visible=False
        Arm2.visible=False
        Arm3.visible=False
        Arm4.visible=False
        AA1.visible=True
        AA2.visible=True
        AA3.visible=True
        AA4.visible=True
        C1.visible=False
        C2.visible=False
        C3.visible=False
        C4.visible=False
        C5.visible=False
        C6.visible=False
        C7.visible=False
        AC1.visible=True
        AC2.visible=True
        AC3.visible=True
        AC4.visible=True
        AC5.visible=True
        AC6.visible=True
        AC7.visible=True


    
#Sword
Sword = Circle(325,300,45,border='black',borderWidth=2,opacity=7)
Line(350,275,325,300, lineWidth=5)
Line(325,275,350,300, lineWidth=4)
Polygon(330,280,345,295,320,320,300,320,fill='darkGrey')


#label
Label('CLICK', 325,360,size=15, font='monospace', bold=True)


#Bear Arms
Arm3=Circle(195,255,13,fill='wheat',visible=True)
Arm4=Circle(105,255,13,fill='wheat',visible=True)
Arm1=Rect(100,215,30,50, rotateAngle=45,fill='burlyWood',visible=True)
Arm2=Rect(170,215,30,50, rotateAngle=-45,fill='burlyWood',visible=True)


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
C1=Rect(150,150,40,10, rotateAngle=25,fill=rgb(217, 174, 48),visible=True)
C2=Polygon(153,143,165,135,165,149,fill=rgb(217, 174, 48),visible=True)
C3=Polygon(165,149,177,141,177,155,fill=rgb(217, 174, 48),visible=True)
C4=Polygon(177,155,189,147,189,167,fill=rgb(217, 174, 48),visible=True)
C5=Circle(165,135,3,fill='lavender',visible=True)
C6=Circle(177,141,3,fill='lavender',visible=True)
C7=Circle(189,147,3,fill='lavender',visible=True)

#Alternative Arms
AA1=Oval(115,240,30,25,fill='burlyWood',rotateAngle=-25,visible=False)
AA2=Oval(185,240,30,25,fill='burlyWood',rotateAngle=25,visible=False)
AA3=Oval(115,240,25,20,fill='wheat',rotateAngle=-25,visible=False)
AA4=Oval(185,240,25,20,fill='wheat',rotateAngle=25,visible=False)

#Alternative Crown
AC1=Rect(125,230,48,10,fill=rgb(217, 174, 48),visible=False)
AC2=Polygon(126,230,133,220,141,230,fill=rgb(217, 174, 48),visible=False)
AC3=Polygon(141,230,148,220,156,230,fill=rgb(217, 174, 48),visible=False)
AC4=Polygon(156,230,163,220,171,230,fill=rgb(217, 174, 48),visible=False)
AC5=Circle(133,220,3,fill='lavender',visible=False)
AC6=Circle(148,220,3,fill='lavender',visible=False)
AC7=Circle(163,220,3,fill='lavender',visible=False)

#Flowers
def draw_flower(color):
    if color == 'pink':
        Line(50,250,50,300,fill='mediumSeaGreen',lineWidth=3)
        Circle(50,255,10,fill='pink')
        Circle(55,250,10,fill='pink')
        Circle(45,250,10,fill='pink')
        Circle(50,245,10,fill='pink')
        Circle(50,250,5,fill='lightYellow')

    elif color =='yellow':
        Line(50,250,50,300,fill='mediumSeaGreen',lineWidth=3)
        Circle(50,255,10,fill='yellow')
        Circle(55,250,10,fill='yellow')
        Circle(45,250,10,fill='yellow')
        Circle(50,245,10,fill='yellow')
        Circle(50,250,5,fill='brown')

# Change variable color to pink or yellow
#it'll change the flowers color

draw_flower('pink')
        
# Run program:
cmu_graphics.run()



