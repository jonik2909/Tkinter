from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Radio Buttons")

# r = IntVar()
# r.set("2")

MODES = [
    ("Peperoni", "Peperoni"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion"),
]

pizza = StringVar()
pizza.set("Peperoni")

for text, mode in MODES:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)

def clicked(value):
    myLabel = Label(root, text=pizza.get())
    myLabel.pack()

# Radiobutton(root, text="option-1", variable=r, value=1, command=lambda : clicked(r.get())).pack()
# Radiobutton(root, text="option-2", variable=r, value=2, command=lambda : clicked(r.get())).pack()

# myLabel = Label(root, text=pizza.get())
# myLabel.pack()

myButton = Button(root, text="Click me!", command=lambda: clicked(pizza.get()))
myButton.pack()

root.mainloop()