import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
turtle_player = Player()
scoreboard = Scoreboard()

car_manager = CarManager()

screen.listen()
screen.onkey(turtle_player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.2)
    screen.update()

    car_manager.create_car()
    car_manager.move()

    # Detect collision with the cars
    for car in car_manager.all_cars:
        if car.distance(turtle_player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect successful crossing
    if turtle_player.is_at_finish_line():
        turtle_player.go_to_start()
        car_manager.level_up()
        scoreboard.up_level()

screen.exitonclick()
