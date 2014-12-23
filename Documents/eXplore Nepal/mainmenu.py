#!/usr/bin/env python
import pygame
import sys
from pygame.locals import*
from pratik import*
from high import*
import inputbox
pygame.init()

BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 120, 230,20)
RED = ( 255, 0, 0)

c=secs=0


screen = pygame.display.set_mode((800,600),pygame.FULLSCREEN)

manche=pygame.image.load("data/a.png").convert_alpha()
mina=pygame.image.load("data/mina.png").convert_alpha()
mumin=pygame.image.load("data/mumin.png").convert_alpha()
title=pygame.image.load("data/image.png").convert_alpha()
background=pygame.image.load("data/background.jpg").convert_alpha()
hover=pygame.image.load("data/hover.png").convert_alpha()
flags=pygame.image.load("data/flag.png").convert_alpha()
speed=200
clock=pygame.time.Clock()   
flag=False
pygame.mixer.music.load('data/background.mp3')
pygame.mixer.music.play(-1,2)                

def main():
    global flag,px,py

    while True:
        
        screen.blit(background,(0,0))
        screen.blit(flags,(590,96))
        screen.blit(mina,(30,419))
        screen.blit(manche,(350,448))
        screen.blit(mumin,(670,469))
        
        screen.blit(title,(20,10))
        for event in pygame.event.get(): # User did something

            if event.type==QUIT:
                    pygame.quit()
                    sys.exit()
        mousex,mousey=pygame.mouse.get_pos()
       
                    
                    
        
        if mousex in range(0,290) and mousey in range(400,600)  :
            
            play()
                        
        elif mousex in range(300,630) and mousey in range(500,600):
            
            how_to_play()
                        
        elif mousex in range(650,800) and mousey in range(500,600):
            
            end()
                    
                   
        pygame.display.update()
    


def play():
                
                global screen,hover
                font = pygame.font.SysFont('Arial',74)
                title = font.render("Play Game", True, RED)
                screen.blit(title,(45,160))
                screen.blit(hover,(15,100))
                pygame.draw.circle(screen, GREEN, (125,510), 122, 30)
                
                for event in pygame.event.get(): # User did something
                   
                    if event.type == pygame.MOUSEBUTTONDOWN or event.type==pygame.MOUSEBUTTONUP:
                        
                        print "You pressed play game"
                        answer = inputbox.ask(screen, "Your name")
                        
                        pygame.mixer.music.stop()
                        pratik(answer)
                        
                    else:
                        break
                    
                    

                secs=0
                milli=clock.tick()
                sec=milli/1000.
                secs+=sec
                d=speed*sec*0.5
                
                                



def how_to_play():
    
    
    global screen,hover
    font = pygame.font.SysFont('Arial',72)
    title = font.render("View Scores", True, RED)
    screen.blit(title,(130,160))
    pygame.draw.circle(screen, RED, (428,510), 100, 30)
    screen.blit(hover,(100,100))
    for event in pygame.event.get(): # User did something
                    
                    if event.type == pygame.MOUSEBUTTONDOWN or event.type==pygame.MOUSEBUTTONUP:
                        high()
                        main()
                    else:
                        break
    secs=0
    milli=clock.tick()
    sec=milli/1000.
    secs+=sec
    d=speed*sec
        
   
    
                
def end():
    
    global screen,hover
    font = pygame.font.SysFont('Arial',80)
    title = font.render("Quit", True, RED)
    screen.blit(title,(300,160))
    pygame.draw.circle(screen, BLACK, (728,510), 100, 30)
    screen.blit(hover,(175,100))
    for event in pygame.event.get(): # User did something
               
                if event.type == pygame.MOUSEBUTTONDOWN or event.type==pygame.MOUSEBUTTONUP:
                                      
                   
                    pygame.quit()
                    sys.exit()
                else:
                    break
                
    secs=0
    milli=clock.tick()
    sec=milli/1000.
    secs+=sec
    d=speed*sec
    
    

    
main()
