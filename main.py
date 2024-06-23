import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(1, delay=0)

r_bar = Paddle((350, 0))
l_bar = Paddle((-350, 0))
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(r_bar.go_up, "Up")
screen.onkeypress(r_bar.go_down, "Down")
screen.onkeypress(l_bar.go_up, "w")
screen.onkeypress(l_bar.go_down, "s")

ball = Ball()

is_game = True

while is_game:
    time.sleep(ball.move_speed)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_bar) < 50 and ball.xcor() > 320 or ball.distance(l_bar) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.goto(0,0)
        ball.bounce_x()
        scoreboard.l_point()
        ball.move_speed = 0.1

    if ball.xcor() < -380:
        ball.goto(0, 0)
        ball.bounce_x()
        scoreboard.r_point()
        ball.move_speed = 0.1


screen.exitonclick()
