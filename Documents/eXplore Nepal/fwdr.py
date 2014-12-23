def fwdr():
        ##Importing
        import pygame,sys
        from pygame.locals import *
        import random
        pygame.init()


        ##screen settings
        screen=pygame.display.set_mode((800,600),pygame.FULLSCREEN)


        ##initialization of images
        bif="files/bif.jpg"
        mif="files/mif.png"
        cloud1="files/cloud1.png"
        cloud2="files/cloud2.png"
        manche="files/manche.png"
        fill1="files/fill1.png"
        fill2="files/fill2.png"
        fill3="files/fill3.png"
        fwdr="files/fwdr.jpg"
        boarder="files/boarder.png"
        api="files/api.jpg"
        dipayal="files/dipayal.jpg"
        deuda="files/deuda.jpg"
        mahakali="files/mahakali.jpg"
        gaura="files/gaura.jpg"
        mahakaliz="files/mahakali.png"
        setiz="files/seti.png"
        man="files/man.png"
        woman="files/woman.png"
        saipal="files/saipal.jpg"
        seti="files/seti.jpg"
        tikapur="files/tikapur.jpg"
        sulkhaphanta="files/sulkhaphanta.jpg"
        khaptad="files/khaptad.jpg"



        ##loading images
        back=pygame.image.load(bif).convert()
        cursor=pygame.image.load(mif).convert_alpha()
        cloud1=pygame.image.load(cloud1).convert_alpha()
        cloud2=pygame.image.load(cloud2).convert_alpha()
        fill1=pygame.image.load(fill1).convert_alpha()
        fill2=pygame.image.load(fill2).convert_alpha()
        manche=pygame.image.load(manche).convert_alpha()
        fill3=pygame.image.load(fill3).convert_alpha()
        fwdr=pygame.image.load(fwdr).convert()
        boarder=pygame.image.load(boarder).convert_alpha()
        dipayal=pygame.image.load(dipayal).convert()
        deuda=pygame.image.load(deuda).convert()
        mahakali=pygame.image.load(mahakali).convert()
        gaura=pygame.image.load(gaura).convert()
        mahakaliz=pygame.image.load(mahakaliz).convert_alpha()
        setiz=pygame.image.load(setiz).convert()
        man=pygame.image.load(man).convert_alpha()
        woman=pygame.image.load(woman).convert_alpha()
        saipal=pygame.image.load(saipal).convert()
        seti=pygame.image.load(seti).convert()
        api=pygame.image.load(api).convert()
        tikapur=pygame.image.load(tikapur).convert()
        sulkhaphanta=pygame.image.load(sulkhaphanta).convert()
        khaptad=pygame.image.load(khaptad).convert()


        ##music
        pygame.mixer.music.load('files/bg1.mp3')
        pygame.mixer.music.play(-1,2)


        ##intialization of variables
        pos1=(40,20)
        pos2=(460,20)
        clock=pygame.time.Clock()
        secs=0
        i=1
        flag=0
        count=0
        text_file = open("files/info.txt", "r")
        ufont = pygame.font.SysFont("monospace",19 )

        ##loop for background
        while True:
                x,y=pygame.mouse.get_pos()
                milli=clock.tick()
                sec=milli
                secs+=sec
                screen.blit(back,(0,0))
                if (secs in range((i*2250),(i*2350)) and flag==0)or (i==1):
                        txt1=text_file.readline()[:-2]
                        txt2=text_file.readline()[:-2]
                        txt3=text_file.readline()[:-2]
                        screen.blit(cloud1,pos1)
                        screen.blit(fill2,pos2)
                        label1 = ufont.render(txt1, 1, (0,random.randrange(255),0))
                        label2= ufont.render(txt2, 1, (0,random.randrange(255),0))
                        label3 = ufont.render(txt3, 1, (0,random.randrange(255),0))
                        screen.blit(label1, (70, 70))
                        screen.blit(label2, (70, 120))
                        screen.blit(label3, (70, 170))
                        screen.blit(manche,(250,300))
                        i+=1
                        flag=1
                        count=count+1
                        if (count==3):
                                screen.blit(fill3,(0,300))
                                screen.blit(fwdr,(250,300))
                                screen.blit(boarder,(245,295))
                                screen.blit(man,(650,310))
                                screen.blit(woman,(0,310))

                        if (count==7):
                                screen.blit(fill3,(0,300))
                                screen.blit(mahakaliz,(75,300))
                                screen.blit(boarder,(70,295))
                                screen.blit(setiz,(425,300))
                                screen.blit(boarder,(420,295))
                                screen.blit(man,(650,310))
                                screen.blit(woman,(0,310))

                        if (count==9):
                                screen.blit(fill3,(0,300))
                                screen.blit(deuda,(250,300))
                                screen.blit(boarder,(245,295))
                                screen.blit(man,(650,310))
                                screen.blit(woman,(0,310))
                        if (count==11):
                                screen.blit(fill3,(0,300))
                                screen.blit(gaura,(250,300))
                                screen.blit(boarder,(245,295))
                                screen.blit(man,(650,310))
                                screen.blit(woman,(0,310))
                        if (count==13):
                                screen.blit(fill3,(0,300))
                                screen.blit(seti,(75,300))
                                screen.blit(boarder,(70,295))
                                screen.blit(mahakali,(425,300))
                                screen.blit(boarder,(420,295))
                                screen.blit(man,(650,310))
                                screen.blit(woman,(0,310))
                        if (count==15):
                                screen.blit(fill3,(0,300))
                                screen.blit(tikapur,(250,300))
                                screen.blit(boarder,(245,295))
                                screen.blit(man,(650,310))
                                screen.blit(woman,(0,310))
                        pygame.display.update()
                elif (secs in range((i*2250),(i*2350)) and flag==1):
                        txt1=text_file.readline()[:-2]
                        txt2=text_file.readline()[:-2]
                        txt3=text_file.readline()[:-2]
                        screen.blit(cloud2,pos2)
                        screen.blit(fill1,pos1)
                        label1 = ufont.render(txt1, 1, (0,random.randrange(255),0))
                        label2= ufont.render(txt2, 1, (0,random.randrange(255),0))
                        label3 = ufont.render(txt3, 1, (0,random.randrange(255),0))
                        screen.blit(label1, (490, 70))
                        screen.blit(label2, (490, 120))
                        screen.blit(label3, (490, 170))
                        screen.blit(manche,(250,300))
                        i+=1
                        flag=0
                        count=count+1
                        if (count==6):
                                screen.blit(fill3,(0,300))
                                screen.blit(dipayal,(250,300))
                                screen.blit(boarder,(245,295))
                                screen.blit(man,(650,310))
                                screen.blit(woman,(0,310))
                        if (count==12):
                                screen.blit(fill3,(0,300))
                                screen.blit(api,(75,300))
                                screen.blit(boarder,(70,295))
                                screen.blit(saipal,(425,300))
                                screen.blit(boarder,(420,295))
                                screen.blit(man,(650,310))
                                screen.blit(woman,(0,310))
                        if (count==14):
                                screen.blit(fill3,(0,300))
                                screen.blit(sulkhaphanta,(75,300))
                                screen.blit(boarder,(70,295))
                                screen.blit(khaptad,(425,300))
                                screen.blit(boarder,(420,295))
                                screen.blit(man,(650,310))
                                screen.blit(woman,(0,310))
                        if (count==16):
                                return
                        pygame.display.update()
                screen.blit(cursor,(x,y))

                for event in pygame.event.get():
                        if event.type==QUIT:
                            pygame.quit()
                            sys.exit()
                if i==1:        
                        pygame.display.update()
