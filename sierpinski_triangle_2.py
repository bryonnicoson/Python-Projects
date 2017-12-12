import turtle
import math

def draw_triangle(x,y,base_len,order,color_delta):
    
    # stop when we reach max recursion depth (and avoid infinite loop)
    if(order == 0):
        return
    
    # move to origin pt (base left vertice)
    t.up()
    t.goto(x,y)
    t.down()
    
    # draw an equilateral triangle
    # if we're at max depth, fill the triangle
    if(order == 1):
        t.begin_fill()
    for i in range(3):
        t.forward(base_len)
        t.left(120)
    if(order == 1):
        t.end_fill()
        
    order = order - 1
        
    # draw three child triangles with base = 1/2 of parent base
    # if it's at the specified depth, change the color
    if(order == color_delta):
        t.color("orange")
    draw_triangle(x,y,base_len/2,order,color_delta)
    if(order == color_delta):
        t.color("green")
    draw_triangle(x+(base_len/2),y,base_len/2,order,color_delta)
    if(order == color_delta):
        t.color("yellow")
    draw_triangle(x+(base_len/4),y+((math.sqrt(3)/4)*base_len),base_len/2,order,color_delta)
    
window = turtle.Screen()
window.bgcolor("black")
t = turtle.Turtle()
t.color("white")
t.speed(0)
t.hideturtle()
draw_triangle(-200,-200,400,7,4)
