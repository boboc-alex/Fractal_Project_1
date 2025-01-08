import cv2
import tkinter as tk
from tkinter import messagebox
from tkinter import *
from GameApp import run_game  # Import the Hexagon game script (ensure GameApp.py is in the same directory)

# VIDEO BACKGROUD
class VideoBackground:
    def __init__(self, video_path, width, height):
        self.video_path = video_path
        self.width = width
        self.height = height
        self.cap = cv2.VideoCapture(video_path)

    def play_video(self, back_ground_label):
        ret, frame = self.cap.read()
        if not ret:  # Loop the video
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            ret, frame = self.cap.read()

        elif ret:
            frame = cv2.cvtColor(frame, 0)  # 0 for orgin color 
            frame = cv2.resize(frame, (self.width, self.height))
            frame_image = tk.PhotoImage(data=cv2.imencode('.png', frame)[1].tobytes())
            back_ground_label.config(image=frame_image)
            back_ground_label.image = frame_image

# Main Menu Class
class MainMenuApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Main Menu")
        self.root.geometry("800x600")
        root.configure(background='yellow')

        # Initialize video background
        self.video_bg = VideoBackground(r"C:\Users\User\work program\uber\HousingAnywhere[infa]\Fractal_Project_1\Assets\bee_video.mp4", 800, 600)

        # Background label for video
        self.bg_label = tk.Label(root)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.bg_label.lower()  # Ensure video background is behind other widgets

        self.update_background()

        #Title label with box
        rectangle = Canvas(root, width=400, height=150, bg="orange", highlightthickness=1, highlightbackground="black")
        rectangle.create_text(200, 75, text="A Bee's Adventure", fill="black", font=("Arial", 24, "bold"),)
        rectangle.pack(pady=20)  # Add the canvas to the layout
        
    
        # Start the Game Button
        start_button = tk.Button(root, text="Play Game", font=("Arial", 14), width=20, command=self.start_game, bg = "orange")
        start_button.pack(pady=10)
        
        # Options Button
        options_button = tk.Button(root, text="Options", font=("Arial", 14), width=20, command=self.open_options, bg= "orange")
        options_button.pack(pady=10)
        
        # Achievements Button
        achievements_button = tk.Button(root, text="Achievements", font=("Arial", 14), width=20, command=self.view_achievements, bg= "orange")
        achievements_button.pack(pady=10)
        
        # Quit the Game Button
        quit_button = tk.Button(root, text="Quit", font=("Arial", 14), width=20, command=self.quit_game, bg= "orange")
        quit_button.pack(pady=10)

    def update_background(self):
        self.video_bg.play_video(self.bg_label)
        self.root.after(15, self.update_background)  # Increased FPS to 60 FPS (15 ms interval)

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
