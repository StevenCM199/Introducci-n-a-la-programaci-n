import sys, pygame
import random
from pygame.locals import *
from math import *
import json
from tkinter import *
from Verificar import*
from Registrar import*

pygame.init()

WIDTH  = 1156
HEIGHT = 650
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
FPS    = pygame.time.Clock()

pygame.display.set_caption('PyDeathRace')

pista = pygame.transform.scale(pygame.image.load('Menu.png').convert(),(WIDTH,HEIGHT))

def menu ():
    
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == K_e:
                Menu2 ()
            if event.key == K_r:
                Menu1 ()


def main():

   while True:
        
        #Test if the game has been quit
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        SCREEN.blit(pista,(0,0))
        menu ()



        pygame.display.update()
        FPS.tick(60)
        
if __name__ == '__main__': main()
