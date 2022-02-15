from turtle import Turtle, Screen
from player import Player
from obstacle import Obstacle
import time
from score import Score

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("white")
screen.title("Turtle Scratch")
screen.tracer(0)

timmy = Player()
obstacle = Obstacle()
score=Score()


screen.listen()
screen.onkey(key="w", fun=timmy.go_up)


is_game_on = True

while is_game_on:
    time.sleep(.1)
    screen.update()

    obstacle.generate()
    obstacle.move()

    for toby in obstacle.all_obstacles:
        if toby.distance(timmy) < 20:
            is_game_on = False
            score.game_over()
    #Detect successful crossing

    if timmy.is_at_finish_line():
        timmy.go_to_start()
        obstacle.level_up()
        score.increase_level()
        score.update_scoreboard()





screen.exitonclick()