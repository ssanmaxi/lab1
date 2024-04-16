import pygame
import sys

pygame.init()



screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Paint")
screen.fill((255, 255, 255))

proc = False
songy = None
brush_color = (0, 0, 0)
brush_size = 5
eraser_color = (255, 255, 255)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           pygame.quit()
           sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                proc = True
                songy = event.pos
            elif event.button == 3:  # Right mouse button for eraser
                proc = True
                songy = event.pos
                brush_color = eraser_color
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 or event.button == 3:
                proc = False
                songy = None
        elif event.type == pygame.MOUSEMOTION:
            if proc:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if songy:
                    if pygame.key.get_pressed()[pygame.K_LSHIFT]:  # Holding Shift for straight lines
                        pygame.draw.line(screen, brush_color, songy, (mouse_x, songy[1]), brush_size)
                        pygame.draw.line(screen, brush_color, songy, (songy[0], mouse_y), brush_size)
                    else:
                        pygame.draw.line(screen, brush_color, songy, (mouse_x, mouse_y), brush_size)
                songy = (mouse_x, mouse_y)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                screen.fill((255, 255, 255))
            elif event.key == pygame.K_r:
                brush_color = (255, 0, 0)  # Red color
            elif event.key == pygame.K_g:
                brush_color = (0, 255, 0)  # Green color
            elif event.key == pygame.K_b:
                brush_color = (0, 0, 255)  # Blue color
            elif event.key == pygame.K_y:
                brush_color = (255, 255, 0)  # Yellow color
            elif event.key == pygame.K_e:
                brush_color = eraser_color = (255, 255, 255)  # Eraser color same as background
            elif event.key == pygame.K_PLUS or event.key == pygame.K_KP_PLUS:
                brush_size += 1
            elif event.key == pygame.K_MINUS or event.key == pygame.K_KP_MINUS:
                brush_size = max(1, brush_size - 1)
            elif event.key == pygame.K_1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                pygame.draw.rect(screen, brush_color, pygame.Rect(mouse_x - 25, mouse_y - 25, 50, 50))  # Draw rectangle
            elif event.key == pygame.K_2:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                pygame.draw.circle(screen, brush_color, (mouse_x, mouse_y), 30)  # Draw circle

    pygame.display.flip()
