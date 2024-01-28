import turtle
import random


t = turtle.Turtle()


# for i in range(1,101):
#     step = random.randint(1,2)
#     t.forward(10)
    
#     if(step == 1):
#         t.right(45)
#     else:
#         t.left(45)

def random_c_walk(turtle, steps, length, angle):
    
    for i in range(steps):
        
        x = random.randint(1,2)
        turtle.forward(length)

        if(x == 1):
            t.right(angle)
            t.pencolor("green")
        else:
            t.left(angle)
            t.pencolor("red")           
    return
    

random_c_walk(t, 100, 10, 45)

