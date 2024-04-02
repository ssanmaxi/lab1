import pygame
import os

pygame.init()
screen = pygame.display.set_mode((500, 200))
pygame.display.set_caption("MP3 Player")
done = False
clock = pygame.time.Clock()

song_index = 0
songs = ["C:\Users\tphil\Downloads\kzkzkz.m4a", "C:\Users\tphil\Downloads\dos.mp3"]
pygame.mixer.music.load(os.path.join("music", songs[song_index]))
play = True

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            play = not play
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            song_index = (song_index - 1) % 4
            pygame.mixer.music.stop()
            pygame.mixer.music.load(os.path.join("music", songs[song_index]))
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            song_index = (song_index + 1) % 4
            pygame.mixer.music.stop()
            pygame.mixer.music.load(os.path.join("music", songs[song_index]))
    if play:
        pygame.mixer.music.play()

    screen.fill((255, 255, 255))
    pygame.display.flip()
    clock.tick(60)

pygame.mixer.music.stop()
pygame.quit()