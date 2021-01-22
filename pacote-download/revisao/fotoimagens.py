import pygame
import time
from PIL import Image
opcao = int(input('Opção: '))
lista = ['foto (1).jpg', 'foto (2).jpg', 'foto (3).jpg', 'foto (4).jpg', 'foto (5).jpg']
total = len(lista)
pygame.mixer.init()
pygame.init()
if opcao == 1:
    pygame.mixer.music.load('exercicio021.mp3')
    pygame.mixer.music.play()
    for c in range(0, total):
        img = Image.open(lista[c])
        img.show()
        time.sleep(2)
if opcao == 2:
    pygame.mixer.music.load('musica2.mp3')
    pygame.mixer.music.play()
pygame.event.wait()


