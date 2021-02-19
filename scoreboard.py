from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 80, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.display_score()


    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align = ALIGNMENT, font= FONT)

    def increase_score_left(self):
        self.left_score += 1
        self.display_score()

    def increase_score_right(self):
        self.right_score += 1
        self.display_score()

    def display_score(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.left_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.right_score, align=ALIGNMENT, font=FONT)




