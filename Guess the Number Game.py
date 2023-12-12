from tkinter import *
import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Function to check the player's guess
def check_guess():
    guess = int(number.get())
    if guess == secret_number:
        result_label.config(text="Congratulations! You guessed it!")
    elif guess < secret_number:
        result_label.config(text="Try a higher number.")
    else:
        result_label.config(text="Try a lower number.")

# Create the main window
window = Tk()
window.title("Guess the Number")

# Create a label and entry for guessing
Label(window, text="Guess the number (1-100):").pack()
number = Entry(window)
number.pack()

# Create a button to check the guess
Button(window, text="Check Guess", command=check_guess).pack()

# Create a label for the result
result_label = Label(window, text="")
result_label.pack()

# Start the Tkinter main loop
window.mainloop()
