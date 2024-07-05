from turtle import Turtle
FONT = ("Courier", 24, "normal")

#create a class that keeps record of the player level and increase their level
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.level = 1
        self.hideturtle()
        self.goto(-280,250)
        self.write(arg=f'Level = {self.level} ',align='left',font=FONT)

    def level_up(self):
        ''''increase the level of the player when the reach the finish line'''
        self.level+=1
        self.clear()
        self.write(arg=f'Level = {self.level} ',align='left',font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(arg='GAME OVER', align='center', font = FONT)
