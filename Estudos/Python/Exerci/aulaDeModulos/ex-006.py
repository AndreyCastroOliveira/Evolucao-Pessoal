#Crie um progrma que abra e reproduza um arquivo mp3

import pygame

pygame.init()
pygame.mixer.music.load('musica.mp3')
pygame.mixer.music.play()
pygame.event.wait()

#incompleto