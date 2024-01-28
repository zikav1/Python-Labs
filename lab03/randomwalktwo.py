import random
import turtle

turtle.Screen().delay(1)

#Setting up turtle
def create_turtle(turtle, x, y, c, s):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.color(c)
    turtle.shape(s)
    return

#A function for randomizing the step of the turtle
def random_step(turtle, step, angle):
    turtle.forward(step)
    turtle.right(angle)    
    return

t1 = turtle.Turtle()
t2 = turtle.Turtle()

create_turtle(t1,-50,-50,'green','turtle')
create_turtle(t2,50,50,'red','turtle')



while t1.distance(t2) > 100:
    
    random_step1 = random.randint(1,10)
    random_step2 = random.randint(1,10)
    random_angle1 = random.randint(-90,90)
    random_angle2 = random.randint(-90,90)
    
    random_step(t1, random_step1, random_angle1)
    random_step(t2, random_step2, random_angle2)
    
    

turtle.mainloop()
    



