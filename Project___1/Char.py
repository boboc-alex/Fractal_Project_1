import pygame

pygame.init()

CLOCK =  pygame.time.Clock()

width = 500
height = 500

win = pygame.display.set_mode((width, height)) 
pygame.display.set_caption("First Game!")

x = 50
y = 50
charter_width = 100
charter_height = 100
vel = 10


# Load the character image
image_path = r"C:\Users\Asus\Downloads\BEE_char.png"  # Replace with your image path
character_image = pygame.image.load(image_path)
character_image = pygame.transform.scale(character_image, (charter_width, charter_height))  # Scale image to fit character size

#game run
run = True
while run:
    pygame.time.delay(40)
    for event in pygame.event.get():  # Handling events
        if event.type == pygame.QUIT:
            run = False
    
    keys_pressed = pygame.key.get_pressed()  # Check for key presses
    if keys_pressed[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys_pressed[pygame.K_RIGHT] and x < 500 - charter_width - vel:
        x += vel
    if keys_pressed[pygame.K_UP] and y > vel :
        y -= vel
    if keys_pressed[pygame.K_DOWN] and y < 500 - charter_height - vel:
        y += vel



  # Update the screen
    win.fill((255,255,255))  # Background color
    win.blit(character_image, (x, y))  # Draw the character image at the new position
    pygame.display.update()

pygame.quit()
