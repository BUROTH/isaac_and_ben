import pygame, sys, time
speed=[1,1]
speed1=[0,0]
size=width,height=1000,600
red=255,0,0
screen=pygame.display.set_mode(size)
#import pdb; pdb.set_trace()
screen.fill(red)
ball=pygame.image.load("C:/Users/isaac/Desktop/intro_ball.gif")
ball1=pygame.image.load("C:/Users/isaac/Desktop/intro_ball.gif")
ballrect=ball.get_rect()
#ballrect1=ball1.get_rect()
ballrect = ballrect.move([50,50])
#ballrect1 = ballrect1.move([50,50])
while 1:
    screen.fill(red)
    screen.blit(ball, ballrect)
    #screen.blit(ball1, ballrect1)
    pygame.display.flip()
    ballrect = ballrect.move(speed)
    #ballrect1 = ballrect1.move(speed1)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    #if ballrect1.left < 0 or ballrect1.right > width:
      #  speed1[0] = -speed1[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
    #if ballrect1.top < 0 or ballrect1.bottom > height:
        #speed1[1] = -speed1[1]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                        speed[0]=-1
                if event.key == pygame.K_w:
                        speed[1]=-1
                if event.key == pygame.K_d:
                        speed[0]=1
                if event.key == pygame.K_s:
                        speed[1]=1
        if event.type ==pygame.KEYUP:
                if event.key == pygame.K_a:
                         speed[0]=0
                if event.key == pygame.K_w:
                         speed[1]=0
                if event.key == pygame.K_d:
                         speed[0]=0
                if event.key == pygame.K_s:
                         speed[1]=0

