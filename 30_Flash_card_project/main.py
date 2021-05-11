from tkinter import *
import pandas
import random
import time

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}
# -------------------------------------------------------------------------------
try:
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("french_words.csv")
    to_learn = original_data.to_dict(orient='records')
else:
    to_learn = data.to_dict("records")

# Functions


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(text_title, text="French", fill='black')
    canvas.itemconfig(text_word, text=current_card["French"], fill='black')
    canvas.itemconfig(card_background, image=card_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(text_title, text="English")
    canvas.itemconfig(text_word, text=current_card["English"], fill='white')
    canvas.itemconfig(card_background, image=card_back_img)


def is_known():
    to_learn.remove(current_card)
    new_data = pandas.DataFrame(to_learn)
    new_data.to_csv('words_to_learn.csv', index=False)
    next_card()

# -----------------------------------------------------------------------------------


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# Card
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_img)
text_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 30, "italic"))
text_word = canvas.create_text(400, 250, text="Word", font=("Ariel", 50, "bold"))
canvas.grid(row=0, column=0, columnspan=2)


# Buttons
button_img = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=button_img, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

button_img_y = PhotoImage(file="images/right.png")
known_button = Button(image=button_img_y, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)


next_card()

window.mainloop()