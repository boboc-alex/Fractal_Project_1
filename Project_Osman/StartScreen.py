import pygame


pygame.init()
screen_width = 900
screen_height = 700



BACKGROUND = pygame.image.load(r"C:\Users\Asus\Downloads\beeimage.jpg")
BACKGROUND = pygame.transform.smoothscale(BACKGROUND, (screen_width, screen_height))

# Create the Screen
main_screen = (screen_width, screen_height)
screen = pygame.display.set_mode(main_screen)     
pygame.display.set_caption("Beehive Menu")



def main_menu():
    pygame.display.set_caption("Main Menu")
    screen.blit(BACKGROUND, (0 ,0))

    MOUSE_POSITION = pygame.mouse.get_pos()
    MENU_TEXT = 
    MENU_RECT = 









run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Update Display
    pygame.display.update()

pygame.quit()
