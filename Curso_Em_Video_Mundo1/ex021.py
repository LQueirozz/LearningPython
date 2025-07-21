#CHALLENGE 21: Playing mp3
#GOAL: Write code that plays an mp3 file
#SKILL: Learning about importations

import pygame

pygame.init()
pygame.mixer.music.load('ParabensGP.mp3')
pygame.mixer.music.play()
a= input('The song will play until you press "ENTER" ')