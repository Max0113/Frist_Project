import turtle 
import random



wind = turtle.Screen()
wind.title("younes")
wind.bgcolor("black")
wind.setup(width=800 , height=600)
wind.tracer(0)


modules_1 = turtle.Turtle()
modules_1.speed(0)
modules_1.shape("turtle")
modules_1.color("blue")
modules_1.shapesize(stretch_wid=2 , stretch_len=2)
modules_1.penup()
modules_1.goto(-350,0)

modules_2 = turtle.Turtle()
modules_2.speed(0)
modules_2.shape("turtle")
modules_2.color("red")
modules_2.shapesize(stretch_wid=2 , stretch_len=2)
modules_2.penup()
modules_2.goto(-350,150)

modules_3 = turtle.Turtle()
modules_3.speed(0)
modules_3.shape("turtle")
modules_3.color("yellow")
modules_3.shapesize(stretch_wid=2 , stretch_len=2)
modules_3.penup()
modules_3.goto(-350,-150)

fin = turtle.Turtle()
fin.speed(0)
fin.shape("square")
fin.color("orange")
fin.shapesize(stretch_wid=25 , stretch_len=0.5)
fin.penup()
fin.goto(350,0)


score = turtle.Turtle()
score.penup()

number = random.randint(1, 3)
n = True

while n :     
    wind.update()
    
    def new_modules_1() :
        x = modules_1.xcor()
        x += random.randint(0, 1)
        modules_1.setx(x)

    def new_modules_2() :
        x = modules_2.xcor()
        x += random.randint(0, 1)
        modules_2.setx(x)

    def new_modules_3() :
        x = modules_3.xcor()
        x += random.randint(0, 1)
        modules_3.setx(x)
    
    if number == 1 :
       new_modules_1()
       new_modules_2()
       new_modules_3()

    if number == 2 :
       new_modules_2()
       new_modules_3()
       new_modules_1()

    if number == 3 :
       new_modules_3()
       new_modules_1()
       new_modules_2()
    
    if  modules_1.xcor() < 350 and  modules_1.xcor() > 320 :
        wind.clear()
        wind.bgcolor("black")
        score.color("blue")
        score.write("blue he is win",align="center" ,font=("Courir",24,"normal"))
        print("blue he is win")
        while True :
            wind.update()

    
    if modules_2.xcor() < 350 and  modules_2.xcor() > 320 :
        wind.clear()
        wind.bgcolor("black")
        score.color("red")
        score.write("red he is win",align="center" ,font=("Courir",24,"normal"))
        print("red he is win")
        while True :
            wind.update()
        
    
    if modules_3.xcor() < 350 and  modules_3.xcor() > 320 :
        wind.clear()
        wind.bgcolor("black")
        score.color("yellow")
        score.write("yellow he is win",align="center" ,font=("Courir",24,"normal"))
        print("yellow he is win")
        while True :
            wind.update()
    
