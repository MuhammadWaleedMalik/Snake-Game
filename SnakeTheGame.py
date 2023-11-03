from turtle import Screen
from snake import Snake
import time
from food import Food 
from scoreborad import scoreboard

screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
screen.listen()
     
snake=Snake()
food=Food()
scoreboard=scoreboard()


screen.onkeypress(snake.up,key="Up")
screen.onkeypress(snake.down,key="Down")
screen.onkeypress(snake.left,key="Left")
screen.onkeypress(snake.right,key="Right")


is_game_on=True
while is_game_on: 
    time.sleep(0.1)   
    screen.update() 
    snake.move()
    if(snake.head.distance(food)<15):
        food.refresh()
        scoreboard.increase_score()
        snake.extend()
    if(snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.xcor()<-280):
        # is_game_on=False
        scoreboard.reset()
        snake.reset()    
    for segments in snake.segments[1:]:
        if(snake.head.distance(segments)<10):
            # is_game_on=False
            scoreboard.reset()
            snake.reset()    
     
      
























screen.exitonclick()