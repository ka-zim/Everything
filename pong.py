import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(800, 600) # (x,y)
wn.title("Pong by Kazim")
wn.tracer(0)

# Middle line 
line = turtle.Turtle()
line.penup()
line.speed(0)
line.shape("square")
line.color("white")
line.shapesize(30, 0.1)

# Top, right, bottom, left lines
top = turtle.Turtle()
top.penup()
top.shape("square")
top.color("white")
top.shapesize(0.1, 40)
top.goto(0, 300)

right = turtle.Turtle()
right.penup()
right.shape("square")
right.color("white")
right.shapesize(30.1, 0.1)# (y,x)
right.goto(400, 0) # (x, y)

bottom = turtle.Turtle()
bottom.penup()
bottom.shape("square")
bottom.color("white")
bottom.shapesize(0.1, 40)
bottom.goto(0, -300) 

left = turtle.Turtle()
left.penup()
left.shape("square")
left.color("white")
left.shapesize(30.1, 0.1)# (y,x)
left.goto(-400, 0) # (x, y)

# paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.color("white")
paddle_a.shape("square")
paddle_a.shapesize(5, 1) # (y,x)
paddle_a.penup()
paddle_a.goto(-350, 0)

# paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.color("white")
paddle_b.shape("square")
paddle_b.shapesize(5, 1) # (y,x)
paddle_b.penup()
paddle_b.goto(350, 0) # (x, y)

# Paddle A up
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

# Paddle A down
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

# Paddle B up
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

# Paddle B down
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Keyboard input
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Ball 
ball = turtle.Turtle()
ball.penup()
ball.shapesize(1,1) # (y,x)
ball.speed(0)
ball.color("white")
ball.shape("square")
ball.goto(0,0)
ball.dx = .4
ball.dy = .4

# Scoreboard
sb = turtle.Turtle()
sb.pendown()
sb.goto(-0, 235) #(x,y)
sb.shape("square")
sb.color("white")
sb.write("A: 0      B: 0", align="center", font=("System", 36))
sb.hideturtle()
score_a = 0
score_b = 0

while True:
    wn.update()

    # Moving the ball 
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # Table borders
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1 
    
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dy = .4
        ball.dx = .4
        ball.dx *= -1
        score_a += 1
        sb.clear()
        sb.write("A: {}      B: {}".format(score_a, score_b), align="center", font=("System", 36))
    
    elif ball.xcor() < -390:
        ball.goto(0,0)
        ball.dy = .4
        ball.dx = .4
        ball.dx *= -1
        score_b += 1
        sb.clear()
        sb.write("A: {}      B: {}".format(score_a, score_b), align="center", font=("System", 36))
    
    # Paddle and ball collisions 
    if ball.xcor() > 330 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.setx(330)
        ball.dx *= -1
        ball.dx -= 0.025
        ball.dy -= 0.025
        
    elif ball.xcor() < -330 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.setx(-330)
        ball.dx *= -1
        ball.dx += 0.025
        ball.dy += 0.025
    
    # Limiting paddle movement
    if paddle_b.ycor() > 240:
        paddle_b.sety(240)
    
    elif paddle_b.ycor() < -240:
        paddle_b.sety(-240)

    if paddle_a.ycor() > 240:
        paddle_a.sety(240)
    
    elif paddle_a.ycor() < -240:
        paddle_a.sety(-240)
    
    # Determining winner
    if score_a == 10:
        sb.goto(0,0)
        sb.color('red')
        sb.write("Player A won", align="center", font=("Comic sans", 38))
        turtle.done()

    elif score_b == 10:
        sb.goto(0,0)
        sb.color('red')
        sb.write("Player B won", align="center", font=("Comic sans", 38))
        turtle.done()

    # Finished
