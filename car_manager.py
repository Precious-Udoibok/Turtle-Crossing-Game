COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
import random

# Create cars that are 20px high by 40px wide that are randomly generated along the y-axis
# and move to the left edge of the screen. No cars should be generated in the top and bottom 50px of the
# screen (think of it as a safe zone for our little turtle). Hint: generate a new car only every 6th time
# the game loop runs.

from turtle import Turtle

class CarManager(Turtle):
    def __init__(self):
        #create an empty list  to store the new cars created
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE


    def create_car(self):
        '''create a new car and append it to the car list
        create a new car every 6th time '''
        random_chance = random.randint(1,6)
        if random_chance == 6:
            new_car = Turtle()
            new_car.penup()
            new_car.shape('square')
            new_car.shapesize(stretch_len=2,stretch_wid=1)
            #generate a random color for each car
            new_car.color(random.choice(COLORS))
            #generate a random y coordinate
            random_y = random.randint(-250,250)
            new_car.goto(300,random_y)
            #append it to the car list
            self.all_cars.append(new_car)

    def move_cars(self):
        '''loop through the car list and move each car backwards '''
        for car in self.all_cars:
            car.backward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT



