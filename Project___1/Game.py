import pygame
import math
pygame.init()

# CREATING THE SCREEN
screen_width = 1100  
screen_height = 800  
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sierpinski Hexagon Fractal")  

# COLOURS
dark_orange = (255, 140, 0)  
yellow = (255, 255, 0)  
background_color = yellow  

# CHARACTER 
character_width = 100
character_height = 100
vel = 5
image_path = r"C:\Users\Asus\Downloads\BEE_char.png"  # Replace with your image path    # Load the character image
character_image = pygame.image.load(image_path)
character_image = pygame.transform.scale(character_image, (character_width, character_height))  # Scale image to fit character size


# ZOOM 
zoom_FIRST = 1.0  # Starting zoom factor (1.0 means no zoom, first version)
zoom_LEVEL = 0.01  # Zoom level value
max_zoom = 5.0  
min_zoom = 0.5  


# Function to calculate the points of a hexagon
def calculate_hexagon(center_x, center_y, radius, rotation=0):
    points = []  # To store the six vertices of the hexagon
    for i in range(6):  
        angle = math.radians(60 * i + rotation)  # Calculate the angle for each vertex
        x = center_x + radius * math.cos(angle)  
        y = center_y + radius * math.sin(angle)  
        points.append((x, y))  # Add the vertex to the list
    return points

# Recursive function to draw the Sierpiński hexagon
def draw_sierpinski_hexagon(center_x, center_y, radius, depth, rotation=0):

    if depth == 0:  # Base case
        return

    # Calculate color based on depth (closer to yellow at deeper levels)
    C1 = dark_orange[0] - int((dark_orange[0] - yellow[0]) * (depth / max_depth))
    C2 = dark_orange[1] - int((dark_orange[1] - yellow[1]) * (depth / max_depth))
    C3 = dark_orange[2] - int((dark_orange[2] - yellow[2]) * (depth / max_depth))
    current_color = (C1, C2, C3)

    # Draw the main hexagon
    points = calculate_hexagon(center_x, center_y, radius, rotation)
    pygame.draw.polygon(screen, current_color, points, 0)  # 0 = HEXAGON FILL

    # Size and position for inner hexagons
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

running = True
rotation_angle = 90  # (The shape we want actually)
max_depth = 4  # LEVEL OF THE FRACTAL ( make it max 5 for now, otherwise its lagging)

# Center and radius of the fractal
center_x = screen_width // 2
center_y = screen_height // 2
base_radius = 300

#Draw character on middle of the screen
char_locx = center_x - character_width // 2
char_locy = center_y - character_height // 2


# Main loop to keep the window open and visualize fractal
running = True
while running:
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            running = False  

    # Character Movements
    keys_pressed = pygame.key.get_pressed()  # Check for key presses
    if keys_pressed[pygame.K_LEFT] and char_locx > vel:
        char_locx -= vel
    if keys_pressed[pygame.K_RIGHT] and char_locx < 1100 - character_width - vel:
        char_locx += vel
    if keys_pressed[pygame.K_UP] and char_locy > vel :
        char_locy -= vel
    if keys_pressed[pygame.K_DOWN] and char_locy < 800 - character_height - vel:
        char_locy += vel


    # Zoom in and out with keyboard
    keys = pygame.key.get_pressed()
    if  keys[pygame.K_KP_PLUS]:   #    Numpad +
        if zoom_FIRST < max_zoom:
            zoom_FIRST += zoom_LEVEL
    if  keys[pygame.K_KP_MINUS]:  #    Numpad -
        if zoom_FIRST > min_zoom:
            zoom_FIRST -= zoom_LEVEL

    screen.fill(background_color)

    # Apply zoom factor to the radius
    radius = base_radius * zoom_FIRST
    

    # Draw the Sierpiński hexagon
    draw_sierpinski_hexagon(center_x, center_y, radius, max_depth, rotation_angle) 

    # Draw the character
    screen.blit(character_image, (char_locx, char_locy))  # Draw the character image at the new position
    
    pygame.display.update()
  
pygame.quit()
    
