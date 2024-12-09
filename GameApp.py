# Import necessary libraries
import pygame
import math

# Function to run the game (called from the main menu)
def run_game():
    # Initialize Pygame
    pygame.init()

    # Screen dimensions
    screen_width = 1100  # Width of the window
    screen_height = 800  # Height of the window

    # Create the screen
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Sierpiński Hexagon Fractal")  # Set the window title

    # Colors
    dark_orange = (255, 140, 0)  # Base color (RGB for dark orange)
    yellow = (255, 255, 0)  # Background color (RGB for yellow)
    background_color = yellow  # Assign background color

    # Fill the background
    screen.fill(background_color)

    # Function to calculate the points of a hexagon
    def calculate_hexagon(center_x, center_y, radius, rotation=0):
        points = []
        for i in range(6):
            angle = math.radians(60 * i + rotation)
            x = center_x + radius * math.cos(angle)
            y = center_y + radius * math.sin(angle)
            points.append((x, y))
        return points

    # Recursive function to draw the Sierpiński hexagon
    def draw_sierpinski_hexagon(center_x, center_y, radius, depth, rotation=0):
        if depth == 0:
            return

        # Calculate color based on depth
        r = dark_orange[0] - int((dark_orange[0] - yellow[0]) * (depth / max_depth))
        g = dark_orange[1] - int((dark_orange[1] - yellow[1]) * (depth / max_depth))
        b = dark_orange[2] - int((dark_orange[2] - yellow[2]) * (depth / max_depth))
        current_color = (r, g, b)

        # Draw the main hexagon
        points = calculate_hexagon(center_x, center_y, radius, rotation)
        pygame.draw.polygon(screen, current_color, points, 0)

        # Define the size and position for smaller hexagons
        inner_radius = radius / 3
        distance_to_center = (2 * radius) / 3

        # Recursively draw six smaller hexagons around the main one
        for i in range(6):
            angle = math.radians(60 * i + rotation)
            child_center_x = center_x + distance_to_center * math.cos(angle)
            child_center_y = center_y + distance_to_center * math.sin(angle)
            draw_sierpinski_hexagon(child_center_x, child_center_y, inner_radius, depth - 1, rotation)

        # Draw the central smaller hexagon
        draw_sierpinski_hexagon(center_x, center_y, inner_radius, depth - 1, rotation)

    # Main loop to keep the window open and animate the fractal
    running = True
    rotation_angle = 90
    max_depth = 4

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen before each frame
        screen.fill(background_color)

        # Center and radius of the largest hexagon
        center_x = screen_width // 2
        center_y = screen_height // 2
        radius = 300

        # Draw the Sierpiński hexagon
        draw_sierpinski_hexagon(center_x, center_y, radius, max_depth, rotation_angle)

        # Update the display to show the drawing
        pygame.display.update()

    # Quit Pygame
    pygame.quit()

# Ensure the game only runs when GameApp.py is executed directly
if __name__ == "__main__":
    run_game()
