def ccdr():
    import pygame,sys
    from pygame.locals import *

    WHITE=(255,255,255)
    BLACK=(0,0,0)
    screen=pygame.display.set_mode((800,600),pygame.FULLSCREEN)
    screen.fill(WHITE)
    bds=pygame.image.load("pics_cdr/bds.jpg").convert_alpha()
    boudha=pygame.image.load("pics_cdr/b.jpg").convert_alpha()
    changu=pygame.image.load("pics_cdr/c.jpg").convert_alpha()
    kds=pygame.image.load("pics_cdr/k.jpg").convert_alpha()
    pashu=pygame.image.load("pics_cdr/p.jpg").convert_alpha()
    swa=pygame.image.load("pics_cdr/s.jpg").convert_alpha()
    back=pygame.image.load("pics_cdr/wall.jpg").convert()
    pygame.init()
    screen=pygame.display.set_mode((800,600),pygame.FULLSCREEN)
    flag=0
    clock=pygame.time.Clock()
    speed=250
    flag=0
    pygame.mixer.music.load('pics_cdr/bgforcdr.mp3')
    pygame.mixer.music.play(-1,0)              
    while True:
        for event in pygame.event.get():
            if (event.type==QUIT) :
                pygame.quit()
                sys.exit()

        x1,y1=50,200
        x2,y2=300,200
        x3,y3=550,200
        x4,y4=50,400
        x5,y5=300,400
        x6,y6=550,400
        h,v=0,0
        i1=pygame.transform.scale(bds,(200,150))
        i2=pygame.transform.scale(boudha,(200,150))
        i3=pygame.transform.scale(changu,(200,150))
        i4=pygame.transform.scale(kds,(200,150))
        i5=pygame.transform.scale(pashu,(200,150))
        i6=pygame.transform.scale(swa,(200,150))
        
        j1=pygame.transform.scale(bds,(800,600))
        j2=pygame.transform.scale(boudha,(800,600))
        j3=pygame.transform.scale(changu,(800,600))
        j4=pygame.transform.scale(kds,(800,600))
        j5=pygame.transform.scale(pashu,(800,600))
        j6=pygame.transform.scale(swa,(800,600))

        

        ufont = pygame.font.SysFont("monospace", 40)
        hfont=pygame.font.SysFont("monospace",120,bold=True)
        label = ufont.render("Press Enter to continue...", 1, (0,0,0))
        header=ufont.render("Major attractions of CDR",1,(0,0,0))
        label1 = ufont.render("Press Enter to continue...", 1, (255,255,255))
        
        screen.blit(back,(0,0))
        screen.blit(header,(100,50))
        screen.blit(label,(100,125))

        milli=clock.tick()
        seconds=milli/1000.0
        dm=seconds*speed
        
        for event in pygame.event.get():
            if event.type==KEYDOWN and event.key==K_RETURN:
                flag+=1
        
        
        if (flag==0):
            screen.blit(i1,(x1,y1))
            screen.blit(i2,(x2,y2))
            screen.blit(i3,(x3,y3))
            screen.blit(i4,(x4,y4))
            screen.blit(i5,(x5,y5))
            screen.blit(i6,(x6,y6))

        elif (flag==1):
            screen.blit(j1,(h,v))
            screen.blit(label, (170,550))
            h+=dm

        elif (flag==2):
            screen.blit(j2,(h,v))
            screen.blit(label, (170,500))

        elif (flag==3):
            screen.blit(j3,(h,v))
            screen.blit(label, (170,265))

        elif (flag==4):
            screen.blit(j4,(h,v))
            screen.blit(label, (170,200))

        elif (flag==5):
            screen.blit(j5,(h,v))
            screen.blit(label, (170,150))

        elif (flag==6):
            screen.blit(j6,(h,v))
            screen.blit(label1, (170,300))

        elif (flag==7):
            pygame.mixer.music.pause()
            return

            
        

            
        pygame.display.update()
