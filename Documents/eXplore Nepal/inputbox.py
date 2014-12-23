#Program to get input from the user

import pygame, pygame.font, pygame.event, pygame.draw, string
from pygame.locals import *

def get_key():
  while 1:
    event = pygame.event.poll()
    if event.type == KEYDOWN:
      return event.key
    else:
      pass

def display_box(screen, message):
  "Print a message in a box in the middle of the screen"
  fontobject = pygame.font.SysFont("Arial",32)
  pygame.draw.rect(screen, (255,0,0),
                   (400,390,
                    700,49), 0)
  
  pygame.draw.rect(screen,(255,0,0),(400,390,800,49), 5)
  if len(message) != 0:
    screen.blit(fontobject.render(message, 1, (255,255,255)),(400,390))
  pygame.display.flip()

def ask(screen, question):
  "ask(screen, question) -> answer"
  pygame.font.init()
  current_string = []
  display_box(screen, question + ": " + string.join(current_string,""))
  while 1:
    inkey = get_key()
    if inkey == K_BACKSPACE:
      current_string = current_string[0:-1]
    elif inkey == K_RETURN:
      break
    elif inkey ==K_ESCAPE:
      break
    elif inkey <= 127:
      current_string.append(chr(inkey))
    display_box(screen, question + ": " + string.join(current_string,""))
  return string.join(current_string,"")

def main():
  screen = pygame.display.set_mode((800,600))
  print ask(screen, "Your Name") 

if __name__ == '__main__': main()
