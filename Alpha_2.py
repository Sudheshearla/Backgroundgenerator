import tkinter as tk
import random

# Define a list of background colors
background_colors = ["#FF5733", "#33FF57", "#5733FF", "#33A2FF", "#FF33A2", "#A2FF33", "#33FFA2", "#A233FF", "#FFA233"]

# Create a function to change the background color
def change_background_color():
    random_color = random.choice(background_colors)
    root.configure(bg=random_color)

# Create a Tkinter window
root = tk.Tk()
root.title("Background Generator")

# Create a button to change the background color
change_button = tk.Button(root, text="Change Background", command=change_background_color)
change_button.pack(pady=20)

# Set an initial background color
root.configure(bg=random.choice(background_colors))

# Run the Tkinter main loop
root.mainloop()
