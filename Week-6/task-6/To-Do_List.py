import tkinter as tk
from tkinter import messagebox
import csv
import os

FILENAME = "tasks.csv"
tasks = []

# Load tasks from CSV
def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, newline='') as f:
            reader = csv.reader(f)
            tasks.clear()
            for row in reader:
                if row:
                    tasks.append(row[0])
        list_update()

# Save all tasks to CSV
def save_tasks():
    with open(FILENAME, 'w', newline='') as f:
        writer = csv.writer(f)
        for task in tasks:
            writer.writerow([task])

# Add task to list
def add_task():
    task = task_field.get().strip()
    if task:
        tasks.append(task)
        list_update()
        save_tasks()
        task_field.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Task cannot be empty!")

# Delete selected task
def delete_task():
    try:
        selected = task_listbox.curselection()[0]
        tasks.pop(selected)
        list_update()
        save_tasks()
    except IndexError:
        messagebox.showwarning("Selection Error", "No task selected.")

# Delete all tasks
def delete_all_tasks():
    if messagebox.askyesno("Confirm Delete", "Delete all tasks?"):
        tasks.clear()
        list_update()
        save_tasks()

# Update listbox UI
def list_update():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)

# Exit the application
def close_app():
    root.destroy()

# ---------------- GUI Design ----------------
root = tk.Tk()
root.title("Stylish To-Do List Manager")
root.geometry("700x450+500+250")
root.configure(bg="#2C3E50")
root.resizable(False, False)

functions_frame = tk.Frame(root, bg="#34495E")
functions_frame.pack(expand=True, fill="both", padx=20, pady=20)

title = tk.Label(functions_frame, text="📝 Stylish To-Do List Manager", font=("Helvetica", 20, "bold"),
                 bg="#34495E", fg="#ECF0F1")
title.pack(pady=(0, 10))

# Entry field + Add button
input_frame = tk.Frame(functions_frame, bg="#34495E")
input_frame.pack(pady=5)

task_field = tk.Entry(input_frame, font=("Arial", 14), width=38, bg="#ECF0F1", fg="#2C3E50", relief=tk.FLAT)
task_field.grid(row=0, column=0, padx=10, pady=5)

add_button = tk.Button(input_frame, text="Add Task", width=12, font=("Arial", 12, "bold"),
                       bg="#27AE60", fg="white", activebackground="#2ECC71", relief=tk.RAISED, command=add_task)
add_button.grid(row=0, column=1)

# Task list area
list_frame = tk.Frame(functions_frame, bg="#34495E")
list_frame.pack(pady=10)

task_listbox = tk.Listbox(list_frame, width=60, height=10, font=("Arial", 12), bg="#ECF0F1", 
                          fg="#2C3E50", selectbackground="#3498DB", activestyle='none')
task_listbox.pack(side="left", fill="y")

scrollbar = tk.Scrollbar(list_frame, orient=tk.VERTICAL)
scrollbar.config(command=task_listbox.yview)
scrollbar.pack(side="right", fill="y")
task_listbox.config(yscrollcommand=scrollbar.set)

# Buttons (Delete/Exit)
button_frame = tk.Frame(functions_frame, bg="#34495E")
button_frame.pack(pady=15)

del_button = tk.Button(button_frame, text="Delete Selected", width=18, font=("Arial", 12, "bold"),
                       bg="#E74C3C", fg="white", activebackground="#C0392B", relief=tk.RAISED, command=delete_task)
del_button.grid(row=0, column=0, padx=10)

del_all_button = tk.Button(button_frame, text="Delete All", width=18, font=("Arial", 12, "bold"),
                           bg="#E67E22", fg="white", activebackground="#D35400", relief=tk.RAISED, command=delete_all_tasks)
del_all_button.grid(row=0, column=1, padx=10)

exit_button = tk.Button(functions_frame, text="Exit Application", width=40, font=("Arial", 12, "bold"),
                        bg="#95A5A6", fg="white", activebackground="#7F8C8D", relief=tk.RAISED, command=close_app)
exit_button.pack(pady=(10, 0))

# Load tasks on startup
load_tasks()
root.mainloop()
