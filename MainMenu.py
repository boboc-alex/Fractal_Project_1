import tkinter as tk
from tkinter import messagebox
from GameApp import run_game # Import the Hexagon game script (ensure GameApp.py is in the same directory)

class MainMenuApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Main Menu")
        self.root.geometry("800x600")
        
        # Title label
        title_label = tk.Label(root, text="A BEE'S ADVENTURE", font=("Arial", 24, "bold"))
        title_label.pack(pady=20)
        
        # Start the Game Button
        start_button = tk.Button(root, text="Start the Game", font=("Arial", 14), width=20, command=self.start_game)
        start_button.pack(pady=10)
        
        # Options Button
        options_button = tk.Button(root, text="Options", font=("Arial", 14), width=20, command=self.open_options)
        options_button.pack(pady=10)
        
        # Achievements Button
        achievements_button = tk.Button(root, text="Achievements", font=("Arial", 14), width=20, command=self.view_achievements)
        achievements_button.pack(pady=10)
        
        # Quit the Game Button
        quit_button = tk.Button(root, text="Quit the Game", font=("Arial", 14), width=20, command=self.quit_game)
        quit_button.pack(pady=10)

    # Methods for button actions
    def start_game(self):
        self.root.destroy()  # Close the main menu
        run_game()

    def open_options(self):
        messagebox.showinfo("Options", "Opening options...")
        # Add logic to open the options menu here

    def view_achievements(self):
        messagebox.showinfo("Achievements", "Viewing achievements...")
        # Add logic to display achievements here

    def quit_game(self):
        answer = messagebox.askyesno("Quit the Game", "Are you sure you want to quit?")
        if answer:
            self.root.destroy()

# Main Tkinter loop
if __name__ == "__main__":
    root = tk.Tk()
    app = MainMenuApp(root)
    root.mainloop()
