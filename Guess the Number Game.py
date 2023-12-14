from tkinter import *
import random

# Here i want the programm to generate a random number between 1 and 100
secret = random.randint(1, 100)

# here i built a function to check the player's guess
def check_guess():
    guess = int(number.get())
    if guess == secret:
        result_label.config(text="Congratulations! You guessed it!")
    elif guess < secret:
        result_label.config(text="Try a higher number.")
    else:
        result_label.config(text="Try a lower number.")

# here i create the main window
window = Tk()
window.title("Guess the Number")

# here i create a label and entry for guessing
Label(window, text="Guess the number (1-100):").pack()
number = Entry(window)
number.pack()

# here i create a button to check the guess
Button(window, text="Check Guess", command=check_guess).pack()

# here i create a label for the result
result_label = Label(window, text="")
result_label.pack()

# this to start the Tkinter main loop
window.mainloop()
