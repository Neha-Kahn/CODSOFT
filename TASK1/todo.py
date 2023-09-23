#NehaKhan
#ToDo List GUI APP

from tkinter import *
from tkinter import messagebox


# Function to add a task
def add_task():
    task_text = task.get()
    if task_text:
        task_list.insert(END, task_text)
        task.set("")
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Please enter a task.")


# Function to delete a selected task
def delete_task():
    selected_task_index = task_list.curselection()
    if selected_task_index:
        task_list.delete(selected_task_index)
        save_tasks()
    else:
        messagebox.showwarning("Error","Please select a task to delete.")


# Function to edit a selected task
def edit_task():
    selected_task_index = task_list.curselection()
    if selected_task_index:
        selected_task = task_list.get(selected_task_index)
        updated_task_text = task.get()
        if updated_task_text:
            task_list.delete(selected_task_index)
            task_list.insert(selected_task_index, updated_task_text)
            task.set("")
            save_tasks()
        else:
            messagebox.showwarning("Warning", "Please enter a task then press edit.")
    else:
        messagebox.showwarning("Warning", "Select a task to edit.")


# Function to save tasks to a file
def save_tasks():
    with open("tasks.txt", "w") as file:
        tasks = task_list.get(0, END)
        for task_text in tasks:
            file.write(task_text + "\n")


# Function to load tasks from a file
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                task_list.insert(END, line.strip())
    except FileNotFoundError:
        pass


root = Tk()
root.title("To-Do List")
root.geometry("800x500+200+100")
root.resizable(False,True)

top_bar = PhotoImage(file="topbar.png")
Label(root,width=900,image=top_bar).pack()

heading = Label(root,text = "Add Items", font="Arial 15",fg="black")
heading.place(x=50,y=150)

frame = Frame(root,width=400,height=50,bg='white',borderwidth=1,relief='sunken')
frame.place(x=50,y=200)
task = StringVar()
task_entry = Entry(frame, width=18,font="arial 20",bd="0",textvariable=task)
task_entry.place(x=10,y=7)

button = Button(root,width=6,bg='grey',borderwidth=1,relief='sunken',text="submit",command=add_task)
button.place(x=460,y=210)


heading2 = Label(root,text = "Tasks", font="Arial 15",fg="black")
heading2.place(x=50,y=260)


# scrollbar for the task list
task_list_scrollbar = Scrollbar(root, orient=VERTICAL)
task_list_scrollbar.place(x=680, y=280, height=200)

task_list = Listbox(root, width=70, height=8, font="Arial 12", selectbackground="grey", yscrollcommand=task_list_scrollbar.set)
task_list.place(x=50, y=300)

task_list_scrollbar.config(command=task_list.yview)

delete_button = Button(root, width=6, bg='red', borderwidth=1, relief='sunken', text="Delete", command=delete_task)
delete_button.place(x=700, y=300)

edit_button = Button(root, width=6, bg='green', borderwidth=1, relief='sunken', text="Edit",command=edit_task)
edit_button.place(x=700, y=330)

# Load tasks from the file when the program starts
load_tasks()

root.mainloop()
