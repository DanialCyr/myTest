import random, os.path
import pygame


SCREEN_RECT = pygame.rect.Rect(0,0,480,700)

pygame.init()
screen = pygame.display.set_mode((SCREEN_RECT.width,SCREEN_RECT.height))
clock = pygame.time.Clock()

bg = pygame.image.load("./images/background.png")
triangle = pygame.image.load("./images/resume_nor.png")
triangle_rect = triangle.get_rect()
print(f"triangle_rect = {triangle_rect}")
speed = [100,50]
screen.blit(bg,(0,0))
screen.blit(triangle,(0,0))

while True:
    clock.tick(40)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if triangle_rect.left < 0 or triangle_rect.right > SCREEN_RECT.width:
        speed[0] = -speed[0]
    if triangle_rect.top < 0 or triangle_rect.bottom > SCREEN_RECT.height:
        speed[1] = -speed[1]
    triangle_rect = triangle_rect.move(speed)
    screen.blit(bg, (0, 0))
    screen.blit(triangle,triangle_rect)
    print(f"triangle_rect = {triangle_rect}")

    pygame.display.update()


pygame.quit()

