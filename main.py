import turtle



wm = turtle.Screen()
wm.title("Pong Game")
wm.bgcolor("black")
wm.setup(width=800, height=600)
wm.tracer(0) #so we can update screen manually


score_A = 0
score_B = 0

# PaddleA
paddle_a = turtle.Turtle()
paddle_a.speed(0) #animation speed
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350, 0)
paddle_a.shapesize(5, 1)


# PaddleB
paddle_b = turtle.Turtle()
paddle_b.speed(0) #animation speed
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350, 0)
paddle_b.shapesize(5, 1)

# Ball
ball = turtle.Turtle()
ball.speed(0) #animation speed, sets to fastest speed
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 3
ball.dy = 3


# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: {}    Player B: {}".format(score_A, score_B), align="center", font=("Courier", 24, "normal"))


pen1 = turtle.Turtle()
pen1.speed(0)
pen1.color("white")
pen1.penup()
pen1.hideturtle()
pen1.goto(0, 0)



def paddle_up_a():
    y = paddle_a.ycor()
    if y < 250:
        y += 20
        paddle_a.sety(y)


def paddle_down_a():
    y = paddle_a.ycor()
    if y > -250:
        y -= 20
        paddle_a.sety(y)


def paddle_up_b():
    y = paddle_b.ycor()
    if y < 250:
        y += 20
        paddle_b.sety(y)

def paddle_down_b():
    y = paddle_b.ycor()
    if y > -250:
        y -= 20
        paddle_b.sety(y)

# def paddle_left_b():
#     x = paddle_b.xcor()
#     x -= 20
#     paddle_b.setx(x)



# Keyboard Binding
wm.listen()
wm.onkeypress(paddle_up_a, "w")
wm.onkeypress(paddle_down_a, "s")
wm.onkeypress(paddle_up_b, "Up")
wm.onkeypress(paddle_down_b, "Down")
# wm.onkeypress(paddle_left_b, "Left")


#Main game Loop

while True:
    wm.update()
    #updates the screen

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    # xcor and ycor is for current coordinate
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        # set current y coordiante as 290, then while loop continues and ball. dy changes to negative so moves down
        ball.dy = ball.dy * -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy = ball.dy * -1

    if ball.xcor() > 390:
        ball.setx(0)
        ball.sety(0)
        score_A += 1
        pen.clear()
        pen.write("Player A: {}    Player B: {}".format(score_A, score_B), align="center",
                  font=("Courier", 24, "normal"))
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.setx(0)
        ball.sety(0)
        score_B += 1
        pen.clear()
        pen.write("Player A: {}    Player B: {}".format(score_A, score_B), align="center",
                  font=("Courier", 24, "normal"))
        ball.dx *= -1


        # paddle and ball collisions
    if 340 < ball.xcor() < 350 and paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50:
        ball.setx(340)
        ball.dx *= -1

    if -350 < ball.xcor() < -340 and paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50:
        ball.setx(-340)
        ball.dx *= -1

    if score_A > 2:
        pen1.write("Player A IS THE WINNER", align="center", font=("Courier", 50, "normal"))
        break

    if score_B > 3:
        pen1.write("Player B IS THE WINNER", align="center", font=("Courier", 50, "normal"))
        break









