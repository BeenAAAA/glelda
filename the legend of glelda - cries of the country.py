import turtle
import time
screennum = 0
while (600 >= screennum):
    screen = turtle.setup(screennum, screennum)
    time.sleep(0.000001)
    screennum = screennum + 1

turtle.speed(10)
import turtle
screen = turtle.Screen()
screen.setup(600, 600) # set the canvas size to 600 by 600
t = turtle.Turtle()
t.hideturtle() # hide the turtle shape
t.penup() # lift the pen up to avoid drawing a line
t.goto(0, 0) # move the turtle to the center of the screen
t.write("best games ever inc.", font=("Arial", 32, "normal"), align="center") # write "Welcome" in Arial font, size 32, normal style, centered
time.sleep(2)
t.clear() # erase everything that t has drawn
t.goto(100, 100) # move the turtle to a new position
t.write("presents", font=("Arial", 32, "normal"), align="center") # write "Goodbye" in Arial font, size 32, normal style, centered
 # keep the window open
time.sleep(2)
t.clear() # erase everything that t has drawn
t.goto(100, 100) # move the turtle to a new position
t.write("the legend of", font=("Arial", 32, "normal"), align="center") # write "Goodbye" in Arial font, size 32, normal style, centered
 # keep the window open
time.sleep(2)
t.clear() # erase everything that t has drawn
t.goto(100, 100) # move the turtle to a new position
t.write("glelda", font=("Arial", 32, "normal"), align="center") # write "Goodbye" in Arial font, size 32, normal style, centered
 # keep the window open
time.sleep(2)
t.clear() # erase everything that t has drawn
t.goto(100, 100) # move the turtle to a new position
t.write("cries of the country", font=("Arial", 32, "normal"), align="center") # write "Goodbye" in Arial font, size 32, normal style, centered
 # keep the window open

t.clear() # clear canvas for SPECTACULAR GAME

print("by the way, the circle you see is just because its in standby.")
pen = turtle.Turtle()
pen.speed(9)
pen.circle(100)

print("1: play full game")
print("2: ULTRA FUN™ games")
startgameQ = input ("would you like to play the full game, or play the ULTRA FUN™ minigames?")

if startgameQ == "1": #hey ben, if you delete the stuff  inside this, your history. love been.
    print("lets start! this will soon clear! also pay atterntion to the screen that says: python turtle graphics. have fun lol")
    print("_")
    print("_")
    print("_")
    print("_")
    print("_")
    print("_")
    print("_")
    print("_")
    print("_")
    print("_")
    print("_")
    print("_")
    print("_")
    print("_")
    print("_")
    print("_")
    print("_")
    print("_")
    print("_")
import random

# Set up the screen
wn = turtle.Screen()
wn.bgcolor("black")

# Create a turtle
t = turtle.Turtle()
t.speed(13)
print("creating art... please wait...")
# Define a function to draw a random line
def draw_random_line(t):
    # Set the pen color to a random RGB value
    t.pencolor((random.random(), random.random(), random.random()))

    # Set the pen width to a random value between 1 and 10
    t.width(random.randint(1, 10))

    # Move the turtle to a random position on the screen
    t.penup()
    t.goto(random.randint(-300, 300), random.randint(-300, 300))
    t.pendown()

    # Draw a line to another random position on the screen
    t.goto(random.randint(-300, 300), random.randint(-300, 300))

# Draw 100 random lines
for _ in range(100):
    draw_random_line(t)

print("in the world of color of fun, where is the darkness, wheres the stupidity.")
time.sleep(10)
t.clear
print("blink...")
time.sleep(3)
print("blink...")
time.sleep(3)
print("open your eyes, wake from your slumber...")
time.sleep(1)
print("setting canvas... please wait...")
while (800 >= screennum):
    screen = turtle.setup(screennum, screennum)
    time.sleep(0.000001)
    screennum = screennum + 1
t.clear()
wn.bgcolor("white")


else: # Hey YOU! if you delete this it will BREAK the option to start the minigames!!!!
    print("wowoowowowowoo")
