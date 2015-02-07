import turtle

def draw_square(turtle):
    for i in range (1, 3):
        turtle.forward(100)
        turtle.right(90)
                

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape("arrow")
    brad.color("white")
    brad.speed(0)
    for i in range (1,37):
        draw_square(brad)
        brad.right(10)

    #angie = turtle.Turtle()
    #angie.shape("arrow")
    #angie.color("blue")
    #angie.circle(100)

    #frank = turtle.Turtle()
    #frank.shape("arrow")
    #frank.color("yellow")
    #frank.speed(0)

    #j = 0
    #while (j < 3):
    #    frank.forward(200)
    #    frank.right(120)
    #    j = j + 1
        
    window.exitonclick()

draw_shapes()
