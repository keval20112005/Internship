import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import sqlite3
import csv
from datetime import datetime
import matplotlib.pyplot as plt

# ------------------ Models ------------------
class Expense:
    def __init__(self, date, category, description, amount):
        self.date = date
        self.category = category
        self.description = description
        self.amount = amount


class ExpenseManager:
    def __init__(self, db_name="expenses.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        query = """CREATE TABLE IF NOT EXISTS expenses (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        date TEXT,
                        category TEXT,
                        description TEXT,
                        amount REAL
                    )"""
        self.conn.execute(query)
        self.conn.commit()

    def add_expense(self, expense: Expense):
        self.conn.execute("INSERT INTO expenses(date, category, description, amount) VALUES (?,?,?,?)",
                          (expense.date, expense.category, expense.description, expense.amount))
        self.conn.commit()

    def delete_expense(self, expense_id):
        self.conn.execute("DELETE FROM expenses WHERE id=?", (expense_id,))
        self.conn.commit()

    def get_all_expenses(self):
        cursor = self.conn.execute("SELECT * FROM expenses")
        return cursor.fetchall()

    def filter_expenses(self, category=None, month=None):
        query = "SELECT * FROM expenses WHERE 1=1"
        params = []
        if category:
            query += " AND category=?"
            params.append(category)
        if month:
            query += " AND strftime('%m', date)=?"
            params.append(f"{int(month):02d}")
        cursor = self.conn.execute(query, tuple(params))
        return cursor.fetchall()

    def calculate_summary(self):
        cursor = self.conn.execute("SELECT SUM(amount) FROM expenses")
        return cursor.fetchone()[0] or 0


class ReportGenerator:
    def __init__(self, manager: ExpenseManager):
        self.manager = manager

    def category_summary(self):
        cursor = self.manager.conn.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
        return cursor.fetchall()

    def monthly_summary(self):
        cursor = self.manager.conn.execute("SELECT strftime('%Y-%m', date), SUM(amount) FROM expenses GROUP BY strftime('%Y-%m', date)")
        return cursor.fetchall()

    def generate_chart(self, chart_type="pie"):
        summary = self.category_summary()
        if not summary:
            messagebox.showwarning("No Data", "No expenses available for report.")
            return

        categories = [s[0] for s in summary]
        amounts = [s[1] for s in summary]

        plt.figure(figsize=(6, 6))
        if chart_type == "pie":
            plt.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=140)
            plt.title("Category-wise Expense Distribution")
        else:  # bar chart
            plt.bar(categories, amounts, color="skyblue")
            plt.title("Category-wise Expense Summary")
            plt.ylabel("Amount (₹)")
        plt.show()


# ------------------ GUI ------------------
class ExpenseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("💰 Smart Expense Manager")
        self.root.geometry("900x600")
        self.root.configure(bg="#f5f6fa")

        # Core components
        self.manager = ExpenseManager()
        self.reporter = ReportGenerator(self.manager)

        # Notebook (Tabs)
        notebook = ttk.Notebook(root)
        notebook.pack(fill="both", expand=True, padx=10, pady=10)

        self.tab_add = tk.Frame(notebook, bg="#f5f6fa")
        self.tab_view = tk.Frame(notebook, bg="#f5f6fa")
        self.tab_report = tk.Frame(notebook, bg="#f5f6fa")

        notebook.add(self.tab_add, text="➕ Add Expense")
        notebook.add(self.tab_view, text="📜 View Expenses")
        notebook.add(self.tab_report, text="📊 Reports")

        self.setup_add_tab()
        self.setup_view_tab()
        self.setup_report_tab()

    # ---------------- Add Expense ----------------
    def setup_add_tab(self):
        tk.Label(self.tab_add, text="Add New Expense", font=("Arial", 18, "bold"), bg="#f5f6fa", fg="#2c3e50").pack(pady=20)

        form = tk.Frame(self.tab_add, bg="#f5f6fa")
        form.pack(pady=10)

        tk.Label(form, text="Date (YYYY-MM-DD):", bg="#f5f6fa").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.entry_date = tk.Entry(form)
        self.entry_date.insert(0, datetime.now().strftime("%Y-%m-%d"))
        self.entry_date.grid(row=0, column=1, pady=5)

        tk.Label(form, text="Category:", bg="#f5f6fa").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.combo_category = ttk.Combobox(form, values=["Food", "Transport", "Utilities", "Entertainment", "Shopping", "Others"])
        self.combo_category.grid(row=1, column=1, pady=5)
        self.combo_category.current(0)

        tk.Label(form, text="Description:", bg="#f5f6fa").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.entry_desc = tk.Entry(form, width=40)
        self.entry_desc.grid(row=2, column=1, pady=5)

        tk.Label(form, text="Amount (₹):", bg="#f5f6fa").grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.entry_amount = tk.Entry(form)
        self.entry_amount.grid(row=3, column=1, pady=5)

        tk.Button(form, text="Add Expense", command=self.add_expense, bg="#27ae60", fg="white",
                  font=("Arial", 12, "bold"), width=20).grid(row=4, column=0, columnspan=2, pady=20)

    def add_expense(self):
        date = self.entry_date.get()
        category = self.combo_category.get()
        description = self.entry_desc.get()
        amount = self.entry_amount.get()

        if not (date and category and description and amount):
            messagebox.showwarning("Input Error", "All fields are required.")
            return

        try:
            amount = float(amount)
        except:
            messagebox.showerror("Invalid Input", "Amount must be a number.")
            return

        exp = Expense(date, category, description, amount)
        self.manager.add_expense(exp)
        messagebox.showinfo("Success", "Expense added successfully!")
        self.entry_desc.delete(0, tk.END)
        self.entry_amount.delete(0, tk.END)
        self.refresh_view()

    # ---------------- View Expenses ----------------
    def setup_view_tab(self):
        tk.Label(self.tab_view, text="All Expenses", font=("Arial", 18, "bold"), bg="#f5f6fa", fg="#2c3e50").pack(pady=20)

        columns = ("ID", "Date", "Category", "Description", "Amount")
        self.tree = ttk.Treeview(self.tab_view, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center")
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

        btn_frame = tk.Frame(self.tab_view, bg="#f5f6fa")
        btn_frame.pack(pady=10)
        tk.Button(btn_frame, text="Delete Selected", command=self.delete_expense, bg="#e74c3c", fg="white").pack(side="left", padx=10)
        tk.Button(btn_frame, text="Export CSV", command=self.export_csv, bg="#2980b9", fg="white").pack(side="left", padx=10)

        self.refresh_view()

    def refresh_view(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for exp in self.manager.get_all_expenses():
            self.tree.insert("", tk.END, values=exp)

    def delete_expense(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Selection Error", "Please select an expense to delete.")
            return
        expense_id = self.tree.item(selected[0])["values"][0]
        self.manager.delete_expense(expense_id)
        self.refresh_view()
        messagebox.showinfo("Deleted", "Expense deleted successfully.")

    def export_csv(self):
        filename = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
        if filename:
            with open(filename, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["ID", "Date", "Category", "Description", "Amount"])
                for exp in self.manager.get_all_expenses():
                    writer.writerow(exp)
            messagebox.showinfo("Exported", "Data exported successfully!")

    # ---------------- Reports ----------------
   # ---------------- Reports ----------------
    def setup_report_tab(self):
        tk.Label(self.tab_report, text="Expense Reports", 
             font=("Arial", 18, "bold"), 
             bg="#f5f6fa", fg="#2c3e50").pack(pady=20)

        tk.Button(self.tab_report, 
              text="Show Pie Chart", 
              command=lambda: self.reporter.generate_chart("pie"), 
              bg="#8e44ad", fg="white", 
              font=("Arial", 12, "bold")).pack(pady=10)

        tk.Button(self.tab_report, 
              text="Show Bar Chart", 
              command=lambda: self.reporter.generate_chart("bar"), 
              bg="#16a085", fg="white", 
              font=("Arial", 12, "bold")).pack(pady=10)
        
if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseApp(root)
    root.mainloop()
