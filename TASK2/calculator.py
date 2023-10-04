import tkinter as tk
import math


def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))


def clear():
    entry.delete(0, tk.END)


def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


# Creating main window
root = tk.Tk()
root.title("Calculator")
root.resizable(False,False)


# Creating an entry or user input widget
entry = tk.Entry(root, width=30, borderwidth=2)
entry.grid(row=0, column=0, columnspan=4)

# Creating buttons for digits and basic operations
button1 = tk.Button(root, text="7", padx=20, pady=20, command=lambda: button_click(7))
button2 = tk.Button(root, text="8", padx=20, pady=20, command=lambda: button_click(8))
button3 = tk.Button(root, text="9", padx=20, pady=20, command=lambda: button_click(9))
button4 = tk.Button(root, text="4", padx=20, pady=20, command=lambda: button_click(4))
button5 = tk.Button(root, text="5", padx=20, pady=20, command=lambda: button_click(5))
button6 = tk.Button(root, text="6", padx=20, pady=20, command=lambda: button_click(6))
button7 = tk.Button(root, text="1", padx=20, pady=20, command=lambda: button_click(1))
button8 = tk.Button(root, text="2", padx=20, pady=20, command=lambda: button_click(2))
button9 = tk.Button(root, text="3", padx=20, pady=20, command=lambda: button_click(3))
button0 = tk.Button(root, text="0", padx=20, pady=20, command=lambda: button_click(0))

button_add = tk.Button(root, text="+", padx=20, pady=20, command=lambda: button_click("+"))
button_subtract = tk.Button(root, text="-", padx=20, pady=20, command=lambda: button_click("-"))
button_multiply = tk.Button(root, text="*", padx=20, pady=20, command=lambda: button_click("*"))
button_divide = tk.Button(root, text="/", padx=20, pady=20, command=lambda: button_click("/"))
button_sqrt = tk.Button(root, text="√", padx=20, pady=20, command=lambda: button_click("math.sqrt("))
button_factorial = tk.Button(root, text=")", padx=20, pady=20, command=lambda: button_click(")"))
button_sq = tk.Button(root, text="x²", padx=20, pady=20, command=lambda: button_click("**2"))
button_decimal = tk.Button(root, text=".", padx=20, pady=20, command=lambda: button_click("."))
button_clear = tk.Button(root, text="C", padx=20, pady=20, command=clear)
button_equals = tk.Button(root, text="=", padx=20, pady=20, command=calculate)

# To place buttons on the grid
button1.grid(row=2, column=0)
button2.grid(row=2, column=1)
button3.grid(row=2, column=2)
button4.grid(row=3, column=0)
button5.grid(row=3, column=1)
button6.grid(row=3, column=2)
button7.grid(row=4, column=0)
button8.grid(row=4, column=1)
button9.grid(row=4, column=2)
button0.grid(row=5, column=1)

button_sq.grid(row=1, column=0)
button_sqrt.grid(row=1, column=1)
button_factorial.grid(row=1, column=2)
button_clear.grid(row=1, column=3)
button_add.grid(row=5, column=3)
button_subtract.grid(row=4, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=2, column=3)
button_decimal.grid(row=5, column=0)
button_equals.grid(row=5, column=2)

root.mainloop()
