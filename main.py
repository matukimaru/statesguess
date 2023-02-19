import turtle

import pandas as pd
from fuzzywuzzy import fuzz

from scoreboard import Scoreboard
from state import State

COUNTRY = "kenya"

data = pd.read_csv(f"resources/{COUNTRY}/states.csv")
states = data["State"].to_list()

screen = turtle.Screen()

screen.title(f"States of {COUNTRY.title()}")
screen.screensize(904, 761)
image = f"resources/{COUNTRY}/states.gif"
screen.addshape(image)
turtle.shape(image)

scoreboard = Scoreboard(len(states))
scoreboard.update()


# def compare(a):
#     s = ""
#     f = 0
#     for st in states:
#         per = fuzz.ratio(a.lower(), st.lower())
#         if per > f:
#             f = per
#             s = st
#
#     return [s, f]


guessed = []

for _ in range(len(states)):
    ans = screen.textinput(title=f"{COUNTRY.title()} states", prompt="Write the state name")

    if ans.title() in states and ans.title() not in guessed:
        scoreboard.score += 1
        guessed.append(ans.title())
        x = int(data[data["State"] == ans.title()].x)
        y = int(data[data["State"] == ans.title()].y)
        State(x, y, ans.title())

    # # partial matching
    # else:
    #     for state in states:
    #         fz = compare(ans.lower())
    #         print(f"Guess: {ans.lower()} ; State: {state.lower()} ; fuzz = {fz}")
    #         if fz[1] > 90:
    #             print(fz[0])
    #             scoreboard.score += 1
    #             guessed.append(state.title())
    #             x = int(data[data["State"] == state.title()].x)
    #             y = int(data[data["State"] == state.title()].y)
    #             State(x, y, state.title())

    scoreboard.attempt += 1
    scoreboard.update()

screen.mainloop()
# screen.exitonclick()
