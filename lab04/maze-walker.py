import maze
import turtle

num = int(input('Choose what maze you want to play, 1-5: '))

#Creating the objects
m = maze.Maze(num)
t = turtle.Turtle()

#Starting point for the maze as a tuple
x,y = m.entry()
entry_pos = (x,y)

#Setting up shape and size for the turtle
t.shape('turtle')
t.color('green')
t.shapesize(0.5)

#Placing and setting up turlte at entry point
t.penup()
t.goto(entry_pos)
t.pendown()
t.left(90)


print('Pos of turtle ', t.pos())
print('Pos of entry ', m.entry())

#Depending on the map the turtles speed will increse
if num == 5 or num == 4:
    turtle.Screen().delay(1)
    turtle.Screen().tracer(2)

    

while m.at_exit(t.pos()) == False:
    if m.wall_at_left(t.heading(), t.pos()) == True:
        t.forward(1)
        if m.wall_in_front(t.heading(), t.pos()) == True:
            t.right(90)
            t.forward(1)
    else:
        t.left(90)
        t.forward(1)



print('You have reached the end of the maze, at tuple ', t.pos())

turtle.mainloop()


