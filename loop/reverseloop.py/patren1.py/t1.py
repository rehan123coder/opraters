import turtle
turtle.Screen().bgcolor("red")
turtle.Screen(). setup(200,300)
polygon=turtle.Turtle()
num_sides=8
side_length=80
angle = 360/num_sides
for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)
turtle.done()