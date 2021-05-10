from tkinter import *

def button(input):
    expression.delete(0, END)
    expression.insert(0, str(expression.get()) + str(input))

gui = Tk()
gui.title("Boolean Calculator")

# Calculation result box
expression = Text(gui, height=3)
expression.grid(row=0, column=0, columnspan=3)

# Defining buttons
button_left_par = Button(gui, text="(",  pady=20, command=lambda: button("("))
button_right_par = Button(gui, text=")", pady=20, command=lambda: button(")"))
button_A = Button(gui, text="A", pady=20, command=lambda: button("A"))
button_AND = Button(gui, text="AND", pady=20, command=lambda: button("AND"))
button_OR = Button(gui, text="OR", pady=20, command=lambda: button("OR"))
button_B = Button(gui, text="B", pady=20, command=lambda: button("B"))
button_NOT = Button(gui, text="NOT", pady=20, command=lambda: button("NOT"))
button_equals = Button(gui, text="=", pady=20, command=lambda: button("="))

# Formatting buttons
button_left_par.grid(row=1, column=0, sticky="ew")
button_right_par.grid(row=1, column=1, sticky="ew")
button_A.grid(row=1, column=2, sticky="ew")
button_AND.grid(row=2, column=0, sticky="ew")
button_OR.grid(row=2, column=1, sticky="ew")
button_B.grid(row=2, column=2, sticky="ew")
button_NOT.grid(row=3, column=0, sticky="ew")
button_equals.grid(row=3, column=1, columnspan = 2, sticky="ew")

gui.mainloop()