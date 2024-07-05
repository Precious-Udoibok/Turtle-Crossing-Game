STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle
# Create a turtle player that starts at the bottom of the screenpl  

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def up(self):
        '''moves the turtle forward by the move distance'''
        self.forward(MOVE_DISTANCE)

    def finish_line(self):
        '''returns True if the player has reached finish line or False
        if the player has not reached the finished line'''
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def go_to_start(self):
        '''returns the player to the starting position'''
        self.goto(STARTING_POSITION)
