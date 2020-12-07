import pygame
import random
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT
)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("images/jet.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
            move_up_sound.play()
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
            move_down_sound.play()
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load("images/missile.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(2, 6)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()


class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud, self).__init__()
        self.surf = pygame.image.load("images/cloud.png").convert()
        self.surf.set_colorkey((0, 0, 0,), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT)
            )
        )

    def update(self):
        self.rect.move_ip(-1, 0)
        if self.rect.right < 0:
            self.kill()

# Audio
pygame.mixer.init()

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Custom event
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)  # in miliseconds
ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 5000)

player = Player()

# create Groups
enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Add music
pygame.mixer.music.load("sound/Sky_dodge_theme.ogg")
pygame.mixer.music.play(loops=-1)
pygame.mixer.music.set_volume(0.15)

# load sound files
move_up_sound = pygame.mixer.Sound("sound/Jet_up.ogg")
move_down_sound = pygame.mixer.Sound("sound/Jet_down.ogg")
collision_sound = pygame.mixer.Sound("sound/Boom.ogg")

move_up_sound.set_volume(0.3)
move_down_sound.set_volume(0.3)

start_time = pygame.time.get_ticks()

running = True

while running:
    for e in pygame.event.get():
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                running = False

        elif e.type == QUIT:
            running = False

        # Add new enemy object
        elif e.type == ADDENEMY:
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

        # Add new cloud object
        elif e.type == ADDCLOUD:
            new_cloud = Cloud()
            clouds.add(new_cloud)
            all_sprites.add(new_cloud)

    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)

    enemies.update()
    clouds.update()

    # get time since the start of game
    seconds = round((pygame.time.get_ticks() - start_time) / 1000, 2)

    r = 100 - seconds*2.75
    g = 100 - seconds*2.75
    b = 255 - seconds*2.75

    # Fill the screen with white color
    screen.fill((r, g, b))

    # Draw surface on the screen
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)


    # display a timer on the screen
    font = pygame.font.SysFont('Consolas', 30)
    screen.blit(font.render(str(seconds), True, (255, 0, 0)), (32, 48))

    # Check if any enemies have collided with the player
    if pygame.sprite.spritecollideany(player, enemies):
        player.kill()

        #screen stop any moving sounds
        move_up_sound.stop()
        move_down_sound.stop()
        pygame.mixer.music.stop()

        pygame.time.delay(50)
        collision_sound.play()
        pygame.time.delay(500)

        # Stop the loop
        running = False

    pygame.display.flip()

    clock.tick(30) # 30 FPS

# stop music here
pygame.mixer.quit()