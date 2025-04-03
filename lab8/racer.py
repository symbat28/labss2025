import pygame
import random

pygame.init()

WIDTH, HEIGHT = 500, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer with Coins")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)


car_img = pygame.image.load("car.png")
coin_img = pygame.image.load("coin.png")

# cars
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

#coins
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(coin_img, (30, 30))
        self.rect = self.image.get_rect(center=(random.randint(50, WIDTH - 50), 0))
        self.speed = 3

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.kill()


ADD_COIN = pygame.USEREVENT + 1
pygame.time.set_timer(ADD_COIN, 1000)

# pleyer while 
player = Player()
coins = pygame.sprite.Group()
all_sprites = pygame.sprite.Group(player)
coin_count = 0

clock = pygame.time.Clock()
running = True
while running:
    win.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == ADD_COIN:
            coin = Coin()
            coins.add(coin)
            all_sprites.add(coin)

    player.move()
    coins.update()
    
    # 
    collected_coins = pygame.sprite.spritecollide(player, coins, True)
    coin_count += len(collected_coins)

    #draw
    all_sprites.draw(win)
    
    
    font = pygame.font.SysFont("Arial", 30)
    text = font.render(f"Coins: {coin_count}", True, BLACK)
    win.blit(text, (350, 10))
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()
