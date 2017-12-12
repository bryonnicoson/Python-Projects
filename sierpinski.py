import turtle
import math

def draw_triangle(x,y,base_len):

    if(base_len <= 6.25):
        return
    
    # move to origin pt (base left vertice)
    t.up()
    t.goto(x,y)
    t.down()
    # draw an equilateral triangle
    for i in range(3):
        t.forward(base_len)
        t.left(120)
    # draw three equilateral triangles with base 1/2 parent base
    draw_triangle(x,y,base_len/2)
    draw_triangle(x+(base_len/2),y,base_len/2)
    draw_triangle(x+(base_len/4),y+((math.sqrt(3)/4)*base_len),base_len/2)
       
t = turtle.Turtle()

draw_triangle(-200,-200,400)




