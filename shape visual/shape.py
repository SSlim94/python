from graphics import *
import random
import time     # importing all files 

ball = {}

# Do some simple drawing
window = GraphWin("Visualisation", 600, 600)

# Read in and print out the data in the data file
datafile = open("data.txt",'r')
lines = datafile.readlines()



for line in lines:
    xpos = random.randint(50,600)    #declaring x position and placing circle at random position 
    ypos = random.randint(50,600)
    mark = float(line.strip());     #creating a float for the marks 
    #ball = Circle(Point(xpos,ypos), mark)
    time.sleep(1)      
    
    #ball.append
    if(mark >= 30) and (mark < 39):  #if mark is lower then specified draw a cirlce
        ball = Circle(Point(xpos,ypos), mark)   #putting cirlce at random position 
        ball.setFill(color_rgb(255,255,255)) #set fill colour for the mark
        ball.draw(window) # drawing cirle 
    if(mark >= 40) and (mark < 49): 
        ball = Circle(Point(xpos,ypos), mark) 
        ball.setFill(color_rgb(255,0,0))
        ball.draw(window)
    if(mark >= 50) and (mark < 59): 
        ball = Circle(Point(xpos,ypos), mark) 
        ball.setFill(color_rgb(251,51,0))
        ball.draw(window)
    if(mark >= 60) and (mark < 69): 
        ball = Circle(Point(xpos,ypos), mark) 
        ball.setFill(color_rgb(102,255,51))
        ball.draw(window)
    if(mark >= 70) and (mark < 86): 
        ball = Circle(Point(xpos,ypos), mark) 
        ball.setFill(color_rgb(0,255,0))
        ball.draw(window)        
    
xspeed = 1  #setting speed of circle 
yspeed = 1
    
while True:     
    currentPos = ball.getCenter()
    if(currentPos.getY() >= 600): yspeed = -yspeed    #determining circle speeds
    if(currentPos.getY() <= 0): yspeed = -yspeed
    if(currentPos.getX() >= 600): xspeed = -xspeed
    if(currentPos.getX() <= 0): xspeed = -xspeed
    ball.move(xspeed,yspeed)   
 


    


# Waits until the mouse is clicked before closing the window
window.getMouse()