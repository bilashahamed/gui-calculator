import tkinter as tk

# Function to update expression
def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

# Function to evaluate expression
def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set(" error ")
        expression = ""

# Function to clear
def clear():
    global expression
    expression = ""
    equation.set("")

# main window
root = tk.Tk()
root.configure(background="lightblue")
root.title("Simple Calculator")
root.geometry("300x400")

expression = ""
equation = tk.StringVar()

# Entry box
entry_field = tk.Entry(root, textvariable=equation, font=('Arial', 18), bd=10, relief="ridge", justify="right")
entry_field.grid(columnspan=4, ipadx=8, ipady=8, padx=10, pady=10)

# Buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for (text, row, col) in buttons:
    if text == "=":
        action = equalpress
    else:
        action = lambda x=text: press(x)
    tk.Button(root, text=text, height=2, width=6, font=("Arial", 14), command=action, bg="lightyellow").grid(row=row, column=col, padx=5, pady=5)

# Clear button
tk.Button(root, text="Clear", height=2, width=26, font=("Arial", 14), command=clear, bg="lightgreen").grid(row=5, column=0, columnspan=4, padx=5, pady=5)

root.mainloop()
