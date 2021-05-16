import turtle
import pandas

screen = turtle.Screen()
screen.setup(1200, 800)
screen.title("Міста України")
image = "Ukraine.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("data_Urkaine.csv")
all_cities = data["City"].to_list()

guessed_cities = []
while len(guessed_cities) < 50:
    answer_city = screen.textinput(title=f"{len(guessed_cities)}/50 States guessed",
                                   prompt="What's another state's name?").title()
    if answer_city == "Exit":
        missing_cities = []
        for city in all_cities:
            if city not in guessed_cities:
                missing_cities.append(city)
        new_data = pandas.DataFrame(missing_cities)
        break
    elif answer_city in all_cities:
        guessed_cities.append(answer_city)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        city_data = data[data.City == answer_city]
        t.goto(int(city_data.x), int(city_data.y))
        t.color("red")
        t.write(answer_city, font=("Courier", 11, "bold"))

screen.exitonclick()