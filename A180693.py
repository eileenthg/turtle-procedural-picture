'''
Created on March 2022

@author: EILEEN TONG HUI GUAN
'''
import random                       # allows randomly generated patterns
import turtle                       # allows us to use the turtles library                                         
wn = turtle.Screen()                # creates a graphics window (canvas)
width = wn.window_width() - 4       # gets the window width and height
height =  wn.window_height() - 8
xAxis = width * 0.5                 # gets the axes, use for relative canvas positions
yAxis = height * 0.5                                

rainbowColor = ['red', 'orange', 'yellow', 'green', 'blue', 'violet', 'purple'] # set rainbow color pallette

'''
=== Variables ===
The following can be set manually in the python file.

defSpeed
- sets the default speed. 
- Accepted values are 1-11, where 1 ist the slowest and 11 the fastest.
- If set beyond that range,it defaults to 11.

defPenColor
- sets the default pen color.
- Accepts a (r,g,b) float tuple and hex notation string.
- Can also use common colour names.  

defBgColor
- sets the default background color
- Accepts a (r,g,b) float tuple and hex notation string.
- Can also use common colour names.
'''
defSpeed = 11
defPenColor = 'white'
defBgColor = 'black'

'''
=== Functions ===
'''
def initCursor(cursor):
    '''Initialises settings for the cursor. Can be manually edited in this python file.
    
    :param cursor: The turtle that which the default settings will be applied.
    :type cursor: Turtle.
    '''
    cursor.speed(defSpeed)
    cursor.color(defPenColor)
    turtle.bgcolor(defBgColor)

def cursorSetOrigin(cursor, x, y):
    cursor.penup()
    cursor.goto(x, y)
    cursor.pendown()
    return cursor.pos()

def pause(cursor, waitTime=3, x=0, y=0):
    '''Makes the cursor spin in place a bit, then clears the canvas.
    
    :param cursor: The turtle that will be running this function.
    :type cursor: Turtle.
    :param waitTime: The number of rotations the turtle will spin in place. Default 3.
    :type waitTime: int
    :param x: The x coordinate where the cursor will spin in place. Default 0.
    :type x: int
    :param y: The y coordinate where the cursor will spin in place. Default 0.
    :type y: int
    :raises: TypeError
    '''
    cursor.penup()                  # lifts the pen up
    cursor.setpos(x, y)             # moves pen to specified position
    cursor.speed(1)                 # slows the pen down so it can spin
    for i in range(waitTime):       # spins the pen
        cursor.circle(1)
    cursor.clear()                  # clear the canvas
    cursor.speed(defSpeed)          # reset pen attributes and returns it to home.
    cursor.home()
    cursor.pendown()
    

def mandala(cursor, rainbow=False, size=75, x=0, y=0):
    '''Draws a rudimentary mandala pattern.
    
    :param cursor: The turtle that will be running this function.
    :type cursor: Turtle.
    :param rainbow: If enabled, draws a rainbow coloured mandala. Default False.
    :type rainbow: Boolean.
    :param size: Sets the size of the mandala. Default 75.
    :type size: int
    :param x: The x coordinate for the pattern origin. Default 0.
    :type x: int
    :param y: The y coordinate for the pattern origin. Default 0.
    :type y: int
    :raises: TypeError
    '''
    cursorSetOrigin(cursor, x, y)                   # sets the starting point of the mandala
    for i in range (0, 2):
        for i in range(0, 7):
            if rainbow:
                cursor.color(rainbowColor[i])       # if rainbow enabled, draw in rainbow colors
            cursor.circle(size)
            cursor.left(25.714)
    cursor.color(defPenColor)                       # resets the pen color

def hydra(cursor, x=0, y=0):
    '''Draws a "tree" with a bunch of zig-zag lines as "leaves"
    
    :param cursor: The turtle that will be running this function.
    :type cursor: Turtle.
    :param x: The x coordinate for the pattern origin. Default 0.
    :type x: int
    :param y: The y coordinate for the pattern origin. Default 0.
    :type y: int
    :raises: TypeError
    '''
    origin = cursorSetOrigin(cursor, x, y)          # sets the starting point of the hydra
    cursor.color('brown', 'brown')                  # draws the triangle stem
    cursor.begin_fill()
    cursor.setheading(-80)
    while(cursor.pos()[1] > -round(yAxis*0.9)):
        cursor.forward(1)
    cursor.setheading(180)
    cursor.forward(2 * (cursor.pos()[0] - origin[0]))
    cursor.goto(origin)
    cursor.end_fill()
    
    defSize = cursor.pensize()    
    cursor.pensize(3)                              # thickens the line so it's easier to see the mandala
    cursor.color(defPenColor)                       # draws the 'leaves'
    for i in range(0, random.randint(3,10)):        # can have 3 to 10 leaves
        cursor.setheading(random.randint(0, 180))   # randomises the leaf direction
        leafLength = random.randint(20, 80)         # randomises the leaf length
        leafCurve = random.randint(10,90)           # randomises how sharp the leaves will bend
        for i in range(0, random.randint(1,5)):     # each leaf may bend 1 to 5 times
            cursor.left(leafCurve)
            cursor.forward(leafLength)
            cursor.right(leafCurve)
            cursor.forward(leafLength)
        cursor.penup()                              # resets the pen to origin to draw the next leaf
        cursor.setpos(origin)
        cursor.pendown()
    cursor.pensize(defSize)                         # resets the pen size

def stair(cursor, step, height, x=0, y=0):
    '''Draws an opaque staircase with a specified step size and height
    
    :param cursor: The turtle that will be running this function.
    :type cursor: Turtle
    :param step: The number of steps the staircase will have
    :type step: int
    :param height: The height of the staircase
    :type height: int or float
    :param x: The x coordinate for the pattern origin. Default 0.
    :type x: int
    :param y: The y coordinate for the pattern origin. Default 0.
    :type y: int
    :raises: TypeError
    '''
    origin = cursorSetOrigin(cursor, x, y)  # sets the starting point of the stair
    cursor.color(defPenColor, defPenColor)
    cursor.begin_fill()
    cursor.setheading(90)                   # draws the back of the stairs
    cursor.forward(height)
    cursor.right(90)                        # draws the first step
    cursor.forward(height/step)
    for i in range(0, step - 1):            # draws the rest of the steps
        cursor.right(90)
        cursor.forward(height/step)
        cursor.left(90)
        cursor.forward(height/step)
    cursor.right(90)                        # draws the last step
    cursor.forward(height/step)
    cursor.goto(origin)                     # draws the base of the stairs
    cursor.end_fill()
    cursor.color(defPenColor)

def spiral(cursor, coil, size, x=0, y=0):
    '''Draws a simple spiral
    
    :param cursor: The turtle that will be running this function.
    :type cursor: Turtle
    :param coil: Controls how tightly the spiral is coiled
    :type coil: int
    :param size: Controls the size of the spiral
    :type size: int or float
    :param x: The x coordinate for the pattern origin. Default 0.
    :type x: int
    :param y: The y coordinate for the pattern origin. Default 0.
    :type y: int
    :raises: TypeError
    '''
    origin = cursorSetOrigin(cursor, x, y)  # sets the starting point of the spiral
    rad = 1
    while(abs(cursor.pos()) < abs(origin) + size):
        rad += 1
        cursor.circle(rad, coil)

def heart(cursor, size, fill='red', angle=90, x=0, y=0):
    '''Draws a heart with the default fill color
    
    :param cursor: The turtle that will be running this function.
    :type cursor: Turtle
    :param size: Controls the size of the heart
    :type size: (r,g,b) float tuple, hex notation string, or common color name as string
    :param size: Sets the color of the heart. Default red.
    :type size: int
    :param angle: Controls how narrow the heart will be. Minimum 60, Maximum 120. Default 90
    :type angle: int
    :param x: The x coordinate for the pattern origin. Default 0.
    :type x: int
    :param y: The y coordinate for the pattern origin. Default 0.
    :type y: int
    :raises: TypeError
    '''
    origin = cursorSetOrigin(cursor, x, y)  # sets the starting point of the heart
    if angle < 60:                          # corrects problematic angle value
        angle = 60
    elif angle > 120:
        angle = 120
    cursor.fillcolor(fill)                  # set fill color
    cursor.begin_fill()
    cursor.setheading(angle)                # Draws the left half of the heart
    cursor.circle(size, 225)
    while cursor.xcor() < origin[0]:
        cursor.forward(1)
    cursor.penup()                          # Resets pen back to origin
    cursor.goto(origin)
    cursor.pendown()
    cursor.setheading(-angle)               # Draws the right heart of the heart
    cursor.circle(size, -225)
    cursor.right(180)                       # Flip the cursor to the correct direction (otherwise it draws upwards)
    while cursor.xcor() > origin[0]:
        cursor.forward(1)
    cursor.end_fill()
    cursor.fillcolor("")                    # revert fill color to transparent

def makePainting(cursor):
    '''Makes a procedurally generated painting out of all available patterns.
    
    :param cursor: The turtle that will be running this function.
    :type cursor: Turtle
    '''    
    
    defSize = cursor.pensize()    
    cursor.pensize(3)                                           # thickens the line so it's easier to see the mandala
    mandala(cursor,                                             # draws a mandala at 0,0.
            random.choice([True, False]),                       # Random if it's rainbow coloured or not
            random.randint(round(yAxis*0.2), round(yAxis*0.7)),             
    )
    cursor.pensize(defSize)
    
    for i in range(1, random.randint(0, 20)):                   # put a random amount of spirals and hearts
        pattern = random.choice([spiral, heart])
        positionX = random.randint(-xAxis, xAxis)
        positionY = random.randint(round(-yAxis*0.8), round(yAxis*0.8))
        if pattern == spiral:
            spiral(cursor,
                    random.randint(3, 100),
                    random.randint(10, 180),
                    positionX,
                    positionY
            )
        elif pattern == heart:
            heart(cursor,
                    random.randint(10, 30),
                    rainbowColor[random.randint(0, 6)],
                    random.randint(60, 120),
                    positionX,
                    positionY
            )
            
    
    stair(cursor,                                               # draws a stair at the bottom left
            step=random.randint(2, 30), 
            height=random.randint(round(height*0.1), round(height*0.6)),
            x=xAxis*-0.9,
            y=yAxis*-0.9
    )
    
    hydra(cursor,                                               # draws a hydra at the bottom right
            x=xAxis*0.8,
            y=yAxis*random.uniform(-0.8, 0.9)
    )

'''
=== Main execution ===
'''
def mainDraw():
    '''Main draw function. Draws two paintings.'''
    cursor = turtle.Turtle()
    initCursor(cursor)            # initialises default settings


    makePainting(cursor)          # starts drawing iteration 1
    pause(cursor, 10)             # pause between drawings, clears canvas
    makePainting(cursor)          # starts drawing interation 2
    pause(cursor, 10)             # pause, clears canvas
    
    # uncomment the below segment to keep creating drawings infinitely
    #while True:
    #    makePainting(cursor)
    #    pause(cursor, 10)
    
 
if __name__ == '__main__':
    mainDraw() 

wn.exitonclick()
