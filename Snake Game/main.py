from turtle import Screen
from snake import Snake
from out_square import Square, OUT_RANGE_A, OUT_RANGE_B
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=400, height=400)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

screen.listen()

my_snake = Snake()
out_side = Square()
food = Food()
score = Scoreboard()

screen.onkey(my_snake.up, "Up")
screen.onkey(my_snake.down, "Down")
screen.onkey(my_snake.left, "Left")
screen.onkey(my_snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    my_snake.move()

    # detect collision with food
    if my_snake.head.distance(food) < 15:
        food.refresh()
        my_snake.extend()
        score.increase_score()

    # detect collision with wall
    if my_snake.head.xcor() > OUT_RANGE_B or my_snake.head.xcor() < OUT_RANGE_A or my_snake.head.ycor() > OUT_RANGE_B or my_snake.head.ycor() < OUT_RANGE_A:
        score.game_over()
        game_is_on = False

    # detect collision with own tail
    for segment in my_snake.segments[1:]:
        if my_snake.head.distance(segment) < 10:
            score.game_over()
            game_is_on = False

screen.exitonclick()
