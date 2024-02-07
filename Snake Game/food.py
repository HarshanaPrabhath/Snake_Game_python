import random
from turtle import Turtle
from out_square import OUT_RANGE_A, OUT_RANGE_B


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("red")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.refresh()

    def refresh(self):
        random_x = random.randint(OUT_RANGE_A + 20, OUT_RANGE_B - 20)
        random_y = random.randint(OUT_RANGE_A + 20, OUT_RANGE_B - 20)
        self.goto(random_x, random_y)
