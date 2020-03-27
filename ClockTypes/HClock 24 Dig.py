#!/usr/bin/env python3
# Addapted by BitMan64 for Holoclock
# Thanks to CoolCat467 for his Original MirrorText Program.

SCREENSIZE = (800, 480)
NAME = '24HHClock'
__version__ = '5.0.1'

FPS = 10
WHITE = (100, 255, 0)
BLACK = (0, 0, 0)

import pygame
from pygame.locals import *
import sys
import time

def GetTime():
    h = time.strftime("%H")
    m = time.strftime("%M")
    s = time.strftime("%S")
    timenow = [h,":",m,":",s]
    return timenow
    


def run():
    pygame.init()
    
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode(SCREENSIZE, 0, 32)
    pygame.display.set_caption(NAME)
    
    font = pygame.font.SysFont('', 32)
    font_height = font.get_linesize()
    
    display_text = GetTime()
    RUNNING = True
    while RUNNING:
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                pygame.quit()
                RUNNING = False

        screen = pygame.display.set_mode(SCREENSIZE, 0, 32)
        pygame.display.set_caption(NAME)
    
        font = pygame.font.SysFont('digital-7', 280)
        font_height = font.get_linesize()
    
        display_text = GetTime()
        clock.tick(FPS)
        screen.fill(BLACK)
        
        HTIME = ''
        for i in display_text:
            HTIME = HTIME + str(i)

        text_surf = font.render( HTIME, True, WHITE)
        SURFACER = text_surf.get_rect()
        SURFACER.center=(400,240)
        flipped_surf = pygame.transform.flip(text_surf, 1, 0)
        screen.blit( flipped_surf, SURFACER)
        #y += font_height
        
        pygame.display.update()
    pygame.quit()

if __name__ == '__main__':
    run()
