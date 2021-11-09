import time
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0) # screen sie nie odswieza

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


# repeat moving until..
game_flag = True
while game_flag:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15: #food 10x10
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() > -280 or snake.head.ycor() > 280 or snake.head.ycor() > -280:
        game_flag = False
        scoreboard.game_over()

    #Detect collision with tail
    #if head. collides with any segment in
    for segment in snake.segments[1:]: #slicing: all except segments[0]
        # if segment == snake.head:
        #     pass # bypassing through collision of head and rest from cords 0,0
        if snake.head.distance(segment) < 10:
            game_flag = False
            scoreboard.game_over()



screen.exitonclick()

# Create a snake body
# Move the snake
# Control the snake
# Detect collision with food
# Create a scoreboard
# Detect collision with wall
# Detect collision with tail
