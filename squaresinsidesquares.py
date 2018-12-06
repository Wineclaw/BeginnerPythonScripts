import turtle

def make_wn(wncolor, wntitle):
     """
     Sets up the turtle's window; color and title
     """
     w = turtle.Screen()
     w.bgcolor(wncolor)
     w.title(wntitle)
     return w

def make_turt(turtcolor, turtsz, turtsp):
     """
     Sets up the turtle; color, pen-size, and speed
     """
     t = turtle.Turtle()
     t.color(turtcolor)
     t.pensize(turtsz)
     t.speed(turtsp)
     return t
# major turtle definitions -- don't touch
###
     

wn = make_wn("lightgreen", "Turtles love refractoring!")
jon = make_turt("blue", 3, 5)
# calls functions: creates windows and one turtle
#########

total_squares = 1
# initial number of squares, must be set to 1

for i in range (5): # repeats the entire code until 5 squares are made
     for i_2 in range(4):
          jon.forward(20 * total_squares)
          jon.left(90)
# initial square

     total_squares = 1 + total_squares
# tracks number of squares made

     jon.right(135)
     jon.penup()
     jon.forward(15)
     jon.left(135)
     jon.pendown()
# sets up for new square



#########
wn.mainloop() # keeps window open
turtle.done() # prevents crash on work PC