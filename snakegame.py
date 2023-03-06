#imports
import turtle
import time
import random

delay = 0.2

#scores
score = 0
high_score = 0

#set up screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor('white')
wn.setup(width=600, height=600)
wn.tracer(0)

#snake head
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

#snake food
food= turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments = []

#scoreboards
sc = turtle.Turtle()
sc.speed(0)
sc.shape("square")
sc.color("black")
sc.penup()
sc.hideturtle()
sc.goto(0,260)
sc.write("score: 0  High score: 0", align = "center", font=("ds-digital", 20, "normal"))

#start game
# start_game = turtle.Turtle()
# start_game.speed(0)
# start_game.shape("square")
# start_game.color("green")
# start_game.penup()
# start_game.hideturtle()
# start_game.goto(0, 150)
# start_game.write("Start The Game",align = "center", font=("ds-digital", 20, "normal"))

#game over
game_sc = turtle.Turtle()
game_sc.speed(0)
game_sc.shape("square")
game_sc.color("red")
game_sc.penup()
game_sc.hideturtle()
game_sc.goto(0,50)

#Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_left():
    if head.direction != "right":
        head.direction = "left"
def go_right():
    if head.direction != "left":
        head.direction = "right"
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)

#keyboard bindings
wn.listen()
wn.onkey(go_up, "Up")
wn.onkey(go_down, "Down")
wn.onkey(go_left, "Left")
wn.onkey(go_right, "Right")

#MainLoop
while True:
    wn.update()
    #check collision with border area
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>220 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        game_sc.write("Game Over", align="center", font=("ds-digital", 30, "normal"))

        #hide the segments of body
        for segment in segments:
            segment.goto(1000,1000) #out of range
        #clear the segments
        segments.clear()



        #reset score
        score = 0

        #reset delay
        delay = 0.2

        sc.clear()
        sc.write("score: {}  High score: {}".format(score, high_score), align="center", font=("ds-digital", 20, "normal"))
    else:
        game_sc.clear()


    #check collision with food
    if head.distance(food) <20:
        # move the food to random place
        x = random.randint(-230,230)
        y = random.randint(-230,230)
        food.goto(x,y)

        #add a new segment to the head
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("black")
        new_segment.penup()
        segments.append(new_segment)

        #shorten the delay
        delay -= 0.001
        #increase the score
        score += 10

        if score > high_score:
            high_score = score
        sc.clear()
        sc.write("score: {}  High score: {}".format(score,high_score), align="center", font=("ds-digital", 20, "normal"))

    #move the segments in reverse order
    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)
    #move segment 0 to head
    if len(segments)>0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()

    #check for collision with body
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            #hide segments
            for segment in segments:
                segment.goto(1000,1000)
            segments.clear()
            score = 0
            delay = 0.1

            #update the score
            sc.clear()
            sc.write("score: {}  High score: {}".format(score,high_score), align="center", font=("ds-digital", 20, "normal"))
    time.sleep(delay)
wn.mainloop()