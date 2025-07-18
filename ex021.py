#Exercício 21: tocando mp3
#Aprendendo sobre importações pt6

import pygame

pygame.init()
pygame.mixer.music.load('ParabensGP.mp3')
pygame.mixer.music.play()
a= input('A música vai tocar até você digitar "ENTER" ')