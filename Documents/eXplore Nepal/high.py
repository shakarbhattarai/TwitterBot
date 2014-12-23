def high():
    ##Importing
    import pygame,sys
    from pygame.locals import *
    from filehandle import*
    pygame.init()


    ##screen settings
    screen=pygame.display.set_mode((800,600),pygame.FULLSCREEN)


    ##initialization of images
    bif="filess/bif.jpg"
    title="filess/title.png"
    back1="filess/back1.png"
    back2="filess/back2.png"


    ##converting images
    bif=pygame.image.load(bif).convert()
    title=pygame.image.load(title).convert_alpha()
    title=pygame.transform.scale(title,(700,100))
    back1=pygame.image.load(back1).convert_alpha()
    back2=pygame.image.load(back2).convert_alpha()
    myfont = pygame.font.SysFont("Times New Roman",25)
    titlefont=pygame.font.SysFont("Arial",30)
    ##loop forbackground
    p,q=0,0
    screen.blit(bif,(0,0))
    txt="NAME                                   SCORE"
    screen.blit(title,(10,50))
    
    if getscore(p)==None:
        print "none"
        return
    temp1,temp2,total=getscore(p)
    print total
    c=[None]*(((total/2)))
    d=[None]*(((total/2)))
    if total==None:
        print "zero"
        return
    for p in range (1,((total/2)+1)):
        print getscore(p)
        c[p-1],d[p-1],total=getscore(p)
        
        d[p-1]=int(d[p-1])
        
    for p in range (0,(total/2)):
        for q in range (p,((total/2))):
            if int(d[p])<int(d[q]):
                newc=c[q]
                newd=d[q]
                d[q]=d[p]
                c[q]=c[p]
                d[p]=newd
                c[p]=newc
       

        
    while 1:
        x,y = pygame.mouse.get_pos()
        screen.blit(back2,(700,500))
        for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
        if x in range (700,800) and y in range (500,600):
            
            screen.blit(back1,(700,500))
            print "TESting"
            for event in pygame.event.get():
                if (event.type == pygame.MOUSEBUTTONDOWN) or (event.type==pygame.MOUSEBUTTONUP):
                    
                    return
        for p in range (0,(((total/2)))):
            txt1=str(c[p])
            txt2=str(d[p])
            
            label1=myfont.render(txt1, 0, (255,0,0))
            label2=myfont.render(txt2, 0, (255,0,0))
            labelfortitle=titlefont.render(txt,1,(0,255,0))
            
            pygame.draw.rect(screen,(60,60,255),(10,195,800,30))
            screen.blit(label1,(55,245+(p*25)))
            screen.blit(label2,(395,245+(p*25)))
            
        screen.blit(labelfortitle,(10,195))
        pygame.display.update()


