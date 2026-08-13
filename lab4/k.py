import turtle

pen = turtle.Turtle()
pen.speed(2)

colors = ['red', 'purple', 'blue', 'orange', 'yellow', 'pink']

for i in range(36):
    pen.color(colors[i % len(colors)])
    pen.circle(100, 60)   # draw a petal-like arc
    pen.left(360 / 36)    # rotate a bit before drawing the next one

pen.hideturtle()
turtle.done()