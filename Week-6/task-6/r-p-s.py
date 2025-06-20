# import tkinter as tk
# import random

# # Create the main window
# root = tk.Tk()
# root.title("Rock Paper Scissors")
# root.geometry("400x400")
# root.config(bg="lightblue")

# user_score = 0
# computer_score = 0

# def get_computer_choice():
#     return random.choice(['rock', 'paper', 'scissors'])

# def determine_winner(user, computer):
#     if user == computer:
#         return 'tie'
#     elif (user == 'rock' and computer == 'scissors') or \
#          (user == 'scissors' and computer == 'paper') or \
#          (user == 'paper' and computer == 'rock'):
#         return 'user'
#     else:
#         return 'computer'

# def play(user_choice):
#     global user_score, computer_score

#     computer_choice = get_computer_choice()

#     result_label.config(text=f"You chose: {user_choice}\nComputer chose: {computer_choice}")
#     winner = determine_winner(user_choice, computer_choice)

#     if winner == 'tie':
#         outcome = "It's a tie!"
#     elif winner == 'user':
#         user_score += 1
#         outcome = "You win this round!"
#     else:
#         computer_score += 1
#         outcome = "Computer wins this round!"

#     score_label.config(text=f"Score\nYou: {user_score} | Computer: {computer_score}")
#     outcome_label.config(text=outcome)

# # UI Elements
# title_label = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 18, "bold"), bg="lightblue")
# title_label.pack(pady=10)

# result_label = tk.Label(root, text="", font=("Arial", 12), bg="lightblue")
# result_label.pack(pady=10)

# outcome_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="lightblue", fg="darkgreen")
# outcome_label.pack(pady=10)

# score_label = tk.Label(root, text="Score\nYou: 0 | Computer: 0", font=("Arial", 12), bg="lightblue")
# score_label.pack(pady=10)

# button_frame = tk.Frame(root, bg="lightblue")
# button_frame.pack(pady=20)

# rock_btn = tk.Button(button_frame, text="Rock", width=10, height=2, bg="#f28b82", command=lambda: play("rock"))
# rock_btn.grid(row=0, column=0, padx=10)

# paper_btn = tk.Button(button_frame, text="Paper", width=10, height=2, bg="#aecbfa", command=lambda: play("paper"))
# paper_btn.grid(row=0, column=1, padx=10)

# scissors_btn = tk.Button(button_frame, text="Scissors", width=10, height=2, bg="#ccff90", command=lambda: play("scissors"))
# scissors_btn.grid(row=0, column=2, padx=10)

# exit_btn = tk.Button(root, text="Exit", width=10, height=2, bg="red", fg="white", command=root.destroy)
# exit_btn.pack(pady=20)

# # Start the GUI loop
# root.mainloop()

import tkinter as tk
import random

def play(player_choice):
    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)
    if player_choice == computer_choice:
        result = "It's a Tie!"
    elif (player_choice == 'Rock' and computer_choice == 'Scissors') or \
         (player_choice == 'Scissors' and computer_choice == 'Paper') or \
         (player_choice == 'Paper' and computer_choice == 'Rock'):
        result = "You Win!"
    else:
        result = "You Lose!"

    result_label.config(text=f"Your Choice: {player_choice}\nComputer: {computer_choice}\nResult: {result}")

window = tk.Tk()
window.title("Rock-Paper-Scissors")
tk.Label(window, text="Choose your move:").pack()
tk.Button(window, text="Rock", command=lambda: play("Rock")).pack()
tk.Button(window, text="Paper", command=lambda: play("Paper")).pack()
tk.Button(window, text="Scissors", command=lambda: play("Scissors")).pack()
result_label = tk.Label(window, text="", font=("Arial", 12))
result_label.pack()
window.mainloop()

