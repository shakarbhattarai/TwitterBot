def mwdr():
        ##Importing
        import pygame,sys
        from pygame.locals import *
        pygame.init()
        import random


        ##screen settings
        screen=pygame.display.set_mode((800,600),pygame.FULLSCREEN)

        pygame.mixer.music.load('filed/copter.mp3')
        pygame.mixer.music.play(-1,2)
        ##initialization of images
        heli1="filed/cop1.png"
        heli2="filed/cop2.png"
        heli3="filed/cop3.png"
        heli4="filed/cop4.png"
        heli5="filed/cop5.png"
        back1="filed/back1.jpg"
        back2="filed/back2.jpg"
        back3="filed/back3.jpg"
        back4="filed/back4.jpg"
        jumla_khalanga_bazzar="filed/jumla_khalanga_bazzar.jpg"
        rara_lake="filed/rara_lake.jpg"
        shey_phoksundo="filed/shey_phoksundo.jpg"
        surkhet="filed/surkhet_airport.jpg"
        swargadwari="filed/swargadwari.jpg"
        txt_cloud="filed/txt_cloud.png"
        up="filed/up.png"
        down="filed/down.png"
        crash="filed/crash.jpg"
        bm="filed/bm.mp3"

        ##loading images
        heli1=pygame.image.load(heli1).convert_alpha()
        heli2=pygame.image.load(heli2).convert_alpha()
        heli3=pygame.image.load(heli3).convert_alpha()
        heli4=pygame.image.load(heli4).convert_alpha()
        heli5=pygame.image.load(heli5).convert_alpha()
        back1=pygame.image.load(back1).convert()
        back2=pygame.image.load(back2).convert()
        back3=pygame.image.load(back3).convert()
        back4=pygame.image.load(back4).convert()
        jumla_khalanga_bazzar=pygame.image.load(jumla_khalanga_bazzar).convert()
        rara_lake=pygame.image.load(rara_lake).convert()
        shey_phoksundo=pygame.image.load(shey_phoksundo).convert()
        surkhet=pygame.image.load(surkhet).convert()
        swargadwari=pygame.image.load(swargadwari).convert()
        txt_cloud=pygame.image.load(txt_cloud).convert_alpha()
        down=pygame.image.load(down).convert_alpha()
        up=pygame.image.load(up).convert_alpha()
        crash=pygame.image.load(crash).convert()


        ##initializing variables
        score=0
        myfont = pygame.font.SysFont("Arial",19)
        largefont = pygame.font.SysFont("Arial",25)
        count=1
        c=random.randint(150,650)
        st=800
        p=0
        x=200
        y=300
        b=0
        c=random.randint(150,650)
        clock=pygame.time.Clock()
        speed=250
        secc=0
        mx=0
        my=0
        flag=0



        ##loop for background
        while 1:
                
                ##for backgrounnd
                if b==0:
                        bg=back1
                elif b==1:
                        bg=back2
                elif b==2:
                        bg=back3
                elif b==3:
                        bg=back4
                if (count==1):
                        screen.blit(surkhet,(0,0))
                        screen.blit(txt_cloud,(1,1))
                        txt1="Welcome to MWDR.This is surkhet airport. I am your guide for this helicopter trip."
                        txt2="You have to fly the helicopter through the obstacles using the arrow key <<SPACE TO CONTINUE>>"
                        label1=myfont.render(txt1, 1, (255,0,0))
                        label2=myfont.render(txt2, 1, (255,0,0))
                        screen.blit(label1,(15,15))
                        screen.blit(label2,(15,45))
                        for event in pygame.event.get():
                            if ((event.type == KEYDOWN and event.key==K_SPACE)):
                                flag=1
                                temp=count+1
                                score=0
                                count=0
                if (count==2):
                        screen.blit(swargadwari,(0,0))
                        screen.blit(txt_cloud,(1,1))
                        txt1="This is Swargadwari Temple. It is one of the most sacred places of the MWDR."
                        txt2="Here lies a fire that is believed never to be extinguished.<<SPACE TO CONTINUE>>"
                        label1=myfont.render(txt1, 1, (255,0,0))
                        label2=myfont.render(txt2, 1, (255,0,0))
                        screen.blit(label1,(15,15))
                        screen.blit(label2,(15,45))
                        for event in pygame.event.get():
                            if ((event.type == KEYDOWN and event.key==K_SPACE)):
                                flag=1
                                temp=count+1
                                count=0
                                score=0
                                b=b+1
                if (count==3):
                        screen.blit(shey_phoksundo,(0,0))
                        screen.blit(txt_cloud,(1,1))
                        txt1="This is an overview of Shey Phoksundo National Park."
                        txt2="Some of the endangered species found here are: Snow leaopard, Musk Dear, Red Panda <<SPACE TO COBTINUE>>."
                        label1=myfont.render(txt1, 1, (255,0,0))
                        label2=myfont.render(txt2, 1, (255,0,0))
                        screen.blit(label1,(15,15))
                        screen.blit(label2,(15,45))
                        for event in pygame.event.get():
                            if ((event.type == KEYDOWN and event.key==K_SPACE)):
                                flag=1
                                score=0
                                temp=count+1
                                count=0
                                b=b+1
                if (count==4):
                        screen.blit(rara_lake,(0,0))
                        screen.blit(txt_cloud,(1,1))
                        txt1="This is the Rara lake. It is one of the most popular lakes of MWDR"
                        txt2="<<SPACE TO CONTINUE>>"
                        label1=myfont.render(txt1, 1, (255,0,0))
                        label2=myfont.render(txt2, 1, (255,0,0))
                        screen.blit(label1,(15,15))
                        screen.blit(label2,(15,45))
                        for event in pygame.event.get():
                            if ((event.type == KEYDOWN and event.key==K_SPACE)):
                                flag=1
                                score=0
                                temp=count+1
                                count=0
                                b=b+1
                if (count==5):
                        screen.blit(jumla_khalanga_bazzar,(0,0))
                        screen.blit(txt_cloud,(1,1))
                        txt1="Welcome to MWDR.This is surkhet airport. I am your guide for this helicopter trip."
                        txt2="You have to fly the helicopter through the obstacles using the arrow key."
                        label1=myfont.render(txt1, 1, (255,0,0))
                        label2=myfont.render(txt2, 1, (255,0,0))
                        screen.blit(label1,(15,15))
                        screen.blit(label2,(15,45))
                        for event in pygame.event.get():
                            if ((event.type == KEYDOWN and event.key==K_SPACE)):
                                flag=1
                                score=0
                                temp=count+1
                                count=0
                                b=b+1
                                pygame.mixer.music.pause()
                                return 

                if flag==1:
                        #for helicopter
                        if st<=-90:
                                c=random.randint(150,650)
                                st=600
                        screen.blit(bg,(0,0))
                        if p==0:
                            screen.blit(heli1,(x,y))
                            p=1
                        elif p==1:
                            screen.blit(heli2,(x,y))
                            p=2
                        elif p==2:
                            screen.blit(heli3,(x,y))
                            p=3
                        elif p==3:
                            screen.blit(heli4,(x,y))
                            p=4
                        elif p==4:
                            screen.blit(heli5,(x,y))
                            p=0




                        ##event handeling
                        for event in pygame.event.get():
                                if (event.type == QUIT):
                                        pygame.quit()
                                        sys.exit()
                                if (event.type==KEYDOWN):
                                        if (event.key==K_DOWN):
                                                my=+.5
                                        elif (event.key==(K_UP)):
                                                my=-.5
                                if (event.type==KEYUP):
                                        if (event.key==K_DOWN):
                                                my=0
                                        elif (event.key==(K_UP)):
                                                my=0




                        ##blitting images and initializing variables
                        screen.blit(up,(st,(c-900)))
                        screen.blit(down,(st,c))
                        milli=clock.tick()
                        sec=milli/1000.
                        dis=sec*speed
                        st-=dis
                        s=st/1
                        s=int(s)
                        
                        


                        lbscore1=myfont.render("score:",1,(0,0,0))
                        lbscore2=myfont.render(str(score),1,(0,0,0))
                        screen.blit(lbscore1,(720,0))
                        screen.blit(lbscore2,(765,0))
                        ##increasing score and displaying fail message
                        if (x in range (s-50,s+50)):
                                score=score+1
                                if (((y+52)*2) in range (c*2,1200)) or (y*2 in range (0,(c-200)*2)):
                                        txt="SORRY!!! U DIDNT MAKE IT!!! :( TRY AGAIN"
                                        screen.blit(crash,(0,0))
                                        label=largefont.render(txt, 1, (0,0,0))
                                        screen.blit (label,(400,300))
                                        score=0
                        if score in range(400,500):
                                count=temp
                                flag=0

                        y+=my
                pygame.display.update()
                if y<0:
                        y=0
                if y>(600-52):
                        y=(600-52)

