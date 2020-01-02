import pygame, sys
import pdb
from pygame.locals import *

#need to seperate player from client 

pygame.init()
width = 500
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

clientno = 0

class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.vel = 3
        
    def draw(self,win):
       pygame.draw.rect(win, self.color, self.rect)
       
    def move(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT]:
            self.x -= self.vel
            
        if keys[pygame.K_RIGHT]:
            self.x += self.vel
            
        if keys[pygame.K_DOWN]:
            self.y += self.vel
            
        if keys[pygame.K_UP]:
            self.y -= self.vel
        
        self.rect = (self.x, self.y, self.width, self.height)
            
            
def redrawWindow(win, player):
    win.fill((255,255,255))
    player.draw(win)
    pygame.display.update()


def main():
    
    run = True
    p = Player(50,50,100,100,(0,255,0))
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
                break
            
        pygame.init()
        p.move()        
        redrawWindow(win, p)
        
main()