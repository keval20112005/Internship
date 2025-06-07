import tkinter as tk
from math import sqrt

# Function to process button press
def press(key):
    if key == "=":
        try:
            result = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif key == "C":
        entry.delete(0, tk.END)
    elif key == "⌫":
        current = entry.get()
        entry.delete(0, tk.END)
        entry.insert(tk.END, current[:-1])
    elif key == "√":
        try:
            value = float(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, sqrt(value))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif key == "x²":
        try:
            value = float(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, value ** 2)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif key == "xʸ":
        entry.insert(tk.END, "**")
    else:
        entry.insert(tk.END, key)

# Main window
root = tk.Tk()
root.title("Modern Calculator")
root.geometry("320x470")
root.configure(bg="#1e1e2f")
root.resizable(False, False)

# Entry widget
entry = tk.Entry(root, font=("Helvetica", 24), bg="#2c2c3c", fg="white",
                 borderwidth=0, relief="flat", justify="right")
entry.pack(pady=20, padx=10, ipady=10, fill="x")

# Colors
btn_color = {
    "num": "#3a3a4f",
    "op": "#f57f17",
    "func": "#3949ab",
    "equal": "#00c853",
    "text": "white"
}

# Button layout
buttons = [
    ["C", "⌫", "√", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "x²", "="],
    ["xʸ"]
]

# Button frame
frame = tk.Frame(root, bg="#1e1e2f")
frame.pack()

# Create buttons
for r, row in enumerate(buttons):
    for c, char in enumerate(row):
        color = btn_color["num"]  # default number button
        if char in ["+", "-", "*", "/", "%"]:
            color = btn_color["op"]
        elif char in ["C", "⌫", "√", "x²", "xʸ"]:
            color = btn_color["func"]
        elif char == "=":
            color = btn_color["equal"]

        tk.Button(frame, text=char, width=6, height=2, font=("Helvetica", 16),
                  bg=color, fg=btn_color["text"],
                  activebackground="#555", activeforeground="white",
                  bd=0, command=lambda ch=char: press(ch))\
            .grid(row=r, column=c, padx=5, pady=5)

# Fill missing columns if needed
frame.grid_columnconfigure((0, 1, 2, 3), weight=1)

root.mainloop()
