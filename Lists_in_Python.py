from turtle import forward, backward, left, right, penup, pendown

length = 200
height = 100
def drawSquare(size=100):
    forward(size)
    left(90)
    forward(size)
    left(90)
    forward(size)
    left(90)
    forward(size)
    left(90)

def drawTriangle(size = 200):
    forward(size)
    left(120)
    forward(size)
    left(120)
    forward(size)



def drawHouse2(length):
    drawSquare(length)

    left(90)
    forward(length)
    right(90)

    drawTriangle(length)

    right(90)
    forward(length)
    left(90)



def drawRectangle(length, height):

    forward(length)
    left(90)
    forward(height)
    left(90)
    forward(length)
    left(90)
    forward(height)
    left(90)

#drawTriangle(100)
#drawRectangle(length, height)
drawHouse2(length)
input()