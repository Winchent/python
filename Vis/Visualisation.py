#this'n imports the file with all the stuff in it
from graphics import *
import random
from random import randrange

with open('data.txt', 'r') as data:
    circledata = data.read().split("\n")
    print(circledata)

#sets the name of the window and how big it is
window = GraphWin("Visualisation", 1000, 500)


# randrange gives you an integral value
for thecircles in circledata:
    randomx = randrange(0, 1000)
    randomy = randrange(0, 500)

#setting the location, size and colour of the ball
#make sure you add on 31 so that they're not bunched too close together
    ball = Circle(Point(randomx,randomy), int(thecircles))
    ball.setFill(color_rgb(255,255,0))


#set the speed of the thing
#since the x positions don't actually matter, there is no need to create a new xspeed every time
#smart thing about these speeds by the way, since some of the results are the same, there is no need to create a new speed for each one, just the ones that have already been created
xspeed = 0
yspeed = int(thecircles)/10

#declare the ball to be drawn in the window
ball.draw(window)


#making sure the ball doesn't break the bounds of the window and destroys the world or anything like that
#make sure you change everything to match the ball that it is for
#i suppose the x positions don't matter, since the balls aren't moving from side to side!
while True:
    currentPosition = ball.getCenter()
    if(currentPosition.getY() <= 0): yspeed = -yspeed
    if(currentPosition.getY() >= 500): yspeed = -yspeed
    ball.move(xspeed, yspeed)
    

#this should close the window at the click of the mouse but doesn't for some stupid reason
window.getMouse(window.close)