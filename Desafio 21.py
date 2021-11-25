import pygame

pygame.init()
pygame.mixer.music.load('gravacao.mp3')
pygame.mixer.music.play()
pygame.event.wait()