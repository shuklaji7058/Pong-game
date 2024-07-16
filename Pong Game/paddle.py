# from turtle import Turtle
#
#
# class Paddle(Turtle):
#
#     def __init__(self, position):
#         super().__init__()
#         self.shape("square")
#         self.color("white")
#         self.shapesize(stretch_wid=5, stretch_len=1)
#         self.penup()
#         self.goto(position)
#
#     def go_up(self):
#         new_y = self.ycor() + 20
#         self.goto(self.xcor(), new_y)
#
#     def go_down(self):
#         new_y = self.ycor() - 20
#         self.goto(self.xcor(), new_y)
from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
        self.move_speed = 20
        self.moving_up = False
        self.moving_down = False

    def go_up(self):
        self.moving_up = True

    def go_down(self):
        self.moving_down = True

    def stop_up(self):
        self.moving_up = False

    def stop_down(self):
        self.moving_down = False

    def move(self):
        if self.moving_up:
            new_y = self.ycor() + self.move_speed
            self.goto(self.xcor(), new_y)
        elif self.moving_down:
            new_y = self.ycor() - self.move_speed
            self.goto(self.xcor(), new_y)
