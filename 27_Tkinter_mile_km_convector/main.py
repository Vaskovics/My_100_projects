from tkinter import *
# window
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=400, height=200)
window.config(padx=30, pady=30)

# label
label_miles = Label(text="Miles")
label_miles.grid(column=3, row=2)

label_equal = Label(text="is equal to ")
label_equal.grid(column=1, row=3)

label_km = Label(text="km")
label_km.grid(column=3, row=3)

label_result = Label()
label_result.grid(column=2, row=3)


# Function
def convert():
    miles = int(entry.get())
    result = round(miles * 1.609)
    label_result["text"] = result


# input
entry = Entry(width=7)
entry.grid(column=2, row=2)

# button
button = Button(text="Calculate", command=convert)
button.grid(column=2, row=4)

window.mainloop()