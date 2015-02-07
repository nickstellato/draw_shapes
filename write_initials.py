import turtle

def write_n(turtle):
    turtle.left(90)
    turtle.forward(100)
    turtle.right(160)
    turtle.forward(100)
    turtle.left(160)
    turtle.forward(100)

def next_pos(turtle):
    turtle.penup()
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(100)
    turtle.left(90)

def write_s(turtle):
    turtle.pendown()
    turtle.forward(25)
    turtle.circle(25, 180)
    turtle.right(180)
    turtle.circle(25, -180)
    turtle.right(180)
    turtle.forward(20)

def write_initials(turtle):
    write_n(turtle)
    next_pos(turtle)
    write_s(turtle)

def draw_shape():
    window = turtle.Screen()
    window.bgcolor("white")

    brad=turtle.Turtle()
    brad.shape("arrow")
    brad.color("blue")
    brad.speed(0)
    write_initials(brad)

    window.exitonclick()

draw_shape()
