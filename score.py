from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.penup()
        self.write_score()

    def write_score(self):
        self.clear()
        self.home()
        self.goto(0, 250)
        self.write("Score: " + str(self.score), True, align=ALIGNMENT, font=FONT)
        self.ht()

    def add_score(self):
        self.score += 1
        self.write_score()

    def game_over(self):
        self.home()
        self.write("Game Over", True, align=ALIGNMENT, font=FONT)
        self.ht()
