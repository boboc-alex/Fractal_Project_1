import os
import cv2
import tkinter as tk
from tkinter import messagebox
from tkinter import *
from GameApp import run_game  # Import the Hexagon game script (ensure GameApp.py is in the same directory)

# VIDEO BACKGROUND
class VideoBackground:
    def __init__(self, video_path, width, height):
        self.video_path = video_path
        self.width = width
        self.height = height
        self.cap = cv2.VideoCapture(video_path)

    def play_video(self, background_label):
        ret, frame = self.cap.read()
        if not ret:  # Loop the video
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            ret, frame = self.cap.read()

        if ret:
            frame = cv2.cvtColor(frame, 0)  # Convert color to RGB ( 0 for origin color)
            frame = cv2.resize(frame, (self.width, self.height))
            frame_image = tk.PhotoImage(data=cv2.imencode('.png', frame)[1].tobytes())
            background_label.config(image=frame_image)
            background_label.image = frame_image

# Main Menu Class
class MainMenuApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Main Menu")
        self.root.geometry("800x600")
        self.root.configure(background="yellow")

        # Initialize video background
        assets_folder = "Assets"
        video_path = os.path.join(assets_folder, "bee_video.mp4")
        self.video_bg = VideoBackground(video_path, 800, 600)
        

        # Background label for video
        self.bg_label = tk.Label(root)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.bg_label.lower()  # Ensure video background is behind other widgets

        self.update_background()

        # Title label with box
        title_canvas = tk.Canvas(root, width=400, height=150, bg="orange", highlightthickness=1, highlightbackground="black")
        title_canvas.create_text(200, 75, text="A Bee's Adventure", fill="black", font=("Arial", 24, "bold"))
        title_canvas.pack(pady=20)

        # Start the Game Button
        start_button = tk.Button(root, text="Play Game", font=("Arial", 14), width=20, command=self.open_level_selection, bg="orange")
        start_button.pack(pady=10)

        # Options Button
        options_button = tk.Button(root, text="Options", font=("Arial", 14), width=20, command=self.open_options, bg= "orange")
        options_button.pack(pady=10)
        
        # Achievements Button
        achievements_button = tk.Button(root, text="Achievements", font=("Arial", 14), width=20, command=self.view_achievements, bg= "orange")
        achievements_button.pack(pady=10)
        
        # Quit Button
        quit_button = tk.Button(root, text="Quit", font=("Arial", 14), width=20, command=self.quit_game, bg="orange")
        quit_button.pack(pady=10)

    def update_background(self):
        self.video_bg.play_video(self.bg_label)
        self.root.after(5, self.update_background)  # Backgroud video speed

    def open_options(self):
        messagebox.showinfo("Options", "Opening options...")
        # Add logic to open the options menu here

    def view_achievements(self):
        messagebox.showinfo("Achievements", "Viewing achievements...")
        # Add logic to display achievements here

    def open_level_selection(self):
        self.root.destroy()
        level_selection_menu()

    def quit_game(self):
        answer = messagebox.askyesno("Quit", "Are you sure you want to quit?")
        if answer:
            self.root.destroy()

# Level Selection Menu
def level_selection_menu():
    level_root = tk.Tk()
    level_root.title("Select Level")
    level_root.geometry("800x600")
    level_root.configure(background="yellow")

    # Initialize video background
    assets_folder = "Assets"
    video_path = os.path.join(assets_folder, "bee_video.mp4")
    video_bg = VideoBackground(video_path, 800, 600)
    bg_label = tk.Label(level_root)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.lower()

    def update_background():
        video_bg.play_video(bg_label)
        level_root.after(5, update_background)

    update_background()

    # Title Label
    title_label = tk.Label(level_root, text="Select a Level", font=("Arial", 24, "bold"), bg="orange")
    title_label.pack(pady=20)

    # Level Buttons
    tk.Button(level_root, text="Level 1", font=("Arial", 14), width=20, command=lambda: start_game(level_root, 2), bg="orange").pack(pady=10)
    tk.Button(level_root, text="Level 2", font=("Arial", 14), width=20, command=lambda: start_game(level_root, 3), bg="orange").pack(pady=10)
    tk.Button(level_root, text="Level 3", font=("Arial", 14), width=20, command=lambda: start_game(level_root, 4), bg="orange").pack(pady=10)

    level_root.mainloop()

# Start Game Function
def start_game(level_root, depth):
    level_root.destroy()
    run_game(depth)  # Pass the depth to the GameApp run_game function

# Main Tkinter Loop
if __name__ == "__main__":
    root = tk.Tk()
    app = MainMenuApp(root)
    root.mainloop()

