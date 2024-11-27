import pygame
def main():
    pygame.init()
    screenwidth,screenheight=100,100
    screen=pygame.display.set_mode((screenwidth,screenheight))
    pygame.display.set_caption("Color changing sprite")
    colors={"red":pygame.Color("red"),"yellow":pygame.Color("yellow"),"green":pygame.Color("green"),"blue":pygame.Color("blue"),"white":pygame.Color("white")}
    currentcolor=colors["white"]
    x,y=30,30
    spritewidth,spriteheight=60,60
    clock=pygame.time.Clock()
    done=False
    while not done:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                done=True
        pressed=pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:x-=3
        elif pressed[pygame.K_RIGHT]:x+=3
        elif pressed[pygame.K_UP]:y-=3
        elif pressed[pygame.K_DOWN]:y+=3
        x=min(max(0,x),screenwidth-spritewidth)
        y=min(max(0,y),screenheight-spriteheight)
        if x==0 :currentcolor=colors["blue"]
        elif x==screenwidth-spritewidth:currentcolor=colors["yellow"]
        elif y==0:currentcolor=colors["red"]
        elif y==screenheight-spriteheight:currentcolor=colors["green"]
        else:
            currentcolor=colors["white"]
        screen.fill((0,0,0))
        pygame.draw.rect(screen,currentcolor,(x,y,spritewidth,spriteheight))
        pygame.display.flip()
        clock.tick(90)
    pygame.quit()
if __name__=="__main__":
    main()

