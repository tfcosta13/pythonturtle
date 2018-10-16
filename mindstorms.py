import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    #Create the turtle Brad - Draws a square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("blue")
    brad.speed(2)
    for i in range(1,37):
        draw_square(brad)
        brad.right(10)
    #Create the turtle Angie - Draws a circle
    #angie = turtle.Turtle()
    #angie.shape("arrow")
    #angie.color("white")
    #angie.circle(100)

    window.exitonclick()

#draw_art()

def draw_form():
    window = turtle.Screen()
    window.bgcolor("black")
    #Create the turtle letter - Draw initials
    pen = turtle.Turtle()
    pen.color("white")

    for i in range(1,37):
        pen.forward(100)
        pen.right(120)
        pen.forward(100)
        pen.right(120)
        pen.forward(100)
        pen.right(120)
        pen.right(10)
        

    window.exitonclick()

draw_form()
    
