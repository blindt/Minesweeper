import pygame, pygame.font, pygame.event, pygame.draw, string
from pygame.locals import *


def get_key():
  while 1:
    event = pygame.event.poll()
    if event.type == KEYDOWN:
      return event.key
    else:
      pass

def display_box(screen, message, ustx, usty):

  fontobject = pygame.font.Font(None,18)
  if len(message) != 0:
    screen.blit(fontobject.render(message, 1, (255,255,255)),
                (ustx+4, usty))
  pygame.display.flip()

def ask(screen, ustx, usty):
    pygame.font.init()
    current_string = []
    display_box(screen, ''.join(current_string), ustx, usty)
    while 1:
        inkey = get_key()
        if inkey == K_BACKSPACE:
            current_string = current_string[0:-1]
            pygame.draw.rect(screen, (50, 200, 50), (ustx, usty-4, 60, 24), 0)
        elif inkey == K_RETURN:
            break
        elif inkey <= 127:
            current_string.append(chr(inkey))
        display_box(screen, ''.join(current_string), ustx, usty)

    return ''.join(current_string)

