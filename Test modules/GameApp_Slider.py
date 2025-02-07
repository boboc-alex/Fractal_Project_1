# Import necessary libraries
import pygame
import math
from pygame_widgets import slider


class Slider():
        def __init__(self, pos: tuple, size: tuple, inital_val: float, min_val: float, max_val: float):
            self.pos = pos
            self.size = size
            self.slider_left_pos = self.pos[0] - (size[0]//2)
            self.slider_right_pos = self.pos[0] + (size[0]//2)
            self.slider_top_pos = self.pos[1] - (size[1]//2)
                
            self.min_val = min_val
            self.max_val = max_val
            self.dragging = False
            
            

            #since button is not 0 pixels wide, it must be offset by half the width
            inital_pixal_val = (self.size[0] * (inital_val - self.min_val)) / (self.max_val - self.min_val)
            self.button_rect = pygame.Rect(self.slider_left_pos + inital_pixal_val - 5, self.slider_top_pos, 10, self.size[1])
        
        def render(self, screen):
            pygame.draw.rect(screen, "orange", (self.slider_left_pos, self.slider_top_pos, self.size[0], self.size[1]))
            pygame.draw.rect(screen, "yellow", self.button_rect)

        def handle_event(self, event):
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.button_rect.collidepoint(event.pos):
                    self.dragging = True
            elif event.type == pygame.MOUSEBUTTONUP:
                self.dragging = False
            elif event.type == pygame.MOUSEMOTION:
                if self.dragging:
                    new_x = min(max(event.pos[0], self.slider_left_pos), self.slider_right_pos)
                    self.button_rect.x = new_x
        
        def get_value(self):
            slider_range = self.slider_right_pos - self.slider_left_pos
            relative_x = self.button_rect.x - self.slider_left_pos
            return self.min_val + ((relative_x / slider_range) * (self.max_val - self.min_val))
    




# Function to run the game (called from the main menu)
def run_game():
    pygame.init()
    
    #mouse position for slider
    mouse_pos = pygame.mouse.get_pos
    mouse = pygame.mouse.get_pressed
    

    # CREATING THE SCREEN
    screen_width = 1000  
    screen_height =600  
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Sierpinski Hexagon Fractal")  

    
    # COLOURS
    dark_orange = (255, 140, 0)  
    yellow = (255, 255, 0)  
    background_color = yellow  

    # CHARACTER
    velocity = 2
    class Player():
        def __init__(self,x,y):
            
            image_path = r"C:\Users\boboc\Downloads\placeholder.jpg"  # Replace with your image path    
            self.character_image = pygame.image.load(image_path)  # Load the character image
            self.character_image = pygame.transform.scale(self.character_image, (60, 80))  # Scale image to fit character size
            self.rect = self.character_image.get_rect()
            self.rect.x = x
            self.rect.y = y

    # ZOOM 
    zoom_FIRST = 1.0  # Starting zoom factor (1.0 means no zoom, first version)
    zoom_LEVEL = 0.01  # Zoom level value
    max_zoom = 5.0  
    min_zoom = 0.5  

    # Slider initalization
    slider_width, slider_height = 200, 20
    slider_pos = (screen_width - slider_width // 2 - 20, screen_height - slider_height // 2 - 20)
    zoom_slider = Slider(slider_pos, (slider_width, slider_height), 1.0, 0.5, 5.0)

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
    char_loc = Player((center_x-40), (center_y-60))


    # Main loop to keep the window open and visualize fractal
    running = True
    while running:
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:  
                running = False  
            zoom_slider.handle_event(event)

        zoom_FIRST = zoom_slider.get_value()

        # Character Movements
        keys_pressed = pygame.key.get_pressed()  # Check for key presses
        if keys_pressed[pygame.K_LEFT] and char_loc.rect.x > velocity:
            char_loc.rect.x -= velocity
        if keys_pressed[pygame.K_RIGHT] and char_loc.rect.x < screen_width - char_loc.rect.width - velocity:
            char_loc.rect.x += velocity
        if keys_pressed[pygame.K_UP] and char_loc.rect.y > velocity:
            char_loc.rect.y -= velocity
        if keys_pressed[pygame.K_DOWN] and char_loc.rect.y < screen_height - char_loc.rect.height - velocity:
            char_loc.rect.y += velocity

        # Zoom in and out with keyboard
        # if keys_pressed[pygame.K_1]:   # Numpad +
        #     if zoom_FIRST < max_zoom:
        #         zoom_FIRST += zoom_LEVEL
        # if keys_pressed[pygame.K_2]:  # Numpad -
        #     if zoom_FIRST > min_zoom:
        #         zoom_FIRST -= zoom_LEVEL

        screen.fill(background_color)


        # Apply zoom factor to the radius
        radius = base_radius * zoom_FIRST

        # Scale the character image based on zoom
        scaled_character = pygame.transform.scale(char_loc.character_image, (int(60 * zoom_FIRST), int(80 * zoom_FIRST)))               #### NOTE THAT 
        scaled_rect = scaled_character.get_rect(center=(char_loc.rect.center))

        # Draw the Sierpiński hexagon
        draw_sierpinski_hexagon(center_x, center_y, radius, max_depth, rotation_angle) 

        # Draw the scaled character
        screen.blit(scaled_character, scaled_rect)

        #Draw the slider
        zoom_slider.render(screen)
        pygame.display.update()
    
    pygame.quit()

# Ensure the game only runs when GameApp.py is executed directly
if __name__ == "__main__":
    run_game()
