import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
screen.onkeypress(player.up, 'Up')  # controls the turtle's movement using the up arrow key
player_score = Scoreboard()
cars = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    '''every 0.1 seconds create a new car and move it'''
    cars.create_car()
    cars.move_cars()

    #Detect collision with car object
    for each_car in cars.all_cars:
        '''if the car to the distance of the player is less than 20 end the game'''
        if player.distance(each_car) <  20:
            game_is_on = False
            player_score.game_over()


    #Detect if the player has reached finished line
    #set the player to the starting position
    if player.finish_line():
        player.go_to_start()
        cars.increase_speed()
        player_score.level_up()



screen.exitonclick()



