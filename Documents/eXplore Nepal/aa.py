def cdr():
        
        import pygame,sys
        from pygame.locals import* 
        pygame.init()
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
        back=pygame.image.load("pics_cdr/back.png").convert_alpha()
        pygame.init()
        screen=pygame.display.set_mode((800,600),pygame.FULLSCREEN)
        screen.fill((255,255,255))
        check=0
        flag=True
        
                


        while True:
            for event in pygame.event.get():
                if (event.type==QUIT) :
                    pygame.quit()
                    sys.exit()

            
            
            i1=pygame.transform.scale(bds,(200,150))
            i2=pygame.transform.scale(boudha,(200,150))
            i3=pygame.transform.scale(changu,(200,150))
            i4=pygame.transform.scale(kds,(200,150))
            i5=pygame.transform.scale(pashu,(200,150))
            i6=pygame.transform.scale(swa,(200,150))
            back1=pygame.transform.scale(back,(100,70))

            
            x1,y1=50,200
            x2,y2=300,200
            x3,y3=550,200
            x4,y4=50,400
            x5,y5=300,400
            x6,y6=550,400
            xb,yb=100,500
            
            mx,my=pygame.mouse.get_pos()
            if mx in range(x1,x1+200) and my in range(y1,y1+150):
                pygame.draw.rect(screen, BLACK, [49,199,201,151], 5)
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        
                            j1=pygame.transform.scale(bds,(800,600))
                            
                            screen.blit(j1,(0,0))
                            screen.blit(back1,(xb,yb))
                            pygame.display.update()
                            check+=1
                            
                            
                            mx1,my1=pygame.mouse.get_pos()
                            if mx1 in range(xb,xb+100) and my1 in range(yb,yb+70):
                                
                                pygame.draw.rect(screen,BLACK,(xb,yb,100,70))
                                
                                for events in pygame.event.get():
                                        
                                        if events.type== pygame.MOUSEBUTTONDOWN:     

                                                screen.blit(i1,(x1,y1))
                                                screen.blit(i2,(x2,y2))
                                                screen.blit(i3,(x3,y3))
                                                screen.blit(i4,(x4,y4))
                                                screen.blit(i5,(x5,y5))
                                                screen.blit(i6,(x6,y6))
                                                
                flag=False
                
                    
                            
                                   
                                    

            elif mx in range(x2,x2+200) and my in range(y2,y2+150):
                pygame.draw.rect(screen, BLACK, [299,199,201,151], 5)
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                            j2=pygame.transform.scale(boudha,(800,600))
                            screen.blit(j2,(0,0))
                            screen.blit(back1,(xb,yb))
                            check+=1
                            mx1,my1=pygame.mouse.get_pos()
                            if mx1 in range(xb,xb+100) and my1 in range(yb,yb+70):
                                pygame.draw.rect(screen,BLACK,(xb,yb,100,70))
                                if event.type== pygame.MOUSEBUTTONDOWN:
                                        screen.blit(i1,(x1,y1))
                                        screen.blit(i2,(x2,y2))
                                        screen.blit(i3,(x3,y3))
                                        screen.blit(i4,(x4,y4))
                                        screen.blit(i5,(x5,y5))
                                        screen.blit(i6,(x6,y6))
                flag=False
                    

            elif mx in range(x3,x3+200) and my in range(y3,y3+150):
                pygame.draw.rect(screen, BLACK, [549,199,201,151], 5)
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                            j3=pygame.transform.scale(changu,(800,600))
                            screen.blit(j3,(0,0))
                            screen.blit(back1,(xb,yb))
                            check+=1    
                            if mx in range(xb,xb+100) and my in range(yb,yb+70):
                                pygame.draw.rect(screen,BLACK,(xb,yb,100,70))
                                if event.type== pygame.MOUSEBUTTONDOWN:
                                        

                                        screen.blit(i1,(x1,y1))
                                        screen.blit(i2,(x2,y2))
                                        screen.blit(i3,(x3,y3))
                                        screen.blit(i4,(x4,y4))
                                        screen.blit(i5,(x5,y5))
                                        screen.blit(i6,(x6,y6))
                flag=False
                            
            elif mx in range(x4,x4+200) and my in range(y4,y4+150):
                pygame.draw.rect(screen, BLACK, [49,399,201,151], 5)
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                            j4=pygame.transform.scale(kds,(800,600))
                            screen.blit(j4,(0,0))
                            screen.blit(back1,(xb,yb))
                            check+=1
                            if mx in range(xb,xb+100) and my in range(yb,yb+70):
                                pygame.draw.rect(screen,BLACK,(xb,yb,100,70))
                                if event.type== pygame.MOUSEBUTTONDOWN:
                                        screen.blit(i1,(x1,y1))
                                        screen.blit(i2,(x2,y2))
                                        screen.blit(i3,(x3,y3))
                                        screen.blit(i4,(x4,y4))
                                        screen.blit(i5,(x5,y5))
                                        screen.blit(i6,(x6,y6))
                flag=False
            elif mx in range(x5,x5+200) and my in range(y5,y5+150):
                pygame.draw.rect(screen, BLACK, [299,399,201,151], 5)
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                            j5=pygame.transform.scale(pashu,(800,600))
                            screen.blit(j5,(0,0))
                            screen.blit(back1,(xb,yb))
                            check+=1
                            if mx in range(xb,xb+100) and my in range(yb,yb+70):
                                pygame.draw.rect(screen,BLACK,(xb,yb,100,70))
                                if event.type== pygame.MOUSEBUTTONDOWN:
                                    screen.blit(i1,(x1,y1))
                                    screen.blit(i2,(x2,y2))
                                    screen.blit(i3,(x3,y3))
                                    screen.blit(i4,(x4,y4))
                                    screen.blit(i5,(x5,y5))
                                    screen.blit(i6,(x6,y6))

                flag=False
            elif mx in range(x6,x6+200) and my in range(y6,y6+150):
                pygame.draw.rect(screen, BLACK, [549,399,201,151], 5)
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                            j6=pygame.transform.scale(swa,(800,600))
                            screen.blit(j6,(0,0))
                            screen.blit(back1,(xb,yb))
                            check+=1
                            if mx in range(xb,xb+100) and my in range(yb,yb+70):
                                pygame.draw.rect(screen,BLACK,(xb,yb,100,70))
                                if event.type== pygame.MOUSEBUTTONDOWN:
                                        

                                        screen.blit(i1,(x1,y1))
                                        screen.blit(i2,(x2,y2))
                                        screen.blit(i3,(x3,y3))
                                        screen.blit(i4,(x4,y4))
                                        screen.blit(i5,(x5,y5))
                                        screen.blit(i6,(x6,y6))
                flag=False
            elif flag==True:
                        
                        screen.blit(i1,(x1,y1))
                        screen.blit(i2,(x2,y2))
                        screen.blit(i3,(x3,y3))
                        screen.blit(i4,(x4,y4))
                        screen.blit(i5,(x5,y5))
                        screen.blit(i6,(x6,y6))
            pygame.display.update()

