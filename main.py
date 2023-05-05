from tkinter import *


# Function
def button_clicked():
    miles = float(entry.get())
    km = round(miles * 1.60934)
    label3.config(text=f"{km}")


# miles to kilometers converter
window = Tk()
window.title("Miles to Kilometers Converter")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)

# Entry
entry = Entry(width=10)
entry.grid(column=1, row=0)

# Label
label1 = Label(text="Miles")
label1.grid(column=2, row=0)

label2 = Label(text="is equal to")
label2.grid(column=0, row=1)

label3 = Label(text="0")
label3.grid(column=1, row=1)

label4 = Label(text="Km")
label4.grid(column=2, row=1)

# Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

window.mainloop()
