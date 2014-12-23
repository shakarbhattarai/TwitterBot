def cedr():
    bif="randfiles/background.jpg"
    mif="randfiles/flag.png"
    sif="randfiles/Sagarmatha.jpg"
    gok="randfiles/gokuc.png"
    gik="randfiles/ssj3-goku.jpg"
    tig="randfiles/tg.jpg"
    bhe="randfiles/bhedetar.jpg"
    ba="randfiles/dragonball.png"
    kos="randfiles/koshi.jpg"

    import pygame, sys
    from pygame.locals import *

    pygame.init()
    myfont = pygame.font.SysFont("monospace", 15)
    screen=pygame.display.set_mode((800,600),pygame.FULLSCREEN)

    bac=pygame.image.load(bif).convert()
    mou=pygame.image.load(mif).convert_alpha()
    sbac=pygame.image.load(sif).convert()
    goku=pygame.image.load(gok).convert_alpha()
    gokusta=pygame.image.load(gik).convert()
    ibac=pygame.image.load(tig).convert()
    bbac=pygame.image.load(bhe).convert()
    dball=pygame.image.load(ba).convert_alpha()
    kbac=pygame.image.load(kos).convert_alpha()

    textcong=myfont.render("Congratulations,you have successfully completed LEVEL 1!! Come on and lets explore .......",1,(0,0,0))
    textcong2=myfont.render("Press the key N",1,(0,0,0))
    textsagar1=myfont.render("lets have a look upon Mount Sagarmatha or Mount everest...",1,(0,0,0))
    textsagar2=myfont.render("It's the highest peak of the world which stands 8848 meters!!! Press the key E",1,(0,0,0))
    textillam1=myfont.render("This is the ILLAM TEA GARDEN..As we can see it has acres of land in which tea is grown",1,(0,0,0))
    textillam2=myfont.render("It is the largest seller of tea in NEPAL..Press the key P",1,(0,0,0))
    textbhede1=myfont.render("Bhedetar is a small town in EDR which is the gateway to limbu villages...this place is ",1,(0,0,0))
    textbhede2=myfont.render("famous for it's beautiful seneries of sunset and sunrise.. PRESS A",1,(0,0,0))
    textkoshi1=myfont.render("Sapta Koshi is one of the three major river systems of Nepal..It has seven tributaries",1,(0,0,0))
    textkoshi2=myfont.render("and the rivers penitrate most of EDR...Press L",1,(0,0,0))


    lp=1
    counter=800
    co=0
    t=0
    clock=pygame.time.Clock()
    mock=0
    pygame.mixer.music.load('randfiles/bg.mp3')
    pygame.mixer.music.play(-1,0)
    while lp!=0:
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


            if event.type==KEYDOWN:
                if event.key==K_n:
                    lp=0
            if event.type==KEYUP:
                if event.key==K_n:
                    lp=0
            
            screen.blit(bac,(0,0))
        if mock<5:
            screen.blit(dball,(645,375))
            screen.blit(dball,(750,500))
            screen.blit(dball,(690,480))
            screen.blit(dball,(665,500))
            mock=mock+.2
        elif mock<10:
            mock=mock+.2
            if mock==9:
                    mock=0
        if co==0:
            screen.blit(goku,(counter,200))
            if counter>350:
                counter=counter-.2
            else:
                co=1
            
        else:
            screen.blit(gokusta,(0,0))
            pygame.draw.rect(screen,(250,250,250),Rect((0,500),(800,100)))
            screen.blit(textcong, (0,500))
            screen.blit(textcong2, (0,550))
            letsag=1


       

        pygame.display.update()

    exits1=350

    while exits1>=0:
        screen.blit(bac,(0,0))
        screen.blit(dball,(645,375))
        screen.blit(dball,(750,500))
        screen.blit(dball,(690,480))
        screen.blit(dball,(665,500))    
        


        
        screen.blit(goku,(exits1,200))
        exits1=exits1-.2
        pygame.display.update()
        


    letsag=1
    cos=0
    counters=800
    while letsag==1:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type==KEYDOWN:
                if event.key==K_e:
                    letsag=0
            if event.type==KEYUP:
                if event.key==K_e:
                    letsag=0

            
        screen.blit(sbac,(0,0))
        if cos==0:
            screen.blit(goku,(counters,200))
            if counters>350:
                counters=counters-.2
            else:
                cos=1

        if cos==1:
            screen.blit(goku,(350,200))
            pygame.draw.rect(screen,(250,250,250),Rect((0,500),(800,100)))
            screen.blit(textsagar1,(0,500))
            screen.blit(textsagar2,(0,550))




        

        pygame.display.update()


    exits1=350

    while exits1>=0:
        screen.blit(sbac,(0,0))
        screen.blit(goku,(exits1,200))
        exits1=exits1-.2


        pygame.display.update()
        


    letil=1
    coi=0
    counti=800
    while letil==1:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type==KEYDOWN:
                if event.key==K_p:
                    letil=0
            if event.type==KEYUP:
                if event.key==K_p:
                    letil=0

            
        screen.blit(ibac,(0,0))
        if coi==0:
            screen.blit(goku,(counti,200))
            if counti>350:
                counti=counti-.2
            else:
                coi=1

        if coi==1:
            screen.blit(goku,(350,200))
            pygame.draw.rect(screen,(250,250,250),Rect((0,500),(800,100)))
            screen.blit(textillam1,(0,500))
            screen.blit(textillam2,(0,550))



        

        pygame.display.update()


    exits1=350

    while exits1>=0:
        screen.blit(ibac,(0,0))
        screen.blit(goku,(exits1,200))
        exits1=exits1-.2
        pygame.display.update()
        

    letil=1
    coi=0
    counti=800
    while letil==1:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type==KEYDOWN:
                if event.key==K_a:
                    letil=0
            if event.type==KEYUP:
                if event.key==K_a:
                    letil=0

            
        screen.blit(bbac,(0,0))
        if coi==0:
            screen.blit(goku,(counti,200))
            if counti>350:
                counti=counti-.2
            else:
                coi=1

        if coi==1:
            screen.blit(goku,(350,200))
            pygame.draw.rect(screen,(250,250,250),Rect((0,500),(800,100)))
            screen.blit(textbhede1,(0,500))
            screen.blit(textbhede2,(0,550))



        

        pygame.display.update()

    exits1=350

    while exits1>=0:
        screen.blit(bbac,(0,0))
        screen.blit(goku,(exits1,200))
        exits1=exits1-.2
        pygame.display.update()
        
        3333
        
    letil=1
    coi=0
    counti=800
    while letil==1:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type==KEYDOWN:
                if event.key==K_l:
                    letil=0
            if event.type==KEYUP:
                if event.key==K_l:
                    letil=0

            
        screen.blit(kbac,(0,0))
        if coi==0:
            screen.blit(goku,(counti,200))
            if counti>350:
                counti=counti-.2
            else:
                coi=1

        if coi==1:
            screen.blit(goku,(350,200))
            pygame.draw.rect(screen,(250,250,250),Rect((0,500),(800,100)))
            screen.blit(textkoshi1,(0,500))
            screen.blit(textkoshi2,(0,550))



        

        pygame.display.update()

    exits1=350

    while exits1>=0:
        screen.blit(kbac,(0,0))
        screen.blit(goku,(exits1,200))
        exits1=exits1-.2
        pygame.display.update()
        

    pygame.mixer.music.pause()
    return    

