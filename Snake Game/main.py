from turtle import Screen
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(width=400, height=400)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

screen.listen()

my_snake = Snake()
food = Food()

screen.onkey(my_snake.up, "Up")
screen.onkey(my_snake.down, "Down")
screen.onkey(my_snake.left, "Left")
screen.onkey(my_snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    my_snake.move()

    if my_snake.head.distance(food) < 15:
        food.refresh()

screen.exitonclick()
