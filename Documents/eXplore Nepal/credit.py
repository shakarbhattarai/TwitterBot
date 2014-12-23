
def credit():
        import pygame,sys,time
        from pygame.locals import*
        pygame.init()

        #screen settings
        screen=pygame.display.set_mode((800,600),pygame.FULLSCREEN)

        pygame.mixer.music.load('files/bg.mp3')
        pygame.mixer.music.play(-1,2)
        #initialization of images
        bif=pygame.image.load("new/bif.jpg")

        txt1="CREDITS"
        txt2="Developers"
        txt3="Shakar Bhattarai"
        txt4="Sudeep Mishra"
        txt5="Andresh Singh"
        txt6="Pratik Joshi"
        txt7="Shradha Silwal"
        txt8="Press Escape to quit"
        txts1 = pygame.font.SysFont("Arial",40)
        txts2 = pygame.font.SysFont("Arial",32)
        txts3 = pygame.font.SysFont("Arial",24)
        txts4 = pygame.font.SysFont("Arial",15)
        lable1 = txts1.render(txt1,1,(255,255,0))
        lable2 = txts2.render(txt2,1,(255,0,0))
        lable3 = txts3.render(txt3,1,(255,0,0))
        lable4 = txts3.render(txt4,1,(255,0,0))
        lable5 = txts3.render(txt5,1,(255,0,0))
        lable6 = txts3.render(txt6,1,(255,0,0))
        lable7 = txts3.render(txt7,1,(255,0,0))
        lable8 = txts4.render(txt8,1,(255,255,255))
        move=0

        while 1:
                for event in pygame.event.get():
                    if event.type == KEYDOWN and event.key==K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                screen.blit(bif,(0,0))
                screen.blit(lable1,(10,600-move))
                screen.blit(lable2,(10,680-move))
                screen.blit(lable3,(10,720-move))
                screen.blit(lable4,(10,750-move))
                screen.blit(lable5,(10,780-move))
                screen.blit(lable6,(10,810-move))
                screen.blit(lable7,(10,840-move))
                screen.blit(lable8,(10,870-move))
                move=move+0.2    
                
                pygame.display.update()
