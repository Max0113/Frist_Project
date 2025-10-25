# This is a simple Python script that uses the turtle graphics library to draw a square.
import turtle

# prepare le windowe pour start the game
wind = turtle.Screen()
wind.title("younes")
wind.bgcolor("orange")
wind.setup(width=800 , height=600)
wind.tracer(0)

# module_1
module_1 = turtle.Turtle()
module_1.speed(0)
module_1.shape("square")
module_1.color("red")
module_1.shapesize(stretch_wid=5 , stretch_len=1)
module_1.penup()
module_1.goto(-350,0)

# module_2
module_2 = module_1.clone()
module_1.color("blue")
module_2.goto(350,0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("black")
ball.penup()
ball.goto(0,0)
ball.dx = 0.5
ball.dy = 0.5

#function
def module_1_Up() :
    y = module_1.ycor()
    y += 30
    module_1.sety(y)
def module_1_Down() :
    y = module_1.ycor()
    y -= 30
    module_1.sety(y)
def module_2_Up() :
    y = module_2.ycor()
    y += 30
    module_2.sety(y)
def module_2_Down() :
    y = module_2.ycor()
    y -= 30
    module_2.sety(y)

# keybord 

wind.listen()
wind.onkeypress(module_1_Up, "w")
wind.onkeypress(module_1_Down, "s")
wind.onkeypress(module_2_Up, "Up")
wind.onkeypress(module_2_Down, "Down")

# score
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0 , 260)
score.write("Player 1 : 0  Player 2 : 0",align="center" ,font=("Courir",24,"normal"))
while True :
    wind.update()

    # mouvement de la ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290 :
        ball.dy *= -1
        
    if ball.ycor() < -290 :
        ball.dy *= -1
        

    if ball.xcor() > 390 :
       ball.dx *= -1
       ball.goto(0,0)
       score.clear()
       score1 +=1
       score.write("Player 1 : {}  Player 2 : {}".format(score1,score2),align="center" ,font=("Courir",24,"normal"))
    
    if ball.xcor() < -390 :
       ball.dx *= -1
       ball.goto(0,0)
       score.clear()
       score2 += 1
       score.write("Player 1 : {}  Player 2 : {}".format(score1,score2),align="center" ,font=("Courir",24,"normal"))

    if ( ball.xcor() > 340 and ball.xcor() < 350 ) and ( ball.ycor() < module_2.ycor() + 40 and ball.ycor() > module_2.ycor() - 40 ) :
       ball.setx(340)
       ball.dx *= -1

    if ( ball.xcor() < -340 and ball.xcor() > -350 ) and ( ball.ycor() < module_1.ycor() + 40 and ball.ycor() > module_1.ycor() - 40 ) :
       ball.setx(-340)
       ball.dx *= -1
       
    


