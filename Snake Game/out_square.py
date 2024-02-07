from turtle import Turtle

OUT_RANGE_A = -290
OUT_RANGE_B = 290


class Square(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(OUT_RANGE_A, OUT_RANGE_B)
        self.pendown()
        for _ in range(0, 4):
            self.forward(OUT_RANGE_B * 2)
            self.right(90)
