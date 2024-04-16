import pygame
import os

pygame.display.set_caption("mp3")


def song_state_handler(command, path, state=True):
    if os.path.exists(path):

        if command == "play\\stop":
            if state == True:
                pygame.mixer.music.load(path)
                pygame.mixer.music.play(0)
            else:
                pygame.mixer.music.stop()

        elif command == "change":
            pygame.mixer.music.load(path)
            pygame.mixer.music.play(0)


path = os.path.join(os.getcwd(), "music")
songs = os.listdir(path)

pygame.init()

width, height = 500, 100
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 24)
state = True
i = 0

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                state = not state
                song_state_handler("play\\stop", path + "\\" + songs[i], state)

            if event.key == pygame.K_LEFT:
                i += 1
                i = i % len(songs)
                song_state_handler("change", path + "\\" + songs[i])

            if event.key == pygame.K_RIGHT:
                i -= 1
                i = i % len(songs)
                song_state_handler("change", path + "\\" + songs[i])

    screen.fill((255, 255, 255))

    song_name = font.render(songs[i], True, (0, 0, 0))
    screen.blit(song_name, (0, 0))

    pygame.display.flip()
    clock.tick(60)