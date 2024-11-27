import pygame
pygame.init()
screen=pygame.display.set_mode((400,400))
screen.fill((255,255,255))
green=(0,255,0)
pygame.draw.circle(screen,green,(300,100),50)
pygame.draw.circle(screen,green,(100,100),50,3)
pygame.display.update()
done=True
while done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=False
pygame.quit()