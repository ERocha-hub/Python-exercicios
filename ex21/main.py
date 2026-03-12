import pygame

def play(filename):
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy == True:
        continue

play("LAKEY INSPIRED - Chill Day [3HjG1Y4QpVA].mp3")
