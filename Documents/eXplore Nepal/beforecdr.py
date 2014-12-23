
def beforecdr():
    import pygame
    from pygame.locals import *
    import sys
    
    pygame.init()

    WINDOWWIDTH = 800
    WINDOWHEIGHT = 600
    screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT),pygame.FULLSCREEN)
    pygame.display.set_caption('Checkpoint Display')

    #lOADING ALPHABETS
    W=pygame.image.load("alphabets/w.png").convert()
    E=pygame.image.load("alphabets/e.png").convert()
    L=pygame.image.load("alphabets/l.png").convert()
    C=pygame.image.load("alphabets/c.png").convert()
    O=pygame.image.load("alphabets/o.png").convert()
    M=pygame.image.load("alphabets/m.png").convert()
    T=pygame.image.load("alphabets/t.png").convert()
    D=pygame.image.load("alphabets/d.png").convert()
    R=pygame.image.load("alphabets/r.png").convert()
    E=pygame.image.load("alphabets/e.png").convert()
    C=pygame.image.load("alphabets/c.png").convert()

    Logo=pygame.image.load("title.png").convert_alpha()

    walkl1=pygame.image.load("gameimages/crono_left_walk.000.gif").convert_alpha()
    walkr1=pygame.transform.flip(walkl1,True,False)
    walkl2=pygame.image.load("gameimages/crono_left_walk.001.gif").convert_alpha()
    walkr2=pygame.transform.flip(walkl2,True,False)
    walkl3=pygame.image.load("gameimages/crono_left_walk.002.gif").convert_alpha()
    walkr3=pygame.transform.flip(walkl3,True,False)
    walkl4=pygame.image.load("gameimages/crono_left_walk.003.gif").convert_alpha()
    walkr4=pygame.transform.flip(walkl4,True,False)
    walkl5=pygame.image.load("gameimages/crono_left_walk.004.gif").convert_alpha()
    walkr5=pygame.transform.flip(walkl5,True,False)
    walkl6=pygame.image.load("gameimages/crono_left_walk.005.gif").convert_alpha()
    walkr6=pygame.transform.flip(walkl6,True,False)


    BASICFONT = pygame.font.SysFont('Arial', 16)
    WHITE = (255, 255, 255)
    BGCOLOR = (100, 50, 50)

    
    x = 120 # x and y are the player's position
    y = 200

    instructionSurf = BASICFONT.render('Hold shift to run.', True, WHITE)
    instructionRect = instructionSurf.get_rect()
    instructionRect.bottomleft = (10, WINDOWHEIGHT - 10)

    running=False
    Flag=0
    rate=0.5
    flag=0
    while True:
        
        screen.fill((12,98,234))
        screen.blit(Logo,(175,10))
       
        
        for event in pygame.event.get(): # event handling loop

            # handle ending the program
            if event.type==QUIT:

                pygame.quit()

                sys.exit()

        





                if event.key in (K_LSHIFT, K_RSHIFT):

                    # player has started running

                    running = True



                



            elif event.type == KEYUP:

                if event.key in (K_LSHIFT, K_RSHIFT):

                    # player has stopped running

                    running = False


        if running== True:
            rate=1.5
        else:
            rate=0.5

        if Flag==0:
            done=walkr1                
        elif Flag== 1or Flag==-1:
            done=walkr2
            
        elif Flag==2 or Flag== -2:
            done=walkr3
             
        elif Flag==3 or Flag== -3:
            done=walkr4
             
        elif Flag==4 or Flag== -4:
            done=walkr5

        elif Flag==5 or Flag== -5:
            done=walkr6
            
        elif Flag>5 or Flag<-5:
            Flag=0

        if x>=200:
            flag=1
        if x>=280:
            flag=2
        if x>=360:
            flag=3
        if x>=440:
            flag=4
        if x>=520:
            flag=5
        if x>=600:
            flag=6
        if x>=680:
            flag=7
        if y>=300:
            if x>320:
                flag=8
            if x>400:
                flag=9
        if y>=380:
            if x>500:
                flag=10
            if x>580:
                flag=11
            if x>660:
                flag=12
        if x>760:
            y=y+100
            x=320
        
        screen.blit(done,(x,y))

        if (flag==1 or flag>=1):

            screen.blit(W,(120,200))

        if (flag==2 or flag>=2):

            screen.blit(E,(200,200))

        if (flag==3 or flag>=3):

            screen.blit(L,(280,200))

        if (flag==4 or flag>=4):

            screen.blit(C,(360,200))

        if (flag==5 or flag>=5):

            screen.blit(O,(440,200))

        if (flag==6 or flag>=6):

            screen.blit(M,(520,200))

        if (flag==7 or flag>=7):

            screen.blit(E,(600,200))

        if (flag==8 or flag>=8):

            screen.blit(T,(260,300))

        if (flag==9 or flag>=9):

            screen.blit(O,(340,300))

        if (flag==10 or flag>=10):

            screen.blit(C,(420,400))

        if (flag==11 or flag>=11):

            screen.blit(D,(500,400))

        if (flag==12 or flag>=12):

            screen.blit(R,(580,400))



        if (y>=480):

            return



        Flag=Flag+1

        x+=rate

        
        
            
        screen.blit(instructionSurf, instructionRect)        
        pygame.display.update()
        















