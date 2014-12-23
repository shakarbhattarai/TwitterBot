def pause(username,score):
        ##Importing
        import pygame,sys
        from pygame.locals import *
        from filehandle import*
        pygame.init()

        screen=pygame.display.set_mode((800,600),pygame.FULLSCREEN)

        ##initialization of images
        bif=pygame.image.load("files/bif2.jpg")
        mif=pygame.image.load("files/mif.png")
        resume=pygame.image.load("files/resume.png")
        exitg=pygame.image.load("files/exitg.png")
        board=pygame.image.load("files/score.png")
        bresume=pygame.image.load("files/bresume.png")
        bexit=pygame.image.load("files/bexit.png")
        tick=pygame.image.load("files/tick.png")
        cross=pygame.image.load("files/cross.png")
        really=pygame.image.load("files/really.png")
        sure=pygame.image.load("files/sure.png")
        gamep=pygame.image.load("files/pause.png")



        flag=1
        while True:
            mousex,mousey=pygame.mouse.get_pos()
            pygame.mouse.set_visible(0)
            ufont = pygame.font.SysFont("monospace", 60)
            label = ufont.render(str(score), 1, (0,0,0))
            screen.blit(bif,(0,0))
            for event in pygame.event.get(): # User did something
                if event.type==QUIT:
                            pygame.quit()
                            sys.exit()
            if flag==1:
                    screen.blit(board,(600,50))
                    screen.blit(gamep,(50,50))
                    screen.blit(label, (620,70))
                    screen.blit(resume,(100,400))
                    screen.blit(exitg,(500,400))
                    
                    if mousex in range(100,300) and mousey in range(400,600):
                            screen.blit(bresume,(250,250))
                            for event in pygame.event.get():
                                    if event.type == pygame.MOUSEBUTTONDOWN or event.type==pygame.MOUSEBUTTONUP:
                                            return
                    elif mousex in range(500,700) and mousey in range(400,600):
                            screen.blit(bexit,(100,250))
                            for event in pygame.event.get():
                                    if event.type == pygame.MOUSEBUTTONDOWN or event.type==pygame.MOUSEBUTTONUP:
                                            flag=0
            elif flag==0:
                    screen.blit(really,(350,500))
                    screen.blit(sure,(100,350))
                    screen.blit(tick,(100,100))
                    screen.blit(cross,(525,100))
                    if mousex in range(100,(100+150)) and mousey in range(100,250):
                            if event.type == pygame.MOUSEBUTTONDOWN or event.type==pygame.MOUSEBUTTONUP:
                                    writescores(username,score)
                                    pygame.quit()
                                    sys.exit()
                    if mousex in range(525,(525+150)) and mousey in range(100,(100+150)):
                            if event.type == pygame.MOUSEBUTTONDOWN or event.type==pygame.MOUSEBUTTONUP:
                                    flag=1
            screen.blit(mif,(mousex,mousey))
            pygame.display.update()
