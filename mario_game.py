import os
import pygame
from pygame.locals import *

WIDTH, HEIGHT = 800, 480
GRAVITY = 0.5

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # 載入靜止、跑步與跳躍圖片
        self.image_idle = pygame.image.load(
            os.path.join("images", "mario.png")
        ).convert_alpha()
        self.image_run = pygame.image.load(
            os.path.join("images", "mario_run.png")
        ).convert_alpha()
        self.image_jump = pygame.image.load(
            os.path.join("images", "mario_jump.png")
        ).convert_alpha()

        self.image = self.image_idle
        self.rect = self.image.get_rect(topleft=(x, y))
        self.vel_y = 0
        self.on_ground = False

    def update(self, platforms):
        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            self.rect.x -= 3
        if keys[K_RIGHT]:
            self.rect.x += 3
        if keys[K_SPACE] and self.on_ground:
            self.vel_y = -10
            self.on_ground = False

        self.vel_y += GRAVITY
        self.rect.y += self.vel_y

        collisions = pygame.sprite.spritecollide(self, platforms, False)
        for platform in collisions:
            if self.vel_y > 0:
                self.rect.bottom = platform.rect.top
                self.vel_y = 0
                self.on_ground = True

        # 根據狀態切換圖片
        if not self.on_ground:
            self.image = self.image_jump
        elif keys[K_LEFT] or keys[K_RIGHT]:
            self.image = self.image_run
        else:
            self.image = self.image_idle

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        super().__init__()
        self.image = pygame.Surface((w, h))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect(topleft=(x, y))


def build_level():
    platforms = pygame.sprite.Group()
    # ground
    platforms.add(Platform(0, HEIGHT-40, WIDTH, 40))
    # simple obstacles
    platforms.add(Platform(200, HEIGHT-120, 100, 20))
    platforms.add(Platform(400, HEIGHT-200, 100, 20))
    return platforms


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Mario Demo")

    player = Player(50, HEIGHT-80)
    platforms = build_level()
    all_sprites = pygame.sprite.Group(platforms)
    all_sprites.add(player)

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        player.update(platforms)

        screen.fill((135, 206, 235))
        for sprite in all_sprites:
            screen.blit(sprite.image, sprite.rect)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
