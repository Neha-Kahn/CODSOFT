import random
import string
import tkinter as tk
from tkinter import messagebox


def generate_password(length, complexity):
    if complexity == "low":
        characters = string.ascii_letters
    elif complexity == "medium":
        characters = string.ascii_letters + string.digits
    elif complexity == "high":
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        return "Invalid complexity level."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def generate_password_action():
    try:
        length = int(length_entry.get())
        if length <= 0:
            messagebox.showerror("Error", "Please enter a valid password length as a positive integer.")
            return
        complexity = complexity_var.get()
        password = generate_password(length, complexity)
        password_label.config(text="Generated Password: " + password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid password length.")


def reset_password_action():
    length_entry.delete(0, tk.END)
    complexity_var.set("low")
    password_label.config(text="Generated Password: ")


app = tk.Tk()
app.title("Password Generator")
app.geometry("500x350+200+100")

heading_font_style = ("Arial", 12, "bold" )
font_style = ("Arial", 12 )

heading = tk.Label(app, text="Password Generator", font=("Arial", 14, "bold",),fg='blue')
heading.place(x=170,y=30)


length_label = tk.Label(app, text="Enter password length:", font=font_style)
length_label.place(x=20,y=90)

length_entry = tk.Entry(app, font=font_style)
length_entry.place(x=210,y=90)

complexity_label = tk.Label(app, text="Select complexity:", font=font_style)
complexity_label.place(x=20,y=140)

complexity_var = tk.StringVar()
complexity_var.set("low")

low_button = tk.Radiobutton(app, text="Low", variable=complexity_var, value="low", font=font_style)
medium_button = tk.Radiobutton(app, text="Medium", variable=complexity_var, value="medium", font=font_style)
high_button = tk.Radiobutton(app, text="High", variable=complexity_var, value="high", font=font_style)

low_button.place(x=210,y=140)
medium_button.place(x=270,y=140)
high_button.place(x=360,y=140)

generate_button = tk.Button(app, text="Generate Password", command=generate_password_action, bg='Blue', fg='white', font=heading_font_style )
generate_button.place(x=170,y=190)

reset_button = tk.Button(app, text="Reset", command=reset_password_action, font=font_style)
reset_button.place(x=220,y=230)

password_label = tk.Label(app, text="Generated Password: ", font=heading_font_style)
password_label.place(x=20,y=280)

app.mainloop()
