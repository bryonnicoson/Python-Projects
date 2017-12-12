import turtle
import math

def draw_triangle(x,y,base_len):
    t.up()
    t.goto(x,y)
    t.down()
    for i in range(3):
        t.forward(base_len)
        t.left(120)
        #push point at points array
        print(t.pos())
        vertices.append(t.pos())
        
def iterate(x,y,base_len):
    draw_triangle(x,y,base_len)
    base_len = base_len /2
    draw_triangle(x,y,base_len)

vertices = []   
t = turtle.Turtle()

iterate(-200,-200,400)
print(vertices)



