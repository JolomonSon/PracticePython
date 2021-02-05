#First Challenge
import turtle
box = turtle.Turtle()
def grid():
    box.forward(100)
    box.right(90)
    box.forward(100)
    box.right(90)
    box.forward(100)
    box.right(90)
    box.forward(100)
gLoop = [grid() for x in range(4)]
#Second Challenge
def circle():
    box.circle(100)
    box.right(90)
    box.circle(100)
    box.circle(-100)
    box.right(90)
    box.circle(100)
    box.right(450)   
#circle()