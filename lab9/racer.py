import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 500, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer with Coins & Enemies")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


bg_img = pygame.image.load("road.png")  #background(road)
car_img = pygame.image.load("car.png")
coin_img = pygame.image.load("coin.png")
silver_coin_img = pygame.image.load("s_coin.png")
enemy_img = pygame.image.load("Enemy.png")


bg_img = pygame.transform.scale(bg_img, (WIDTH, HEIGHT))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(car_img, (50, 100))
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT - 120))
        self.speed = 5

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed

class Enemy(pygame.sprite.Sprite):
    def __init__(self, speed):
        super().__init__()
        self.image = pygame.transform.scale(enemy_img, (50, 100))
        self.rect = self.image.get_rect(center=(random.randint(50, WIDTH - 50), -100))
        self.speed = speed

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.rect.y = -100
            self.rect.x = random.randint(50, WIDTH - 50)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        coin_type = random.choice(["gold", "silver"])
        if coin_type == "gold":
            self.image = pygame.transform.scale(coin_img, (30, 30))
            self.value = 1
        else:
            self.image = pygame.transform.scale(silver_coin_img, (30, 30))
            self.value = 2
        self.rect = self.image.get_rect(center=(random.randint(50, WIDTH - 50), 0))
        self.speed = 3

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.kill()


ADD_COIN = pygame.USEREVENT + 1
ADD_ENEMY = pygame.USEREVENT + 2
pygame.time.set_timer(ADD_COIN, 1000)
pygame.time.set_timer(ADD_ENEMY, 2000)

player = Player()
coins = pygame.sprite.Group()
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group(player)
coin_count = 0
enemy_speed = 3
N = 10

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 30)
running = True

while running:
    win.blit(bg_img, (0, 0))  # background

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == ADD_COIN:
            coin = Coin()
            coins.add(coin)
            all_sprites.add(coin)

        if event.type == ADD_ENEMY:
            
            new_enemy = Enemy(enemy_speed)
            overlap = False
            for enemy in enemies:
                if new_enemy.rect.colliderect(enemy.rect.inflate(0, 20)):
                    overlap = True
                    break
            if not overlap:
                enemies.add(new_enemy)
                all_sprites.add(new_enemy)

    player.move()
    coins.update()
    enemies.update()


    collected_coins = pygame.sprite.spritecollide(player, coins, True)
    for coin in collected_coins:
        coin_count += coin.value

    
    if pygame.sprite.spritecollideany(player, enemies):
        text = font.render("Game Over!", True, (255, 0, 0))
        win.blit(text, (WIDTH // 2 - 80, HEIGHT // 2))
        pygame.display.update()
        pygame.time.wait(2000)
        pygame.quit()
        sys.exit()

    
    if coin_count >= N:
        enemy_speed = 5

    all_sprites.draw(win)

    # show coins numbers
    text = font.render(f"Coins: {coin_count}", True, BLACK)
    win.blit(text, (350, 10))

    pygame.display.update()
    clock.tick(60)


