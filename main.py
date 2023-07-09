from turtle import Screen, Turtle
from snake import Snake
from food import Food
from score import Score
import time

mys = Screen()
mys.setup(650, 650)

mys.title("Snake game")
mys.bgcolor("black")
mys.tracer(0)
snake = Snake()
food = Food()
score = Score()

mys.listen()
mys.onkey(snake.up, "Up")
mys.onkey(snake.down, "Down")
mys.onkey(snake.left, "Left")
mys.onkey(key="Right", fun=snake.right)

game = True
while game:
    tt = Turtle()
    tt.hideturtle()
    tt.color("white")
    tt.penup()
    tt.goto(-325, 290)
    tt.pendown()
    tt.goto(325, 290)
    mys.update()
    time.sleep(.1)
    snake.move()

    if snake.head.distance(food) < 13:
        food.refresh()
        snake.extend()
        score.inc_score()

    # if score.score >= 15:
    #     score.win()
    #     game = False

    if snake.head.xcor() > 325 or snake.head.xcor() < -325 or snake.head.ycor() > 290 or snake.head.ycor() < -325:
        score.reset()
        snake.snake_reset()

    for segment in snake.segments[1:]:
        # if segment==snake.head:
        #     pass
        if snake.head.distance(segment) < 5:
            score.reset()
            snake.snake_reset()

mys.exitonclick()
