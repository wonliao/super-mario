import pygame

# 遊戲設定
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
FPS = 60
GRAVITY = 0.8

# 顏色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 200)

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("超級瑪莉歐 Demo")
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((32, 32))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.vel_y = 0
        self.on_ground = False

    def update(self, tiles):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 4
        if keys[pygame.K_RIGHT]:
            self.rect.x += 4
        if keys[pygame.K_SPACE] and self.on_ground:
            self.vel_y = -12
            self.on_ground = False

        self.vel_y += GRAVITY
        self.rect.y += self.vel_y

        # 碰撞檢查
        self.on_ground = False
        for tile in tiles:
            if self.rect.colliderect(tile):
                if self.vel_y > 0:
                    self.rect.bottom = tile.top
                    self.vel_y = 0
                    self.on_ground = True

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((32, 32))
        self.image.fill(RED)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.direction = 1

    def update(self, tiles):
        self.rect.x += self.direction * 2
        for tile in tiles:
            if self.rect.colliderect(tile):
                if self.direction > 0:
                    self.rect.right = tile.left
                else:
                    self.rect.left = tile.right
                self.direction *= -1
                break

class Mushroom(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((28, 28))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect(center=(x, y))


def create_level():
    tiles = []
    enemies = pygame.sprite.Group()
    items = pygame.sprite.Group()

    # 地板
    for i in range(20):
        rect = pygame.Rect(i * 32, SCREEN_HEIGHT - 32, 32, 32)
        tiles.append(rect)

    # 簡易障礙與敵人
    block = pygame.Rect(200, SCREEN_HEIGHT - 96, 64, 32)
    tiles.append(block)
    enemies.add(Enemy(300, SCREEN_HEIGHT - 64))
    items.add(Mushroom(220, SCREEN_HEIGHT - 128))
    return tiles, enemies, items


def main():
    tiles, enemies, items = create_level()
    player = Player(50, SCREEN_HEIGHT - 64)
    all_sprites = pygame.sprite.Group(player, enemies, items)
    score = 0

    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player.update(tiles)
        enemies.update(tiles)

        # 敵人碰撞
        if pygame.sprite.spritecollide(player, enemies, False):
            print("遊戲結束！")
            running = False

        # 吃香菇
        hit_items = pygame.sprite.spritecollide(player, items, True)
        if hit_items:
            score += 10
            print(f"取得香菇！當前分數：{score}")

        screen.fill(WHITE)
        for tile in tiles:
            pygame.draw.rect(screen, BLACK, tile)
        all_sprites.draw(screen)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
