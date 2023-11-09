import turtle as t
from math import sqrt

def dragon(length, n, start):
    """
        Trace the dragon's curve with turtle
        Recursive function
        One should not call this function without doing a mainloop afterwards
    Args:
        length (int): Lenght of the structure
        n (int): Number of step to trace
        start (bool): To know if we should draw the figure on the left (False) or on the right (True)
    """
    #Shutdown condition
    if n == 0:
        #Trace one in two, the primary form in one direction or the other (the perpendicular bases of a right triangle)
        if start:
            t.right(45)
            t.forward(length)
            t.left(90)
            t.forward(length)
            t.right(45)
        else:
            t.left(45)
            t.forward(length)
            t.right(90)
            t.forward(length)
            t.left(45)
    #Recursion
    else:
        #Trace the last step's figure with smallest length (To the right)
        dragon(length/sqrt(2), n-1, True)
        #To trace the good figure's version (right or left)
        if start:
            t.left(90)
        else:
            t.right(90)
        #Trace the last step's figure with smallest length (To the left)
        dragon(length/sqrt(2), n-1, False)


def dragonTrace(length, n):
    """
        To trace the dragon's curve in a windows
    Args:
        length (int): Lenght of the structure
        n (int): Number of step to trace
    """
    t.tracer(0,0)
    t.penup()
    t.goto(-length//2, length//3)
    t.pendown()
    #Trace dragon's curve
    dragon(length, n, True)
    #Finish the trace and open the window
    t.update()
    t.mainloop()