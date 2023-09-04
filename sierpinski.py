import turtle
import random 

t = turtle.Turtle()
t.width(5)
t.shape("circle")
t.penup()

vertices = [(0, 250), (-216.506, -125), (216.506, -125)]

def generateTriangle(t, vertices):
    for v in vertices:
        t.goto(v)
        t.dot()
        t.penup()
    return


generateTriangle(t, vertices)    
