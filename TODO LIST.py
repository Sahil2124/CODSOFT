#Task - 3  To-Do List Application
import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("TO-DO LIST APP")
window.geometry("600x600")

tasks = []

def updatelistbox():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)

def addtask():
    task = entry.get()
    if task != "":
        tasks.append(task)
        updatelistbox()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task")

def deletetask():
    try:
        selected_task_index = task_listbox.curselection()[0]
        tasks.pop(selected_task_index)
        updatelistbox()
    except:
        messagebox.showwarning("Selection Error", "Please select a task to delete")

def updatetask():
    try:
        selected_task_index = task_listbox.curselection()[0]
        new_task = entry.get()
        if new_task != "":
            tasks[selected_task_index] = new_task
            updatelistbox()
            entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a new task")
    except:
        messagebox.showwarning("Selection Error", "Please select a task to update")


title_label = tk.Label(window, text="My To-Do List", font=("Times New Roman", 25, "bold"))
title_label.pack(pady=10)


entry = tk.Entry(window, font=("Times New Roman", 15), width=35)
entry.pack(pady=10)


butn_frame = tk.Frame(window)
butn_frame.pack(pady=10)

add_btn = tk.Button(butn_frame, text="Add Task", command=addtask, width=10)
add_btn.grid(row=0, column=0, padx=5)

update_btn = tk.Button(butn_frame, text="Update Task", command=updatetask, width=10)
update_btn.grid(row=0, column=1, padx=5)

delete_btn = tk.Button(butn_frame, text="Delete Task", command=deletetask, width=10)
delete_btn.grid(row=0, column=2, padx=5)


task_listbox = tk.Listbox(window, font=("Times New Roman", 12), width=45, height=20)
task_listbox.pack(pady=20)

window.mainloop()
