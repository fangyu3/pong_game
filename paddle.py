from turtle import Turtle

class Paddle(Turtle):

    def __init__(self,starting_position):
        self.create_paddle(starting_position)

    def create_paddle(self,starting_position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x=starting_position[0],y=starting_position[1])

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(),new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(),new_y)