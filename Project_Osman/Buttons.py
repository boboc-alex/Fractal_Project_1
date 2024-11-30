import pygame


pygame.init()
screen_width = 900
screen_height = 700

main_screen = (screen_width, screen_height)
screen = pygame.display.set_mode(main_screen)     
pygame.display.set_caption("Buttons")

#Loading button images
start_img = pygame.image.load(r"C:\Users\Asus\Downloads\start.button.jpg").convert_alpha
exit_img = pygame.image.load(r"C:\Users\Asus\Downloads\exit.button.jpg").convert_alpha




run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    pygame.display.update()

pygame.quit()
