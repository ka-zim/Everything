import turtle
import time
import random

# Screen
wn = turtle.Screen()
wn.bgcolor("white")
wn.setup(700, 700) #x,y
wn.title("Snake by Kazim")
wn.tracer(0)

# Borders
top = turtle.Turtle()
top.penup()
top.speed(0)
top.color("black")
top.shape("square")
top.shapesize(0.1,29.3) #y,x
top.goto(0,292) #x,y

right = turtle.Turtle()
right.penup()
right.speed(0)
right.color("black")
right.shape("square")
right.shapesize(29.3,0.1) #y,x
right.goto(292,0) #x,y

bottom = turtle.Turtle()
bottom.penup()
bottom.speed(0)
bottom.color("black")
bottom.shape("square")
bottom.shapesize(0.1,29.3) #y,x
bottom.goto(0,-292) #x,y

left = turtle.Turtle()
left.penup()
left.speed(0)
left.color("black")
left.shape("square")
left.shapesize(29.3,0.1) #y,x
left.goto(-292,0) #x,y

# Snake 
snake = turtle.Turtle()
snake.penup()
snake.speed(0)
snake.shape("square")
snake.color("green")
snake.goto(0,0) #x,y
snake.dx = 0
snake.dy = 0
snake.direction = "stop"

# Snake movement
def snake_up():
    if snake.direction != "down":
        snake.direction = "up"
def snake_down():
    if snake.direction != "up":
        snake.direction = "down"
def snake_right():
    if snake.direction != "left":
        snake.direction = "right"
def snake_left():
    if snake.direction != "right":
        snake.direction = "left"
def move():
    if snake.direction == "up":
        snake.dx = 0
        snake.dy = 20
    if snake.direction == "down":
        snake.dx = 0
        snake.dy = -20
    if snake.direction == "right":
        snake.dx = 20
        snake.dy = 0
    if snake.direction == "left":
        snake.dx = -20
        snake.dy = 0
    if snake.direction == "stop":
        snake.dx = 0
        snake.dy = 0
wn.listen()
wn.onkeypress(snake_up, "w"); wn.onkeypress(snake_up, "Up")
wn.onkeypress(snake_down, "s"); wn.onkeypress(snake_down, "Down")
wn.onkeypress(snake_right, "d"); wn.onkeypress(snake_right, "Right")
wn.onkeypress(snake_left, "a"); wn.onkeypress(snake_left, "Left")

# Scoreboard
sb = turtle.Turtle()
sb.color("black")
sb.penup()
sb.hideturtle()
sb.goto(0, 300)
score = 0
high_score = 0
sb.write("Score: {}             Highscore: {}".format(score, high_score), align="center", font=("System", 24))

# Food locations
food_location = [-280,-260,-240,-220,-200,-180,-160,-140,-120,-100,-80,-60,-40,-20,0,20,40,60,80,100,120,140,160,180,200,220,240,260,280]
x = random.randint(0,28)
y = random.randint(0,28)

# Food
food = turtle.Turtle()
food.penup()
food.speed(0)
food.color("red")
food.shape("square")
food.goto(food_location[x],food_location[y])


# Snake segmnets 
segments = []

while True:
    wn.update()
    move()

    # Snake delta x,y cords 
    time.sleep(0.08)
    snake.setx(snake.xcor() + snake.dx)
    snake.sety(snake.ycor() + snake.dy)
    time.sleep(0)

    # Border elimination
    if snake.xcor() > 280 or snake.xcor() < -280 or snake.ycor() > 280 or snake.ycor() < -280:
        segments = []
        snake.goto(0,0)
        snake.direction = "stop"
        score = 0
        sb.clear()
        sb.write("Score: {}             Highscore: {}".format(score, high_score), align="center", font=("System", 24))

    # Eating food
    elif snake.ycor() < food.ycor() + 20 and snake.ycor() > food.ycor() - 20 and snake.xcor() < food.xcor() + 20 and snake.xcor() > food.xcor() - 20:
        score += 10
        sb.clear()
        sb.write("Score: {}             Highscore: {}".format(score, high_score), align="center", font=("System", 24))
        x = random.randint(0,28)
        y = random.randint(0,28)
        food.goto(food_location[x],food_location[y])

        # Appending new segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("green")
        new_segment.penup()
        segments.append(new_segment)

    if score >= high_score:
        high_score = score
        sb.clear()
        sb.write("Score: {}             Highscore: {}".format(score, high_score), align="center", font=("System", 24))

    # Move all of the tail upto but not including the one before the head (that being segments[0])
    for i in range(len(segments) - 1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)

    # Move segment 0 to main snake location
    if len(segments) > 0:
        x = snake.xcor()
        y = snake.ycor()
        segments[0].goto(x,y)
    
    # Finish later when not lazy
