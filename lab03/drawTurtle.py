import turtle

t1 = turtle.Turtle()
t2 = turtle.Turtle()
t2.penup()
t2.goto(-50,0)
t2.pendown()

for i in range(4):
    t1.forward(150)
    t1.left(90)
    t2.backward(150)
    t2.right(90)



turtle.mainloop()