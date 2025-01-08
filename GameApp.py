import pygame
import math
from pygame_widgets import slider

# Function to run the game (called from the main menu)

def run_game():

    # Initialize Pygame
    pygame.init()

    # Screen Settings
    SCREEN_WIDTH = 1200
    SCREEN_HEIGHT = 800
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("BEE GAME")

    # Colors
    DARK_ORANGE = (255, 140, 0)
    YELLOW = (255, 255, 0)
    RED = (255, 0, 0)
    PINK = (255, 105, 180)
    DARK_GREEN = (0, 100, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    LIGHT_BLUE = (173, 216, 230)
    BACKGROUND_COLOR = YELLOW

    # Character Settings
    CHARACTER_WIDTH = 100
    CHARACTER_HEIGHT = 100
    VELOCITY = 5
    CHARACTER_IMAGE_PATH = r"C:\Users\User\work program\uber\HousingAnywhere[infa]\Fractal_Project_1\Assets\BEE_char.png"  # Replace with your image path
    character_image = pygame.image.load(CHARACTER_IMAGE_PATH)
    character_image = pygame.transform.scale(character_image, (CHARACTER_WIDTH, CHARACTER_HEIGHT))

    # Zoom Settings
    ZOOM_FACTOR = 1.0
    ZOOM_INCREMENT = 0.01
    MAX_ZOOM = 5.0
    MIN_ZOOM = 0.5

    # Game Variables
    score = 0
    font = pygame.font.SysFont(None, 36)
    COLOR_TABLE = (DARK_ORANGE, YELLOW)  # Default color

    # Clock
    clock = pygame.time.Clock()

    # Player Class
    class Player(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = character_image
            self.rect = self.image.get_rect()
            self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            self.speed = VELOCITY

        def update(self, keys):
            if keys[pygame.K_LEFT]:
                self.rect.x -= self.speed
            if keys[pygame.K_RIGHT]:
                self.rect.x += self.speed
            if keys[pygame.K_UP]:
                self.rect.y -= self.speed
            if keys[pygame.K_DOWN]:
                self.rect.y += self.speed

    # Collectible Class
    COLLECTIBLE_IMAGE_PATH = r"C:\Users\User\work program\uber\HousingAnywhere[infa]\Fractal_Project_1\Assets\HONEY.png"  # Replace with your image path
    collectible_image = pygame.image.load(COLLECTIBLE_IMAGE_PATH)
    collectible_image = pygame.transform.scale(collectible_image, (30, 30))

    class Collectible(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = collectible_image
            self.rect = self.image.get_rect()

    # Hexagon Functions
    def calculate_hexagon(center_x, center_y, radius, rotation=0):
        points = []
        for i in range(6):
            angle = math.radians(60 * i + rotation)
            x = center_x + radius * math.cos(angle)
            y = center_y + radius * math.sin(angle)
            points.append((x, y))
        return points

    def point_in_polygon(x, y, polygon):
        n = len(polygon)
        inside = False
        px, py = polygon[0]
        for i in range(1, n + 1):
            sx, sy = polygon[i % n]
            if ((sy > y) != (py > y)) and (x < (sx - px) * (y - py) / (sy - py) + px):
                inside = not inside
            px, py = sx, sy
        return inside

    def draw_sierpinski_hexagon(center_x, center_y, radius, depth, rotation=0):
        if depth == 0:
            return

        start_color, end_color = COLOR_TABLE
        C1 = start_color[0] - int((start_color[0] - end_color[0]) * (depth / max_depth))
        C2 = start_color[1] - int((start_color[1] - end_color[1]) * (depth / max_depth))
        C3 = start_color[2] - int((start_color[2] - end_color[2]) * (depth / max_depth))
        current_color = (C1, C2, C3)

        points = calculate_hexagon(center_x, center_y, radius, rotation)
        pygame.draw.polygon(screen, current_color, points, 0)

        inner_radius = radius / 3
        distance_to_center = (2 * radius) / 3

        for i in range(6):
            angle = math.radians(60 * i + rotation)
            child_center_x = center_x + distance_to_center * math.cos(angle)
            child_center_y = center_y + distance_to_center * math.sin(angle)
            draw_sierpinski_hexagon(child_center_x, child_center_y, inner_radius, depth - 1, rotation)

        draw_sierpinski_hexagon(center_x, center_y, inner_radius, depth - 1, rotation)

    # Fractal Settings
    rotation_angle = 90
    max_depth = 3
    center_x = SCREEN_WIDTH // 2
    center_y = SCREEN_HEIGHT // 2
    base_radius = 300
    hexagons = []
    inner_hexagon_centers = []

    # Populate Hexagons and Centers
    def populate_hexagons(center_x, center_y, radius, depth, rotation=0):
        if depth == 0:
            return
        points = calculate_hexagon(center_x, center_y, radius, rotation)
        hexagons.append(points)

        if depth == 1:
            inner_hexagon_centers.append((center_x, center_y))

        inner_radius = radius / 3
        distance_to_center = (2 * radius) / 3
        for i in range(6):
            angle = math.radians(60 * i + rotation)
            child_center_x = center_x + distance_to_center * math.cos(angle)
            child_center_y = center_y + distance_to_center * math.sin(angle)
            populate_hexagons(child_center_x, child_center_y, inner_radius, depth - 1, rotation)
        populate_hexagons(center_x, center_y, inner_radius, depth - 1, rotation)

    populate_hexagons(center_x, center_y, base_radius, max_depth, rotation_angle)

    # Initialize Sprites
    player = Player()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    collectibles = pygame.sprite.Group()
    for center in inner_hexagon_centers:
        collectible = Collectible()
        collectible.rect.center = center
        all_sprites.add(collectible)
        collectibles.add(collectible)

    # Add Slider class after the imports and before run_game()
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

    # Add after the game variables initialization:
    slider_width, slider_height = 200, 20
    slider_pos = (SCREEN_WIDTH - slider_width // 2 - 20, SCREEN_HEIGHT - slider_height // 2 - 20)
    zoom_slider = Slider(slider_pos, (slider_width, slider_height), 1.0, MIN_ZOOM, MAX_ZOOM)

    # Main Game Loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            zoom_slider.handle_event(event)  # Add this line to handle slider events

        # Player Movement
        keys_pressed = pygame.key.get_pressed()
        dx, dy = 0, 0
        if keys_pressed[pygame.K_LEFT]:
            dx = -player.speed
        elif keys_pressed[pygame.K_RIGHT]:
            dx = player.speed
        elif keys_pressed[pygame.K_UP]:
            dy = -player.speed
        elif keys_pressed[pygame.K_DOWN]:
            dy = player.speed

        new_x = player.rect.x + dx
        new_y = player.rect.y + dy

        for hex_points in hexagons:
            if point_in_polygon(new_x + 25, new_y + 25, hex_points):
                player.rect.x = new_x
                player.rect.y = new_y
                break

        # Change Color Scheme
        if keys_pressed[pygame.K_0]:
            COLOR_TABLE = (DARK_ORANGE, YELLOW)
        elif keys_pressed[pygame.K_1]:
            COLOR_TABLE = (BLUE, LIGHT_BLUE)
        elif keys_pressed[pygame.K_2]:
            COLOR_TABLE = (RED, PINK)
        elif keys_pressed[pygame.K_3]:
            COLOR_TABLE = (DARK_GREEN, GREEN)

        # Zoom Controls
        ZOOM_FACTOR = zoom_slider.get_value()

        # Collectibles Interaction
        collected_items = pygame.sprite.spritecollide(player, collectibles, True)
        for _ in collected_items:
            score += 1

        if len(collectibles) == 0:
            print("Game Over! You collected all items.")
            running = False

        # Draw Everything
        screen.fill(BACKGROUND_COLOR)
        draw_sierpinski_hexagon(center_x, center_y, base_radius * ZOOM_FACTOR, max_depth, rotation_angle)
        all_sprites.draw(screen)
        score_text = font.render(f"Score: {score}", True, (0, 0, 0))
        screen.blit(score_text, (10, 10))

        zoom_slider.render(screen)

        pygame.display.flip()
        clock.tick(60)
        

    pygame.quit()



# Ensure the game only runs when GameApp.py is executed directly

if __name__ == "__main__":
    run_game()

