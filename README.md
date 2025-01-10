# **BEE's ADVENTURE**

## **An Interactive Fractal Exploration Game**
- Bee's Adventure is a Python-based puzzle game designed to make learning about fractals engaging and interactive.
- The game is centered around the Sierpinski Hexagon, where players control a bee, collect honey, and explore the depths of fractals.
- The project combines mathematical concepts, recursive logic, and game mechanics to create an educational and entertaining experience.

---

## **Features**

### **Interactive Gameplay:**
- Control a bee to navigate through fractal-based levels.
- Collect honey scattered across the hexagonal maze.

### **Fractal Visualization:**
- Explore the recursive structure of the Sierpinski Hexagon.
- Dynamic color gradients enhance the visual appeal of fractals.

### **Dynamic Menus:**
- A video-enhanced main menu and leveling menu using OpenCV and Tkinter.

### **Customization Options:**
- Zoom in and out of fractals using a slider.
- Change fractal colors dynamically.

### **Leveling System:**
- Progress through three increasingly complex levels, each with deeper recursive structures.

### **Gamification Elements:**
- Scoring system based on collected honey.

# **Step-by-Step Guide for Bee's Adventure**

---

## **1. Installation**

### Step 1: Install Pygame
- Open your terminal or command prompt.
- Run the following command to install Pygame:
  ```bash
  pip install pygame
-If you haven’t installed other libraries like OpenCV or pygame-widgets, install them as well:
  ```bash
  pip install opencv-python pygame-widgets
  ```

## 2. Prepare the Assets Folder

### Step 1: Create an Assets folder
-Inside the project directory, create a folder named Assets.
### Step 2: Add Required Images
-Place the following images into the Assets folder:
bal.jpg: Used as the background image.
BEE_char.png: Represents the bee character.
HONEY.png: Represents the collectible honey items.


## 3. Running the Game
### Step 1: Start the Game
-Run the following command:
  ```bash
  python game.py
  ```

## **4. Gameplay Instructions**

### **Controls:**
- **Arrow Keys:** Use the arrow keys to move the bee:
  - **Up Arrow:** Move up.
  - **Down Arrow:** Move down.
  - **Left Arrow:** Move left.
  - **Right Arrow:** Move right.

### **Zoom:**
- Use the slider at the bottom-right corner of the screen to zoom in and out of the fractal.

### **Change Fractal Colors:**
- Press the following keys to switch the fractal's color scheme:
  - `0`: Default colors (orange to yellow).
  - `1`: Blue to light blue.
  - `2`: Red to pink.
  - `3`: Dark green to green.

### **Objective:**
- Collect honey scattered across the hexagonal fractal by moving the bee over them.
- The game ends when all honey is collected.

Credits
This game is built using the Pygame library.
Custom assets and images are required to make the game visually appealing.
