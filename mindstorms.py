import turtle
import time

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("blue")
    draw_square()
    draw_circle()
    draw_triangle()
    time.sleep(20)
    turtle.clearscreen()
    window.bgcolor("navy")
    spirograph_square()
    window.exitonclick()

def draw_square():
    schwarber = turtle.Turtle()
    schwarber.shape("turtle")
    schwarber.color("white")
    schwarber.speed(2)

    for i in range(0,4):
        schwarber.forward(100)
        schwarber.right(90)
        i = i + 1
        
def draw_circle():
    bryant = turtle.Turtle()
    bryant.shape("arrow")
    bryant.color("red")
    bryant.circle(100)

def draw_triangle():
    rizzo = turtle.Turtle()
    rizzo.shape("triangle")
    rizzo.color("black")

    for i in range(0,3):
        rizzo.left(120)
        rizzo.forward(100)
        i = i + 1
    
def spirograph_square():
    arrieta = turtle.Turtle()
    arrieta.shape("circle")
    arrieta.color("white")

    for i in range(0,40):
        arrieta.left(9)
        
        for j in range(0,4):
            arrieta.forward(150)
            arrieta.right(90)

draw_shapes()

