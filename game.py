import turtle
import os
import math
import random
# Set the score to Zero
score=0

# Score Pen
score_p=turtle.Turtle()
score_p.speed(0)
score_p.color("white")
score_p.penup()
score_p.setposition(-290,280)
Scorestring="Score: %s" %score
score_p.write(Scorestring,False,align="left")
score_p.hideturtle()

##################################################

# maintaing high score
highscore=0
hscore_p=turtle.Turtle()
hscore_p.speed(0)
hscore_p.color("white")
hscore_p.penup()
hscore_p.setposition(-290,260)
hScorestring="High Score: %s" %highscore
hscore_p.write(hScorestring,False,align="left")
hscore_p.hideturtle()

#############################################


#Screen Of The game
screen=turtle.Screen()
screen.bgcolor("brown")
#screen.bgpic("giphy.gif")
screen.title("My First Game")
############################################


# Gaming region	
pen1=turtle.Turtle()
pen1.speed(0)
pen1.penup()
pen1.color("red")
pen1.setposition(-300,-300)
pen1.pendown()
pen1.pensize(4)
for i in range(4):
	pen1.fd(600)
	pen1.lt(90)
pen1.hideturtle()
############################################

# Registering an image
turtle.register_shape("player.gif")

#############################################

# Now draw the player pen
penp=turtle.Turtle()
penp.pensize(3)
penp.shape("triangle")
penp.color("blue")
penp.penup()
penp.speed(0)
penp.setposition(0,-250)
penp.setheading(90)
playerspeed=10
 
###############################################

#bullet turtle
bullet=turtle.Turtle()
bullet.shape("triangle")
bullet.color("yellow")
bullet.penup()
bullet.speed(0)
bullet.shapesize(0.5,0.5)
bullet.setheading(90)
bulletspeed=20
state=0
bullet.hideturtle()
################################################

#All the important functions

def fire():#When bullet is fired
	global state
	if state ==0:
		state=1
		bullet.setposition(penp.xcor(),penp.ycor())
		bullet.showturtle()
			
#Move player
def ml():#Move left
	x=penp.xcor()
	x-=playerspeed
	if x < -290:
		x=-290
	penp.setx(x)
def mr():#Move right
	x=penp.xcor()
	x+=playerspeed
	if x > 290:
		x=290
	penp.setx(x)
def collision(t1,t2):#check collision
	dis=math.sqrt((math.pow(t1.xcor()-t2.xcor(),2))+math.pow(t2.ycor()-t1.ycor(),2))
	if dis <= 15:
		return True
	return False
turtle.listen()
turtle.onkey(ml,"Left")
turtle.onkey(mr,"Right")
turtle.onkey(fire,"space")

##############################################################

#CPU turtles
n=int(raw_input("Enter The Number Of Enemies You Want?"))
enemies=[]
for i in range(n):
	enemies.append(turtle.Turtle())

for pene in enemies:
	x=random.randint(-200,200)
	y=random.randint(100,250)
	pene.shape("circle")
	pene.color("black")
	pene.penup()
	pene.speed(0)
	pene.setposition(x,y)
enemyspeed=2
##################################################

#Main Loop
while 1:
	for pene in enemies:
		x=pene.xcor()
		x+=enemyspeed
		pene.setx(x)
		if x>290:
			for i in enemies:
				y=i.ycor()
				y-=40
				i.sety(y)
			enemyspeed*=-1
		if x<-290:
			for i in enemies:
				y=i.ycor()
				y-=40
				i.sety(y)
			enemyspeed*=-1
	if state==1:
		yb=bullet.ycor()
		yb+=bulletspeed
		bullet.sety(yb)
	if bullet.ycor() >= 290:
		state=0
		bullet.hideturtle()
	for pene in enemies:
		if (collision(bullet,pene)):
			score+=100
			if highscore < score:
				highscore=score
			bullet.hideturtle()
			bullet.setposition(0,-400)
			pene.setposition(-200,250)
			state=0
			Scorestring="Score: %s" %score
			score_p.clear()
			score_p.write(Scorestring,False,align="left")
			hScorestring="High Score: %s" %highscore
			hscore_p.clear()
			hscore_p.write(hScorestring,False,align="left")
		if (collision(penp,pene)):
			penp.hideturtle()
			pene.hideturtle()
			print "Game Over"
			break

####################################################################

# Keep the o/p stable
delay=raw_input("Press Enter to Esc")
