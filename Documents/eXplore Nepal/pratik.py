
def pratik(a):          
    import pygame,sys
    from filehandle import*
    from pygame.locals import*
    import random
    from one import*
    from two import*
    from cdr import*
    from random import randrange
    from congrats import*
    from last import*
    from fwdr import*
    from mwdr import*
    from beforeedr import*
    from beforecdr import*
    from beforewdr import*
    from beforemwdr import*
    from beforefwdr import*
    from tutorial import*
    from credit import*
    from pause import*
    pygame.init()
    tutorial()
    beforeedr()
    screen=pygame.display.set_mode((800,600),pygame.FULLSCREEN)
    event = pygame.event.poll()
    nepal="data/nep.png"
    title="data/title.png"
    m_r2l="data/r2l.png"
    m1=pygame.image.load("randfiles/01.png").convert_alpha()
    m2=pygame.image.load("randfiles/02.png").convert_alpha()
    m3=pygame.image.load("randfiles/03.png").convert_alpha()
    m4=pygame.image.load("randfiles/04.png").convert_alpha()
    m5=pygame.image.load("randfiles/05.png").convert_alpha()
    road=pygame.image.load("randfiles/road.png").convert_alpha()
    scores=pygame.image.load("randfiles/score.png").convert_alpha()
    level=0
    expon=pygame.image.load(title).convert_alpha()
    Nepal=pygame.image.load(nepal).convert_alpha()
    r2l=pygame.image.load(m_r2l).convert_alpha()
    x,y=370,320
    movex,movey=0,0
    seconds=0
    second=0
    answered=False
    fa=False
    fb=False
    fc=False
    fd=False
    qn=0
    c,d,e,f=random.sample(range(4), 4)
    temp=random.sample(range(65),25)
    number=temp[qn]
    score=0
    Flag=0
    count=0
    sec=0
    clock=pygame.time.Clock()
    u=0
    ce=0
    counts=True
    checkflag=False
    #event=()
    level=0
    score=0
    pygame.mixer.music.load('randfiles/pinkybg.mp3')
    pygame.mixer.music.play(-1,0)
    clock=pygame.time.Clock()
    while True:
        
        milli=clock.tick()
        seconds=milli
        speed=0.065
        step=int (speed*seconds)
        print step
        number=temp[qn]+1
        if counts==False:
            ce=randrange(5)
            counts=True
        if ce==0:
            big="data/b.jpg"
            
        elif ce==1:
            big="data/001.jpg"
           
        elif ce==2:
            big="data/002.jpg"
            
        elif ce==3:
            big="data/003.jpg"
            
        else:
            big="data/004.jpg"
            
        background=pygame.image.load(big).convert()
        Flagentry=2
        for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    sys.exit()
                elif(event.type==KEYDOWN and event.key==K_ESCAPE):
                    pause(a,score)
                # Move the man
                
                if event.type==KEYDOWN:
                    count+=1
                    Flagentry=3
                    if  event.key==K_RIGHT :
                        
                        movex=+step
                        Flag+=1
                        
                    elif event.key==K_LEFT:
                        movex=-step
                        Flag-=1
                    elif event.key==K_UP:
                        movey=-step
                        Flag+=1
                    elif event.key==K_DOWN:
                        movey=+step
                        Flag-=1
                    
                if event.type==KEYUP:
                    count=0
                    Flagentry=1
                    if event.key==K_RIGHT :
                        movex=0
                    elif event.key==K_LEFT:
                        movex=0
                    elif event.key==K_UP:
                        movey=0
                    elif event.key==K_DOWN:
                        movey=0
    
        if Flagentry==2 and count>=1:
            if (event.type==KEYDOWN or event.type==KEYUP) and (event.key==K_RIGHT or event.key==K_UP):
                        Flag+=1
                        if Flag>4 :
                            Flag=0
            elif (event.type==KEYDOWN or event.type==KEYUP) and (event.key==K_LEFT or event.key==K_DOWN):
                        Flag-=1
                        if Flag<-4:
                            Flag=0
            
            Flagentry=0
                       
        x+=movex
        y+=movey

        screen.blit(background,(0,0))
        screen.blit(expon,(10,10))
        screen.blit(road,(150,169))
        screen.blit(scores,(100,199))
        g=getoptions(number)
        correct=g[0]
            
        #Transparent map of nepal will be used
        screen.blit(Nepal,(585,0))
        if score in range(0,5):
            if u in range(0,20):
                
                pygame.draw.circle(screen, (255,0,0), (780,100), 7)
                u+=1
            elif u in range(20,40):
                pygame.draw.circle(screen, (255,255,255), (780,100), 7)
                u+=1
            if u==40:
                u=0
        elif score in range(5,10):
            if u in range(0,20):
                
                pygame.draw.circle(screen, (255,0,0), (730,85), 7)
                u+=1
            elif u in range(20,40):
                pygame.draw.circle(screen, (255,255,255), (730,85), 7)
                u+=1
            if u==40:
                u=0
        elif score in range(10,15):
            if u in range(0,20):
                
                pygame.draw.circle(screen, (255,0,0), (690,65), 7)
                u+=1
            elif u in range(20,40):
                pygame.draw.circle(screen, (255,255,255), (690,65), 7)
                u+=1
            if u==40:
                u=0
        elif score in range(15,20):
            if u in range(0,20):
                
                pygame.draw.circle(screen, (255,0,0), (650,55), 7)
                u+=1
            elif u in range(20,40):
                pygame.draw.circle(screen, (255,255,255), (650,55), 7)
                u+=1
            if u==40:
                u=0
        elif score in range(20,25):
            if u in range(0,20):
                
                pygame.draw.circle(screen, (255,0,0), (610,45), 7)
                u+=1
            elif u in range(20,40):
                pygame.draw.circle(screen, (255,255,255), (610,45), 7)
                u+=1
            if u==40:
                u=0
        #Display user
        ufont = pygame.font.SysFont("monospace", 30)
        label = ufont.render("Username:", 1, (0,0,0))
        """BLIT USERNAME HERE"""
        #Hari is replaced by get_user()
        label= ufont.render(a,1,(0,0,0))
        """BLIT SCORE HERE"""
        #Display score
        label = ufont.render("SCORE", 1, (255,0,0))
        screen.blit(label, (0,215))
        #*** is replaced by get_score()
        marks=(str) (score)  
        label = ufont.render(marks, 1, (0,0,255))
        screen.blit(label, (130,235))
        #The color of text box will be changed
        #Question box
        pygame.draw.rect(screen,(60,60,255),(10,125,1000,50))
        #Answer boxes

        ###pygame.draw.rect(screen,(255,255,255),(100,380,265,65))
        """
        ###pygame.draw.rect(screen,(255,255,255),(430,380,265,65))
        ###pygame.draw.rect(screen,(255,255,255),(100,480,265,65))
        ###pygame.draw.rect(screen,(255,255,255),(430,480,265,65))"""

        
        #display questions
        #"some text" is replaced by disp_question()
        if len(questions(number)) < 50:
            fontsize=24
        elif len(questions(number)) in range(50,75):
            fontsize=18
        else:
            fontsize=12
        qfont = pygame.font.SysFont("monospace",fontsize)
        
        label = qfont.render(questions(number), 1, (255,255,255))
        screen.blit(label, (10,135))
        #display options
        #option 1,2,3,4 are replced by disp_options()
        if len(g[c])>25:
            fontsize=15
        elif len(g[c])>30:
            fontsize=10
        else:
            fontsize=16
        myfont = pygame.font.SysFont("monospace", fontsize)

        pygame.draw.rect(screen,(72,72,72),(10,370,305,53))
        label = myfont.render(g[c], 1, (0,255,0))
        screen.blit(label, (15,390))
        
        
        label = myfont.render(g[d], 1, (255,130,200))
        pygame.draw.rect(screen,(72,72,72),(490,368,305,53))
        screen.blit(label, (500,390))
        
        label = myfont.render(g[e], 1, (0,190,255))
        pygame.draw.rect(screen,(72,72,72),(230,200,305,53))
        screen.blit(label, (250,217))


        label = myfont.render(g[f], 1, (255,255,255))
        pygame.draw.rect(screen,(72,72,72),(270,530,305,53))
        screen.blit(label, (290,548))
        
        
        
        mousex,mousey=pygame.mouse.get_pos()
        
        if mousex in range(x-50,x+50) and mousey in range(y-50,y+50):
            
            ufont = pygame.font.SysFont("monospace", 30)
            labels = ufont.render("MOVE ME", 1, (255,0,0))
            screen.blit(labels, (x-170,y))
            pygame.draw.circle(screen, (0,25,255), (x+32,y+40), 50, 12)
            
      
        if Flag==0:
            screen.blit(m1,(x,y))
                
        elif Flag==1 or Flag==-1:
            screen.blit(m2,(x,y))
                        
        elif Flag==2 or Flag== -2:
            screen.blit(m3,(x,y))
                         
        elif Flag==3 or Flag== -3:
            screen.blit(m4,(x,y))
                         
        elif Flag==4 or Flag== -4:
                screen.blit(m2,(x,y))

        elif Flag>4 or Flag<-4:
                Flag=0
        
        for i in range(170):
            
            for j in range(70):
               

                
                
                if event.type==KEYDOWN:
                    if event.key==K_RIGHT:
                       
                            movex=+step
                        
                    elif event.key==K_LEFT:
                        movex=-step
                    elif event.key==K_UP:
                        movey=-step
                    elif event.key==K_DOWN:
                        movey=+step
                if event.type==KEYUP:
                    if event.key==K_RIGHT:
                        movex=0
                    elif event.key==K_LEFT:
                        movex=0
                    elif event.key==K_UP:
                        movey=0
                    elif event.key==K_DOWN:
                        movey=0

                
                if (x,y) in [(40+i,280+j)]:
                    for event in pygame.event.get():
                                                      
                        if ((event.type==KEYDOWN) or (event.type==KEYUP)):
                            if event.key==K_RETURN:
                               
                                x,y=370,320
                                
                                if c==0:
                                    c,d,e,f=random.sample(range(4), 4)    
                                    print "Correct! :)"
                                   
                                    score+=1
                                    answered=True
                                    checkanswer(True,score)
                                    counts=False
                                    pygame.display.update()
                                    
                                else:
                                    writescores(a,score)
                                    checkanswer(False,score)
                                    
                                    pygame.display.update()
                            
                            
                    
                    
                            
                            pygame.draw.rect(screen,(255,140,0),(10,370,305,53),3)
                    
                    

                elif (x,y) in [(480+i,280+j)]:
                    
                    label = myfont.render("Option 2", 1, (255,255,255))
                    #screen.blit(label, (520,400))
                    pygame.draw.rect(screen,(255,140,0),(490,368,305,53),3)

                   
                    #label = myfont.render(sec, 1, (255,255,255))
                    #screen.blit(label,(0,0))
                    for event in pygame.event.get():
                        
                        
                        if (event.type==KEYDOWN) or (event.type==KEYUP):
                            if event.key==K_RETURN:
                                
                                
                               
                                x,y=370,320
                                if d==0:
                                    print "Correct! :)"
                                    score+=1
                                    checkanswer(True,score)
                                    counts=False
                                    pygame.display.update()
                                    answered=True
                                    c,d,e,f=random.sample(range(4), 4)
                                    
                                else:
                                    writescores(a,score)
                                    checkanswer(False,score)
                                    
                                    pygame.display.update()
                        

                elif (x,y) in [(300+i,100+j)]:
                    
                    pygame.draw.rect(screen,(230,140,0),(230,200,305,53),3)
                    label = myfont.render("Option 3", 1, (255,255,255))
                    
                                         
                    #label = myfont.render(sec, 1, (255,255,255))
                    #screen.blit(label,(0,0))
                    for event in pygame.event.get():
                        
                        
                        if (event.type==KEYDOWN) or (event.type==KEYUP):
                            if event.key==K_RETURN:
                                
                                
                                
                                x,y=370,320
                                if e==0:
                                   c,d,e,f=random.sample(range(4), 4)
                                   print "Correct! :)"
                                   score+=1
                                   checkanswer(True,score)
                                   counts=False
                                   answered=True
                                   pygame.display.update()
                                   
                                else:
                                    writescores(a,score)
                                    checkanswer(False,score)
                                    
                                    pygame.display.update()
                                    
                        
                elif (x,y) in [(300+i,450+j)]:
                    pygame.draw.rect(screen,(255,140,0),(270,530,305,53),3)
                    label = myfont.render("Option 4", 1, (255,255,255))

                    
                    #label = myfont.render(sec, 1, (255,255,255))
                    #screen.blit(label,(0,0))
                    for event in pygame.event.get():
                        
                        
                        if (event.type==KEYDOWN):
                            if (event.type==KEYDOWN) or (event.type==KEYUP):
                                if event.key==K_RETURN:
                                    
                                    
                                    
                                    x,y=370,320
                                    if f==0:
                                        c,d,e,f=random.sample(range(4), 4)
                                        print "Correct! :)"
                                        score+=1
                                        checkanswer(True,score)
                                        counts=False
                                        answered=True
                                        pygame.display.update()
                                        
                                        
                                    else:
                                        writescores(a,score)
                                        checkanswer(False,score)
                                        
                                        pygame.display.update()
                             
                    
                              
        if score==5 and level==0:
                    cedr()
                    level=1
                    
                    beforecdr()
                    pygame.mixer.music.load('randfiles/pinkybg.mp3')
                    pygame.mixer.music.play(-1,0)
                     
        elif score==10 and level==1:
                    pygame.event.clear()
                    pygame.mixer.music.pause()
                    ccdr()
                    level=2
                    beforewdr()
                    pygame.mixer.music.load('randfiles/pinkybg.mp3')
                    pygame.mixer.music.play(-1,0)

        elif score==15 and level==2:
                    pygame.mixer.music.pause()
                    wdr()
                    level=3
                    beforemwdr()
                    pygame.mixer.music.load('randfiles/pinkybg.mp3')
                    pygame.mixer.music.play(-1,0)
                   
        elif score==20 and level==3:
                    pygame.mixer.music.pause()
                    mwdr()
                    level=4
                    beforefwdr()
                    pygame.mixer.music.load('randfiles/pinkybg.mp3') 
                    pygame.mixer.music.play(-1,0)
                    
        elif score==25 and level==4:
                    pygame.mixer.music.pause()
                    fwdr()
                    level=5
                    writescores(a,score)
                    last()
                    credit()
                    
        if answered==True:
            qn+=1
            answered=False
        pygame.display.update()
        if(x in (0,800) or y in (0,600)):
            print x,y
            x,y=370,320

