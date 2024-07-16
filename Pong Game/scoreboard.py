# from turtle import Turtle
#
#
# class Scoreboard(Turtle):
#
#     def __init__(self):
#         super().__init__()
#         self.color("white")
#         self.penup()
#         self.hideturtle()
#         self.l_score = 0
#         self.r_score = 0
#         self.update_scoreboard()
#
#     def update_scoreboard(self):
#         self.clear()
#         self.goto(-100, 200)
#         self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
#         self.goto(100, 200)
#         self.write(self.r_score, align="center", font=("Courier", 80, "normal"))
#
#     def l_point(self):
#         self.l_score += 1
#         self.update_scoreboard()
#
#     def r_point(self):
#         self.r_score += 1
#         self.update_scoreboard()
from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self, player1_name, player2_name):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))
        self.goto(-200, 260)
        self.write(self.player1_name, align="center", font=("Courier", 24, "normal"))
        self.goto(200, 260)
        self.write(self.player2_name, align="center", font=("Courier", 24, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
