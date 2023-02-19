import turtle


class Scoreboard(turtle.Turtle):

    def __init__(self, total):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.attempt = 0
        self.total = total

    def update(self):
        self.clear()
        self.goto(350, 370)
        self.write(f"   Score: {self.score}\nAttempt: {self.attempt} of {self.total}", align="left",
                   font=("Arial", 10, "bold"))
