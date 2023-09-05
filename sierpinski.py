import turtle
import random 

t = turtle.Turtle()
#iters = turtle.Turtle()
t.width(0.1)
t.hideturtle()
#iters.hideturtle()
t.penup()
t.speed(0)
turtle.bgcolor("black")
t.pencolor("white")
#iters.pencolor("white")
count = 0
#iters.goto(0, 0)
#iters.pendown()
#iters.write("Iteration: " + str(count))
#iters.penup()

vertices = [(0, 350), (-303.109, -175), (303.109, -175)]

def generateTriangle(t, vertices):
    for v in vertices:
        t.goto(v)
        t.dot()
        t.penup()
    return

def inTriangle(p, v):
    a = ((v[1][1] - v[2][1])*(p[0] - v[2][0]) + (v[2][0] - v[1][0])*(p[1] - v[2][1])) / ((v[1][1] - v[2][1])*(v[0][0] - v[2][0]) + (v[2][0] - v[1][0])*(v[0][1] - v[2][1]))
    b = ((v[2][1] - v[0][1])*(p[0] - v[2][0]) + (v[0][0] - v[2][0])*(p[1] - v[2][1])) / ((v[1][1] - v[2][1])*(v[0][0] - v[2][0]) + (v[2][0] - v[1][0])*(v[0][1] - v[2][1]))
    c = 1 - a - b

    if (0 <= a <= 1) and (0 <= b <= 1) and (0 <= c <= 1):        
        return True
    else:
        return False

def choosePoint(vertices):
    while 1:
        x = random.uniform(vertices[1][0], vertices[2][0])
        y = random.uniform(vertices[0][1], vertices[2][1])
        p = (x, y)
        if (inTriangle(p, vertices)):
            break
        else:
            continue
    return p

def findMidpoint(p, a):
    x = (p[0] + a[0])/2
    y = (p[1] + a[1])/2
    m = (x, y)
    return m

generateTriangle(t, vertices)

p = choosePoint(vertices)
t.goto(p)
t.dot()
t.penup()

while True:
    a = random.choice(vertices)
    p = findMidpoint(p, a)
    t.goto(p)
    t.dot()
    t.penup()
    count += 1
    #iters.goto(300, 0)
    #iters.pendown()
    #iters.clear()
    #iters.write("Iteration: " + str(count))
    #iters.penup()
