import turtle

def draw_Spiral(turtle, length):
    if length > 0:
        turtle.forward(length)
        turtle.right(90)
        draw_Spiral(turtle, length-5)


brad = turtle.Turtle()

window = turtle.Screen()

draw_Spiral(brad, 100)
window.exitonclick()
