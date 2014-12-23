def checkanswer(a,score):
    print a
    import pygame
    import sys
    from pygame.locals import*
    pygame.init()
    screen=pygame.display.set_mode((800,600),pygame.FULLSCREEN)
    
    


   
    while True:
       
    
        if a==True:
            correct(score) 
            return
        else:
            wrong(score)

               
            
        for event in pygame.event.get():
            if event.type==QUIT or event.type==KEYDOWN and event.key==K_ESCAPE:
                pygame.quit()
                sys.exit()
        pygame.display.update()
    
def correct(score):
    import pygame
    import sys
    from pygame.locals import*
    from random import randrange
    pygame.init()
    image1=pygame.image.load("randfiles/goku.png").convert_alpha()
    image1=pygame.transform.scale(image1,(250,250))
    image2=pygame.image.load("randfiles/goku2.png").convert_alpha()
    image2=pygame.transform.scale(image2,(250,250))
    image3=pygame.image.load("randfiles/scores.png").convert_alpha()
    image3=pygame.transform.scale(image3,(250,250))
    screen=pygame.display.set_mode((800,600),pygame.FULLSCREEN)
    temp=True
    clock=pygame.time.Clock()
    sec=0
    x=0
    main=image1
    score=int(score)
    score=score-1
    myfont = pygame.font.SysFont("monospace", 75)
    myfont2 = pygame.font.SysFont("monospace", 23)
    ct=myfont2.render("",1,(255,0,0))
    while True:
        screen.fill((0,0,0))
        milli=clock.tick()
        sec+=milli
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            elif (event.type==KEYDOWN and event.key==K_UP):
                return 0
        if sec>2000:
            main=image2
            pygame.draw.rect(screen,(60,60,255),(130,395,x,100))
            x+=0.75
            if x>=500:
                x=500
                score=int (score)
                score+=1
                ct=myfont2.render("CONGRATULATIONS! YOU ARE CORRECT!Press UP ARROW or SPACE!!",1,(255,0,0))
                sec=-1000000
        score=str (score)
        screen.blit(ct,(0,200))
        txt=myfont.render(score,1,(0,0,0))
        screen.blit(main,(0,300))
        screen.blit(image3,(600,300))
        screen.blit(txt,(630,330))
        pygame.display.update()
        for event in pygame.event.get():
            if  (event.type==KEYDOWN and event.key==K_SPACE) or (event.type==KEYUP and event.key==K_SPACE):
                return
    
def wrong(score):
    import pygame
    import sys
    from pygame.locals import*
    from random import randrange
    pygame.init()
    pygame.mixer.music.load('randfiles/haryo.mp3')
    pygame.mixer.music.play(-1,0)

    image1=pygame.image.load("randfiles/goku.png").convert_alpha()
    image1=pygame.transform.scale(image1,(250,250))
    image2=pygame.image.load("randfiles/goku2.png").convert_alpha()
    image2=pygame.transform.scale(image2,(250,250))
    image3=pygame.image.load("randfiles/scores.png").convert_alpha()
    image3=pygame.transform.scale(image3,(250,250))
    screen=pygame.display.set_mode((800,600),pygame.FULLSCREEN)
    temp=True
    clock=pygame.time.Clock()
    sec=0
    x=0
    main=image1
    
    myfont = pygame.font.SysFont("monospace", 75)
    myfont2 = pygame.font.SysFont("monospace", 23)
    ct=myfont2.render("",1,(255,0,0))
    while True:
        screen.fill((0,0,0))
        milli=clock.tick()
        sec+=milli
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            elif (event.type==KEYDOWN and event.key==K_UP):
                return 0
        if sec>4000:
            main=image2
            pygame.draw.rect(screen,(60,60,255),(130,300,x,300))
            x+=0.75
            if x>=800:
                x=800
                while True:
                    screen.fill((0,0,105))
                    
                    ct=myfont2.render("Sorry you couldn't make it. Game will now quit",0,(255,255,255))
                    ct2=myfont2.render("Your score has been recorded. Press Space to exit",1,(255,255,255))
                    screen.blit(ct,(0,200))
                    screen.blit(ct2,(0,300))
                    pygame.display.update()
                    for event in pygame.event.get():
                        if  (event.type==KEYDOWN and event.key==K_SPACE):
                            pygame.quit()
                            sys.exit()
                sec=-1000000
        score=str (score)
        screen.blit(ct,(0,200))
        txt=myfont.render(score,1,(0,0,0))
        screen.blit(main,(0,300))
        screen.blit(image3,(600,300))
        screen.blit(txt,(630,330))
        pygame.display.update()
        for event in pygame.event.get():
            if  (event.type==KEYDOWN and event.key==K_SPACE):
                return
