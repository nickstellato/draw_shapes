import turtle

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape("arrow")
    brad.color("white")
    brad.speed(6)

    i = 0
    while (i < 4):
        brad.forward(100)
        brad.right(90)
        i += 1

    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)

    frank = turtle.Turtle()
    frank.shape("arrow")
    frank.color("yellow")
    frank.speed(0)

    j = 0
    while (j < 3):
        frank.forward(200)
        frank.right(120)
        j = j + 1
        
    window.exitonclick()

draw_shapes()
