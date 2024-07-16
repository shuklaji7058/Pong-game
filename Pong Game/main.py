
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

# Get player names after initializing screen
player1_name = screen.textinput("Player 1", "Enter name for Player 1 (Left):")
player2_name = screen.textinput("Player 2", "Enter name for Player 2 (Right):")

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard(player1_name, player2_name)

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeyrelease(r_paddle.stop_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeyrelease(r_paddle.stop_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeyrelease(l_paddle.stop_up, "w")
screen.onkeypress(l_paddle.go_down, "s")
screen.onkeyrelease(l_paddle.stop_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    r_paddle.move()
    l_paddle.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
