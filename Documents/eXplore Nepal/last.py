def last():
        bif="lastimages/background.jpg"
        c1="lastimages/candle2.png"
        cb2="lastimages/candle1.png"

        d1="lastimages/diyo1.png"
        d2="lastimages/diyo2.png"
        r="lastimages/rocketflyorgi.png"
        rf="lastimages/rocketflyorgi.png"
        dh="lastimages/diyohover.png"
        rh="lastimages/rockethover.png"
        ex="lastimages/explosion.png"
        la="lastimages/lastbac.png"
        temp=False
        import pygame,sys
        from pygame.locals import *
        pygame.init()
        myfont = pygame.font.SysFont("monospace", 15)
        screen=pygame.display.set_mode((800,600),pygame.FULLSCREEN)

        bac=pygame.image.load(bif).convert()
        cur1=pygame.image.load(c1).convert_alpha()
        cur2=pygame.image.load(cb2).convert_alpha()
        diyohover=pygame.image.load(dh).convert_alpha()

        diyo1=pygame.image.load(d1).convert_alpha()
        diyo2=pygame.image.load(d2).convert_alpha()
        rocket=pygame.image.load(r).convert_alpha()
        rocketburning=pygame.image.load(rf).convert_alpha()
        rockethover=pygame.image.load(rh).convert_alpha()
        explosion=pygame.image.load(ex).convert_alpha()
        lbac=pygame.image.load(la).convert_alpha()
       

        di=1
        mm=1
        rr=0
        rmove=0
        rhh=0
        last=0
        flag=False
        pygame.mixer.music.load('lastimages/rocket.mp3')
        
        while True:
            
            

            for event in pygame.event.get():
                if event.type == QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
                    return
            
            screen.blit(bac,(0,0))
            font = pygame.font.SysFont('Arial',32)
            if flag==False:
                title = font.render("Please light the candle from the diyo", True,(255,0,120))
            elif flag==True:
                title = font.render("Now Light the Rocket", True,(255,0,120))        
            else:
                title=font.render(" ",True,(255,0,120))
            if di%2.0==0:
                
                screen.blit(diyo1,(0,525))
                di=di+mm
            else:
                
                di=di+mm
                screen.blit(diyo2,(0,525))
            

            mousex,mousey=pygame.mouse.get_pos()
            if mm==1:
                if mousex in range(0,50) and mousey in range(525,600):
                    screen.blit(diyohover,(0,510))
                    screen.blit(diyo2,(0,525))
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        mm=2
                        rr=1
                        flag=True
            
            if rhh==0:
                screen.blit(rocket,(403,485))
            
            if mousex in range(403,439) and mousey in range(525,600):
                if rr==1 and rhh==0:
                    temp=True
                    screen.blit(rockethover,(403,525))
                    screen.blit(rocket,(403,525))
                    flag=56
                    rhh=1         
            if rhh==1:
                screen.blit(rocketburning,(403,525-rmove))
                
                if rmove<=500:
                    rmove=rmove+1
            if rmove==501:
                screen.blit(explosion,(330,10))
                if last<200:
                    last=last+1
            if last==200:
                screen.blit(lbac,(0,0))
            if mm==1:
                x,y = pygame.mouse.get_pos()
                x -= cur1.get_width()/2
                y -= cur1.get_height()/2
                screen.blit(cur1,(x,y))
            else:
                x,y = pygame.mouse.get_pos()
                x -= cur2.get_width()/2
                y -= cur2.get_height()/2
                screen.blit(cur2,(x,y))
            screen.blit(title,(100,100))
            if temp==True:
                    pygame.mixer.music.play(-1,1.5)
                    temp=False
            pygame.display.update()
            






                
            
