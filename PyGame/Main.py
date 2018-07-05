import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))
myImage = pygame.image.load("image.jpg").convert()
myImage = pygame.transform.scale(myImage, (100, 100))
bg_color =000000
x = y = 100
loop = True
while loop:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                loop = False
            elif event.key == pygame.K_RIGHT:
                x += 10
            elif event.key == pygame.K_LEFT:
                x -= 10
            elif event.key == pygame.K_UP:
                y -= 10
            elif event.key == pygame.K_DOWN:
                y += 10
    screen.fill(bg_color)
    screen.blit(myImage, (x, y))
    pygame.display.flip()
