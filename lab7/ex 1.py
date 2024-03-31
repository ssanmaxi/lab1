import pygame
from datetime import datetime

pygame.init()
win = pygame.display.set_mode((700, 526))
pygame.display.set_caption("Mikey Mouse clock")
done = False
clock = pygame.time.Clock()

mickey = pygame.image.load(r"C:\Users\tphil\Downloads\mickeyclock.png")
minuty = pygame.image.load(r"C:\Users\tphil\Downloads\rightarm.png")
secundy = pygame.image.load(r"C:\Users\tphil\Downloads\leftarm.png")

clock_r = mickey.get_rect(center=(350, 263))
minuty_r = minuty.get_rect(center=(350, 263))
secundy_r = secundy.get_rect(center=(350, 263))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    rn = datetime.now().time()
    angle_s = rn.second * 6 #360 degs = 6*60
    angle_m = rn.minute * 60 + rn.second #3600 seconds

    rotated_secundy = pygame.transform.rotate(secundy, -angle_s)
    rotated_minuty = pygame.transform.rotate(minuty, - angle_m)

    s_r = rotated_secundy.get_rect(center=clock_r.center)
    m_r = rotated_minuty.get_rect(center=clock_r.center)
    win.blit(mickey, clock_r)
    win.blit(rotated_secundy, secundy_r)
    win.blit(rotated_minuty, minuty_r)
    pygame.display.flip()
    clock.tick(60)


