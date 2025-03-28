import pygame
pygame.init()

WIDTH,HEIGHT=(500,500)
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("move the red ball")

white=(255,255,255)
red=(255,0,0)

radius = 25
x, y = WIDTH // 2, HEIGHT // 2
step = 20

running = True
while running:
    screen.fill(white)
    pygame.draw.circle(screen, red, (x, y), radius) 
    pygame.display.flip()

for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and y - radius - step >= 0:
                y -= step
            elif event.key == pygame.K_DOWN and y + radius + step <= HEIGHT:
                y += step
            elif event.key == pygame.K_LEFT and x - radius - step >= 0:
                x -= step
            elif event.key == pygame.K_RIGHT and x + radius + step <= WIDTH:
                x += step

pygame.quit()
