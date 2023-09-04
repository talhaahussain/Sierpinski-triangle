import turtle
import random 

t = turtle.Turtle()
t.width(5)
t.shape("circle")
t.penup()
t.speed(0)

vertices = [(0, 250), (-216.506, -125), (216.506, -125)]

def generateTriangle(t, vertices):
    for v in vertices:
        t.goto(v)
        t.dot()
        t.penup()
    return

def choosePoint(vertices):
    x = random.uniform(vertices[1][0], vertices[2][0])
    y = random.uniform(vertices[0][1], vertices[2][1])
    p = (x, y)

generateTriangle(t, vertices)
