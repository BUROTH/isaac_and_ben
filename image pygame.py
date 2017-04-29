import pygame, sys, time
speed=[0,0]
speed1=[-1,0]
size=width,height=1000,600
red=255,0,0
screen=pygame.display.set_mode(size)
screen.fill(red)
ball=pygame.image.load("C:/Users/isaac/Desktop/intro_ball.gif")
ball1=pygame.image.load("C:/Users/isaac/Desktop/intro_ball.gif")
ballrect=ball.get_rect()
ballrect1=ball1.get_rect()
ballrect = ballrect.move([50,50])
ballrect1 = ballrect1.move([1000,300])
def failing (rect1, rect2):
    d=abs(rect1.left-rect1.right)/2
    if ((abs(rect1.right-rect2.left)<d) or (abs(rect1.left-rect2.right)<d)) and ((abs(rect1.bottom-rect2.top)<d) or (abs(rect1.top-rect2.bottom)<d)):
        print ("failing")
        return True
while 1:
    if failing (ballrect, ballrect1):
        pygame.display.quit()
        sys.exit()
    screen.fill(red)
    screen.blit(ball, ballrect)
    screen.blit(ball1, ballrect1)
    pygame.display.flip()
    ballrect = ballrect.move(speed)
    ballrect1 = ballrect1.move(speed1)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect1.right < 0:
        ballrect1 = ballrect1.move([1000,0])
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
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

