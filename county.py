import turtle


class County(turtle.Turtle):

    def __init__(self, x, y, county):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x, y)
        self.write(county, True, align="center", font=("Arial", 8, "normal"))
