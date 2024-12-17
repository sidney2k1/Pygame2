import pygame
pygame.init()
screen=pygame.display.set_mode((300,400))
screen.fill((255,255,255))
green=(0,255,0)
pygame.draw.circle(screen,green,(200,100),40)
pygame.draw.circle(screen,green,(100,100),40,3)
pygame.draw.rect(screen,(0,125,125),pygame.Rect(100,200,100,60))
pygame.display.update()
done=True
while done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=False
pygame.quit()


