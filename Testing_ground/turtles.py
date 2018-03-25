import turtle

wm = turtle.Screen()
don = turtle.Turtle()
colors = ["yellow", "orange", "red", "purple", "blue", "green"]
sides = int(input("How many sides do you want?"))
length = int(input("How long do you want the sides?"))
angle = 360 / sides
for color in colors:
    don.color(color)
    don.left(60)
    for x in range(sides):
        don.forward(length)
        don.left(angle)

