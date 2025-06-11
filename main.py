import pygame
import sys

# 初始化 Pygame
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Super Mario Demo")
clock = pygame.time.Clock()

# 顏色常數
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 200, 0)

# 玩家、怪物、平台尺寸
PLAYER_SIZE = (40, 50)
ENEMY_SIZE = (40, 40)
MUSHROOM_SIZE = (60, 40)
PLATFORM_HEIGHT = 20

class Entity(pygame.sprite.Sprite):
    def __init__(self, color, size, pos):
        super().__init__()
        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=pos)
        self.vel = pygame.math.Vector2(0, 0)

class Player(Entity):
    def __init__(self, pos):
        super().__init__(BLUE, PLAYER_SIZE, pos)
        self.speed = 5
        self.jump_power = -15
        self.on_ground = False
        self.is_big = False

    def grow(self):
        if not self.is_big:
            self.is_big = True
            scale_factor = 1.5
            new_size = (
                int(self.rect.width * scale_factor),
                int(self.rect.height * scale_factor),
            )
            midbottom = self.rect.midbottom
            self.image = pygame.transform.scale(self.image, new_size)
            self.rect = self.image.get_rect(midbottom=midbottom)

    def update(self, platforms):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.vel.x = -self.speed
        elif keys[pygame.K_RIGHT]:
            self.vel.x = self.speed
        else:
            self.vel.x = 0
        if keys[pygame.K_SPACE] and self.on_ground:
            self.vel.y = self.jump_power

        self.vel.y += 0.8  # 重力
        self.rect.x += self.vel.x
        self._handle_collision(platforms, 'x')
        self.rect.y += self.vel.y
        self.on_ground = False
        self._handle_collision(platforms, 'y')

    def _handle_collision(self, platforms, dir):
        for plat in platforms:
            if self.rect.colliderect(plat.rect):
                if dir == 'x':
                    if self.vel.x > 0:
                        self.rect.right = plat.rect.left
                    elif self.vel.x < 0:
                        self.rect.left = plat.rect.right
                elif dir == 'y':
                    if self.vel.y > 0:
                        self.rect.bottom = plat.rect.top
                        self.on_ground = True
                    elif self.vel.y < 0:
                        self.rect.top = plat.rect.bottom
                    self.vel.y = 0

class Enemy(Entity):
    def __init__(self, pos, movement_range):
        super().__init__(RED, ENEMY_SIZE, pos)
        self.range = movement_range
        self.start_x = pos[0]
        self.direction = 1
        self.speed = 2

    def update(self, platforms):
        self.rect.x += self.speed * self.direction
        if abs(self.rect.x - self.start_x) > self.range:
            self.direction *= 1 if self.rect.x < self.start_x else -1

class Platform(Entity):
    def __init__(self, pos, width):
        super().__init__(GREEN, (width, PLATFORM_HEIGHT), pos)

class Mushroom(Entity):
    def __init__(self, pos):
        super().__init__(YELLOW, MUSHROOM_SIZE, pos)

# 建立遊戲元素
player = Player((100, HEIGHT - 150))
enemies = pygame.sprite.Group(
    Enemy((300, HEIGHT - 110), 100),
    Enemy((600, HEIGHT - 110), 100)
)
platforms = [
    Platform((0, HEIGHT - PLATFORM_HEIGHT), WIDTH),  # 地面
    Platform((200, HEIGHT - 200), 200),
    Platform((450, HEIGHT - 300), 150)
]
platform_group = pygame.sprite.Group(platforms)
mushrooms = pygame.sprite.Group(
    Mushroom((350, HEIGHT - PLATFORM_HEIGHT - MUSHROOM_SIZE[1]))
)
all_sprites = pygame.sprite.Group([player] + platforms + list(enemies) + list(mushrooms))

# 遊戲主迴圈
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.update(platforms)
    enemies.update(platforms)
    mushrooms.update()

    if pygame.sprite.spritecollide(player, mushrooms, True):
        player.grow()

    if pygame.sprite.spritecollideany(player, enemies):
        print("遊戲結束！")
        running = False

    screen.fill(WHITE)
    for sprite in all_sprites:
        screen.blit(sprite.image, sprite.rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
