from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.create_paddle(position)

    def create_paddle(self, position):
        self.penup()
        self.color("white")
        self.goto(position)
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)

    def move_up(self):
        x = self.xcor()
        y = self.ycor()
        self.goto(x, y + 20)

    def move_down(self):
        x = self.xcor()
        y = self.ycor()
        self.goto(x, y - 20)
