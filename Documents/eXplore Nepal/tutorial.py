def tutorial():
    import pygame
    import sys
    from pygame.locals import*
    pygame.init()
    
    frame2="Photographs/frame_001.png"
    frame3="Photographs/frame_002.png"
    frame4="Photographs/frame_003.png"
    frame5="Photographs/frame_004.png"
    frame6="Photographs/frame_005.png"
    frame7="Photographs/frame_006.png"
    
    screen=pygame.display.set_mode((800,600),pygame.FULLSCREEN)
    
    two=pygame.image.load(frame2).convert_alpha()
    three=pygame.image.load(frame3).convert_alpha()
    four=pygame.image.load(frame4).convert_alpha()
    five=pygame.image.load(frame5).convert_alpha()
    six=pygame.image.load(frame6).convert_alpha()
    seven=pygame.image.load(frame7).convert_alpha()
    
    
    two=pygame.transform.scale(two,(800,600))
    three=pygame.transform.scale(three,(800,600))
    four=pygame.transform.scale(four,(800,600))
    five=pygame.transform.scale(five,(800,600))
    six=pygame.transform.scale(six,(800,600))
    seven=pygame.transform.scale(seven,(800,600))
    
    flag=False
    clock=pygame.time.Clock()
    secs=0
    sec=0
    n=2
    pygame.mixer.music.load('Photographs/bgforgame.mp3')
    pygame.mixer.music.play(1,1)
    seconds=0
    while True:
        font = pygame.font.SysFont('Arial',30)
        title = font.render("Press SPACE TO SKIP", True,(255,0,0))
        
        milli=clock.tick()
        
        sec=milli
        secs+=sec
        seconds+=sec
        minute=seconds/60.
        
        
        if (int (secs))% 3000 in range(0,500):
                screen.blit(two,(0,0))
                
        elif (int (secs))% 3000 in range(500,1000):
                screen.blit(three,(0,0))
        elif (int (secs))% 3000 in range (1000,1500):
                screen.blit(four,(0,0))
        
        elif (int (secs))% 3000 in range (1500,2000):
                screen.blit(five,(0,0))
        elif (int (secs))% 3000 in range (2000,2500):
                screen.blit(six,(0,0))
                
        else:
                screen.blit(seven,(0,0))
                secs=0
        screen.blit(title,(30,30))
        if minute>1880.0:
            pygame.mixer.music.pause()
            return
            
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==KEYDOWN and event.key==K_SPACE or (event.type==KEYUP and event.key==K_SPACE):
                pygame.mixer.music.pause()
                return
            
        pygame.display.update()   

