import tkinter as tk
from tkinter import messagebox

#add a task
def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

#delete a task
def delete_task():
    try:
        selected_task_index = listbox.curselection()
        listbox.delete(selected_task_index)
    except:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

#task as completed
def mark_completed():
    try:
        selected_task_index = listbox.curselection()
        task = listbox.get(selected_task_index)
        listbox.delete(selected_task_index)
        listbox.insert(selected_task_index, task + " - Completed")
    except:
        messagebox.showwarning("Selection Error", "Please select a task to mark as completed.")

# main window
root = tk.Tk()
root.title("To-Do List Application")

#input field for adding tasks
entry = tk.Entry(root, width=40)
entry.pack(pady=10)

#buttons for adding, deleting, and completing tasks
add_button = tk.Button(root, text="Add Task", width=15, command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", width=15, command=delete_task)
delete_button.pack(pady=5)

complete_button = tk.Button(root, text="Mark Completed", width=15, command=mark_completed)
complete_button.pack(pady=5)

#display tasks
listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=10)

root.mainloop()
