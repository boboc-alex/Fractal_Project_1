import pygame


pygame.init()
screen_width = 900
screen_height = 700

# Create the Screen
main_screen = (screen_width, screen_height)
screen = pygame.display.set_mode(main_screen)     
pygame.display.set_caption("Beehive Menu")

BACKGROUND = pygame.image.load(r"C:\Users\Asus\Downloads\beeimage.jpg")
BACKGROUND = pygame.transform.smoothscale(BACKGROUND, (screen_width, screen_height))

#game variables
game_paused = False

TEXT_COLOR =(0, 0, 0, 255)
font = pygame.font.SysFont("arialblack", 40) #First one is the color and second is the font size
#define colors
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img,(x,y))
#Calculating text's center distances
centered_x = (screen_width / 2)
centered_y = (screen_height/ 2) 

# Game Loop
status = True
while status:

    # Draw the background
    screen.blit(BACKGROUND, (0, 0)) 
    #check if game is paused
    if game_paused:
        draw_text("Game Paused", font, TEXT_COLOR, centered_x, centered_y)
    else:
        draw_text("Press space to pause", font, TEXT_COLOR, centered_x, centered_y)
        
        #display menu
    



    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_paused = not game_paused  # Toggle the pause state

        if event.type == pygame.QUIT:
            status = False

    # Update Display
    pygame.display.update()

pygame.quit()

