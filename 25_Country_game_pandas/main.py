import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


# If answer_state is one of the states in all the states of the 50_states.csv
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

guessed = 0
list_of_guessed_state = []
while len(list_of_guessed_state) < 50:
    answer_state = screen.textinput(title=f"{guessed}/50 States guessed", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in list_of_guessed_state:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed += 1
        list_of_guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

# states to learn.csv
