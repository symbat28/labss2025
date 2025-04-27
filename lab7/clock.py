import pygame
import time
import os

pygame.init()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

WHITE = (255, 255, 255)


base_path = os.path.dirname(os.path.abspath(__file__))


clock_face = pygame.image.load(os.path.join(base_path, "clock.jpg"))
clock_face = pygame.transform.scale(clock_face, (300, 300))

minute_hand = pygame.image.load(os.path.join(base_path, "right_hand.png"))
second_hand = pygame.image.load(os.path.join(base_path, "left_hand.png"))

minute_hand = pygame.transform.scale(minute_hand, (300, 200))
second_hand = pygame.transform.scale(second_hand, (300, 200))


center_x, center_y = WIDTH // 2, HEIGHT // 2


clock = pygame.time.Clock()

running = True
while running:
    screen.fill(WHITE)

    t = time.localtime()
    minute = t.tm_min
    second = t.tm_sec

    
    minute_angle = -(minute * 6)
    second_angle = -(second * 6)

    rotated_minute = pygame.transform.rotate(minute_hand, minute_angle)
    rotated_second = pygame.transform.rotate(second_hand, second_angle)

    min_rect = rotated_minute.get_rect(center=(center_x, center_y))
    sec_rect = rotated_second.get_rect(center=(center_x, center_y))

    screen.blit(clock_face, (center_x - 150, center_y - 150))
    screen.blit(rotated_minute, min_rect.topleft)
    screen.blit(rotated_second, sec_rect.topleft)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(1)  

pygame.quit()

