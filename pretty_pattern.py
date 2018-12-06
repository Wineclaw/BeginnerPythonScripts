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
jon = make_turt("blue", 3, 8)
# calls functions, creates windows and one turtle
#########

def sq_draw(t, sz):
     """t is turtle, sz is side length"""
     for i in range(4):
          jon.forward(125)
          jon.left(90)

for i in range(20):
     sq_draw(jon, 125)
     jon.left(18)
# Creates a pretty pattern

#########
wn.mainloop() # keeps window open
turtle.done() # prevents crash on work PC