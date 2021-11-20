import pygame
import sys
from pygame.locals import *
from classes import *
pygame.init()
NOIR = (0, 0, 0)
taille = 1200, 600
pygame.display.set_caption('Angry birds')
screen = pygame.display.set_mode(taille)
clock = pygame.time.Clock()
play = True
lance = False
game = Game()
pygame.mixer.music.load('angry-birds.ogg')
pygame.mixer.music.play(-1)
background = pygame.image.load('background.png').convert_alpha()
bird = pygame.image.load('bird.png').convert_alpha()
sling = pygame.image.load('sling.png').convert_alpha()
sling2 = pygame.image.load('sling2.png').convert_alpha()
bird_rect = Rect(160, 380, 64, 64)
p0 = (220, 420)
p2 = (173, 425)
t0 = 0
while play:
    for event in pygame.event.get():
        if event.type == QUIT:
            play = False
        if event.type == MOUSEBUTTONDOWN:
            if bird_rect.collidepoint(event.pos):
                lance = True
        if event.type == MOUSEMOTION:
            if lance:
                bird_rect.move_ip(event.rel)
        if event.type == MOUSEBUTTONUP:
            lance = False
            bird_rect = pygame.Rect(160, 380, 64, 64)
            t0 = pygame.time.get_ticks() + 10
            game.launch_bird(p0, p1)
        game.do_event(event)
    #-- draw --#
    screen.blit(background, (0, 0))
    screen.blit(sling, (200, 390))
    p1 = bird_rect.move(10, 40).topleft
    pygame.draw.line(screen, NOIR, p1, p0, 4)
    t = pygame.time.get_ticks()
    if t > t0:
        screen.blit(bird, bird_rect)
    pygame.draw.line(screen, NOIR, p1, p2, 4)
    screen.blit(sling2, (170, 380))
    game.draw()
    pygame.display.flip()
    clock.tick(30)
pygame.quit()
sys.exit()
