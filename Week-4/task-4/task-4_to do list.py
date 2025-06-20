# import sqlite3

# # Initialize or connect to the database
# conn = sqlite3.connect('listOfTasks.db')
# cursor = conn.cursor()
# cursor.execute('CREATE TABLE IF NOT EXISTS tasks (title TEXT)')

# # Fetch all tasks into memory
# def retrieve_tasks():
#     cursor.execute('SELECT title FROM tasks')
#     return [row[0] for row in cursor.fetchall()]

# # Add a new task
# def add_task():
#     task = input("Enter a new task: ").strip()
#     if task:
#         cursor.execute('INSERT INTO tasks VALUES (?)', (task,))
#         conn.commit()
#         print("Task added!")
#     else:
#         print("Empty task. Nothing added.")

# # View tasks
# def view_tasks():
#     tasks = retrieve_tasks()
#     if tasks:
#         print("\n--- To-Do List ---")
#         for i, task in enumerate(tasks, start=1):
#             print(f"{i}. {task}")
#     else:
#         print("\nNo tasks found.")

# # Delete a specific task
# def delete_task():
#     view_tasks()
#     tasks = retrieve_tasks()
#     if tasks:
#         try:
#             task_num = int(input("Enter task number to delete: "))
#             if 1 <= task_num <= len(tasks):
#                 cursor.execute('DELETE FROM tasks WHERE title = ?', (tasks[task_num - 1],))
#                 conn.commit()
#                 print("Task deleted.")
#             else:
#                 print("Invalid task number.")
#         except ValueError:
#             print("Please enter a valid number.")
#     else:
#         print("No tasks to delete.")

# # Delete all tasks
# def delete_all_tasks():
#     confirm = input("Are you sure you want to delete all tasks? (yes/no): ").strip().lower()
#     if confirm == "yes":
#         cursor.execute('DELETE FROM tasks')
#         conn.commit()
#         print("All tasks deleted.")
#     else:
#         print("Cancelled.")

# # Menu loop
# def menu():
#     while True:
#         print("\n--- TO-DO LIST MENU ---")
#         print("1. View Tasks")
#         print("2. Add Task")
#         print("3. Delete Task")
#         print("4. Delete All Tasks")
#         print("5. Exit")

#         choice = input("Choose an option (1-5): ").strip()

#         if choice == '1':
#             view_tasks()
#         elif choice == '2':
#             add_task()
#         elif choice == '3':
#             delete_task()
#         elif choice == '4':
#             delete_all_tasks()
#         elif choice == '5':
#             print("Goodbye!")
#             break
#         else:
#             print("Invalid choice. Please select 1-5.")

# # Run the program
# if __name__ == "__main__":
#     menu()
#     conn.close()

import sqlite3
import os
import logging

# Logging setup
logging.basicConfig(filename="todo.log", level=logging.INFO, format='%(asctime)s - %(message)s')

# DB initialization
def init_db():
    conn = sqlite3.connect("todo.db")
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_task():
    task = input("Enter your task: ").strip()
    if task:
        conn = sqlite3.connect("todo.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO tasks (description) VALUES (?)", (task,))
        conn.commit()
        conn.close()
        logging.info(f"Added task: {task}")
        print("✅ Task added!")
    else:
        print("❌ Task cannot be empty.")

def view_tasks():
    conn = sqlite3.connect("todo.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")
    rows = cur.fetchall()
    conn.close()
    if not rows:
        print("📂 No tasks found.")
    else:
        print("\n📋 Your To-Do List:")
        for row in rows:
            print(f"{row[0]}. {row[1]}")

def delete_task():
    view_tasks()
    try:
        task_id = int(input("Enter the task ID to delete: "))
        conn = sqlite3.connect("todo.db")
        cur = conn.cursor()
        cur.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        if cur.rowcount == 0:
            print("❌ Task ID not found.")
        else:
            conn.commit()
            logging.info(f"Deleted task ID: {task_id}")
            print("🗑️ Task deleted.")
        conn.close()
    except ValueError:
        print("❌ Please enter a valid number.")

def menu():
    init_db()
    while True:
        print("\n=== CLI To-Do List with SQLite ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")
        choice = input("Enter your choice (1–4): ").strip()

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid option. Please try again.")

menu()

