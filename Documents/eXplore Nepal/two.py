def wdr():
    mbif="randfiles/backgroundss.jpg"
    dif="randfiles/duck.png"
    wdif="randfiles/duckdead.png"
    c="randfiles/aim.png"
    bkimg="randfiles/image.png"
    pbac="randfiles/pokhara.jpg"
    pabac="randfiles/palpa.jpg"
    gbac="randfiles/gorkha.jpg"
    kbac="randfiles/kapilvastu.jpg"
    mubac="randfiles/mustang.jpg"
    ne="randfiles/next.png"

    import pygame,sys
    from pygame.locals import *
    pygame.init()
    myfont = pygame.font.SysFont("monospace", 15)
    myfont1= pygame.font.SysFont("monospace", 30)
    screen=pygame.display.set_mode((800,600),pygame.FULLSCREEN)

    mbac=pygame.image.load(mbif).convert()
    pointer=pygame.image.load(c).convert_alpha()
    duck=pygame.image.load(dif).convert_alpha()
    wduck=pygame.image.load(wdif).convert_alpha()
    hoverback=pygame.image.load(bkimg).convert_alpha()
    pokharaback=pygame.image.load(pbac).convert()
    palpabac=pygame.image.load(pabac).convert()
    gorkhaback=pygame.image.load(gbac).convert()
    kapilback=pygame.image.load(kbac).convert()
    mustangback=pygame.image.load(mubac).convert()
    nextdev=pygame.image.load(ne).convert_alpha()



    textmainpokhara=myfont1.render("This duck for POKHARA",1,(255,255,0))
    textmaingorkha=myfont1.render("This one's for GORKHA",1,(255,255,250))
    textmainkapilvastu=myfont1.render("I shall be sold to KAPILVASTU",1,(255,0,0))
    textmainmustang=myfont1.render("Want to go to MUSTANG?",1,(0,255,30))
    textmainpalpa=myfont1.render("I swear PALPA's fun",1,(21,210,30))
    textmain=myfont1.render("PRESS SPACE TO SHOOT",2,(0,255,0))
    tp1=myfont.render("I'm sure you have been to Pokhara is a major tourist destination. It has many places ",1,(0,0,0))
    tp2=myfont.render("to visit such as david's fall,fewa lake,etc. It is famous for Rainfall>>>PRESS N",1,(0,0,0))
    tg1=myfont.render("Gorkha is a beautiful city which is the homeland of late King Prithivi Narayan Shah",1,(0,0,0))
    tg2=myfont.render(". The palace is worth visiting. Ask your parents to take you there? >>>PRESS E",1,(0,0,0))
    tk1=myfont.render("Kapilvastu,in lumbini, is the hometown of The Light of ASIA, Gautam Budhha.",1,(0,0,0))
    tk2=myfont.render("It has many gumbas built by many several nations. You'll love it there>>>PRESS P",1,(0,0,0))
    tm1=myfont.render("Mustang is one of the most beautiful places on earth. The Muktinath Temple ",1,(0,0,0))
    tm2=myfont.render("is a major attraction. Did you know it SNOWS there? >>PRESS A",1,(0,0,0))
    tpa1=myfont.render("Palpa is a city famous for mild climate. It is compaired to Darjeeling of India.",1,(0,0,0))
    tpa2=myfont.render("Bhairavsthan Temple is attraction of this District>>>PRESS L",1,(0,0,0))

    mc=0
    duck1=0
    duck2=0
    duck3=0
    duck4=0
    duck5=0
    duck11=0
    duck22=0
    duck33=0
    duck44=0
    duck55=0


    
    pygame.mixer.music.load('randfiles/andreshbg.mp3')
    pygame.mixer.music.play(-1,0)


    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        

        screen.blit(mbac,(0,0))
        screen.blit(textmain,(0,0))
       
        
        

        x,y = pygame.mouse.get_pos()
        x -= pointer.get_width()/2
        y -= pointer.get_height()/2

        mousex,mousey=pygame.mouse.get_pos()

        if mousex in range(50,120) and mousey in range(400,518):
            screen.blit(hoverback,(50,400))
            screen.blit(textmainpokhara,(50,365))
            for event in pygame.event.get():
                if event.type==KEYDOWN:
                    if event.key==K_SPACE:
                        duck1=1
                        duck11=1
                        pygame.mixer.music.load('randfiles/bullet.mp3')
                        pygame.mixer.music.play(1,0)
            while duck11==1:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type==KEYDOWN:
                        if event.key==K_n:
                            duck11=0
                    if event.type==KEYUP:
                        if event.key==K_n:
                            duck11=0
                        
                screen.blit(pokharaback,(0,0))
                pygame.draw.rect(screen,(250,250,250),Rect((0,500),(800,100)))
                screen.blit(tp1, (0,500))
                screen.blit(tp2, (0,550))
                xx,yx = pygame.mouse.get_pos()
                xx -= pointer.get_width()/2
                yx -= pointer.get_height()/2
                screen.blit(pointer,(xx,yx))
                pygame.display.update()
                
        


        
        if mousex in range(170,240) and mousey in range(390,508):
            screen.blit(hoverback,(170,390))
            screen.blit(textmaingorkha,(70,355))
            for event in pygame.event.get():
                if event.type==KEYDOWN:
                    if event.key==K_SPACE:
                        duck2=1
                        duck22=1
                        pygame.mixer.music.load('randfiles/bullet.mp3')
                        pygame.mixer.music.play(1,0)
            while duck22==1:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type==KEYDOWN:
                        if event.key==K_e:
                            duck22=0
                    if event.type==KEYUP:
                        if event.key==K_e:
                            duck22=0
                        
                screen.blit(gorkhaback,(0,0))
                pygame.draw.rect(screen,(250,250,250),Rect((0,500),(800,100)))
                screen.blit(tg1, (0,500))
                screen.blit(tg2, (0,550))
                xx,yx = pygame.mouse.get_pos()
                xx -= pointer.get_width()/2
                yx -= pointer.get_height()/2
                screen.blit(pointer,(xx,yx))
                pygame.display.update()
                        
        if mousex in range(320,390) and mousey in range(405,523):
            screen.blit(hoverback,(320,405))
            screen.blit(textmainkapilvastu,(180,340))
            for event in pygame.event.get():
                if event.type==KEYDOWN:
                    if event.key==K_SPACE:
                        duck3=1
                        duck33=1
                        pygame.mixer.music.load('randfiles/bullet.mp3')
                        pygame.mixer.music.play(1,0)
            while duck33==1:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type==KEYDOWN:
                        if event.key==K_p:
                            duck33=0
                    if event.type==KEYUP:
                        if event.key==K_p:
                            duck33=0
                        
                screen.blit(kapilback,(0,0))
                pygame.draw.rect(screen,(250,250,250),Rect((0,500),(800,100)))
                screen.blit(tk1, (0,500))
                screen.blit(tk2, (0,550))
                xx,yx = pygame.mouse.get_pos()
                xx -= pointer.get_width()/2
                yx -= pointer.get_height()/2
                screen.blit(pointer,(xx,yx))
                pygame.display.update()
            
        if mousex in range(480,550) and mousey in range(396,514):
            screen.blit(hoverback,(480,396))
            screen.blit(textmainmustang,(120,365))
            for event in pygame.event.get():
                if event.type==KEYDOWN:
                    if event.key==K_SPACE:
                        duck4=1
                        duck44=1
                        pygame.mixer.music.load('randfiles/bullet.mp3')
                        pygame.mixer.music.play(1,0)
            while duck44==1:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type==KEYDOWN:
                        if event.key==K_a:
                            duck44=0
                    if event.type==KEYUP:
                        if event.key==K_a:
                            duck44=0
                        
                screen.blit(mustangback,(0,0))
                pygame.draw.rect(screen,(250,250,250),Rect((0,500),(800,100)))
                screen.blit(tm1, (0,500))
                screen.blit(tm2, (0,550))
                xx,yx = pygame.mouse.get_pos()
                xx -= pointer.get_width()/2
                yx -= pointer.get_height()/2
                screen.blit(pointer,(xx,yx))
                pygame.display.update()
                
        if mousex in range(650,720) and mousey in range(401,519):
            screen.blit(hoverback,(650,401))
            screen.blit(textmainpalpa,(400,356))
            for event in pygame.event.get():
                if event.type==KEYDOWN:
                    if event.key==K_SPACE:
                        duck5=1
                        duck55=1
                        pygame.mixer.music.load('randfiles/bullet.mp3')
                        pygame.mixer.music.play(1,0)
            while duck55==1:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type==KEYDOWN:
                        if event.key==K_l:
                            duck55=0
                    if event.type==KEYUP:
                        if event.key==K_l:
                            duck55=0
                        
                screen.blit(palpabac,(0,0))
                pygame.draw.rect(screen,(250,250,250),Rect((0,500),(800,100)))
                screen.blit(tpa1, (0,500))
                screen.blit(tpa2, (0,550))
                xx,yx = pygame.mouse.get_pos()
                xx -= pointer.get_width()/2
                yx -= pointer.get_height()/2
                screen.blit(pointer,(xx,yx))
                pygame.display.update()
        if duck1==0:
            screen.blit(duck,(50,400))
        else:
            screen.blit(wduck,(50,400))
            
        if duck2==0:
            screen.blit(duck,(170,390))
        else:
            screen.blit(wduck,(170,390))
            
        if duck3==0:
            screen.blit(duck,(320,405))
        else:
            screen.blit(wduck,(320,405))
            
        if duck4==0:
            screen.blit(duck,(480,396))
        else:
            screen.blit(wduck,(480,396))
            
        if duck5==0:
            screen.blit(duck,(650,401))
        else:
            screen.blit(wduck,(650,401))
     





        if duck1!=0 and duck2!=0 and duck3!=0 and duck3!=0 and duck4!=0 and duck5!=0:
            screen.blit(nextdev,(370,0))
            lastx,lasty=pygame.mouse.get_pos()
            if lastx in range(370,430) and lasty in range(0,70):
                for event in pygame.event.get():
                    if event.type==KEYDOWN:
                        if event.key==K_SPACE:
                            return
                        


        pygame.mouse.set_visible(0)
        screen.blit(pointer,(x,y))

        pygame.display.update()
