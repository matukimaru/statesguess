import turtle

import pandas as pd

from scoreboard import Scoreboard
from county import County

data = pd.read_csv("counties.csv")
counties = data["County"].to_list()

screen = turtle.Screen()

screen.title("Counties of Kenya")
screen.screensize(904, 761)
image = "counties_blank.gif"
screen.addshape(image)
turtle.shape(image)

scoreboard = Scoreboard(len(counties))
scoreboard.update()


guessed = []

for _ in range(len(counties)):
    ans = screen.textinput(title=f"Kenya Counties", prompt="Write the county name.")

    if ans.title() in counties and ans.title() not in guessed:
        scoreboard.score += 1
        guessed.append(ans.title())
        x = int(data[data["County"] == ans.title()].x)
        y = int(data[data["County"] == ans.title()].y)
        County(x, y, ans.title())

    scoreboard.attempt += 1
    scoreboard.update()

screen.mainloop()
# screen.exitonclick()
