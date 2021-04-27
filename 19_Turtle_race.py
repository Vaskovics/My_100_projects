from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter the color")
print(user_bet)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]


is_race_on = False
i = 0
y = -150
all_turtle = []
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.goto(x=-240, y=y)
    new_turtle.color(colors[i])
    i += 1
    y += 60
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")#
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()