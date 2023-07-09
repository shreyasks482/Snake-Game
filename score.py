from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 16, "normal")

with open("data.txt", "r") as fp:
    high = int(fp.read())


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.h_score = high
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 300)
        self.write(f"Score = {self.score} High Score = {self.h_score}", align=ALIGN, font=FONT)

    def up_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score} High Score = {self.h_score}", align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.h_score:
            self.h_score = self.score
            inp = str(self.h_score)
            with open("data.txt", "w") as fps:
                fps.write(inp)
        self.score = 0
        self.up_scoreboard()

    def win(self):
        self.goto(0, 0)
        self.write("YOU WIN", align=ALIGN, font=FONT)

    def inc_score(self):
        self.score += 1
        self.up_scoreboard()
