import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int) -> None:
        super().__init__()
        self.sprite_sheet = pygame.image.load('assets/player.png')
        self.image = pygame.transform.scale(self.get_image(0, 0), (16, 16))
        self.image.set_colorkey((0, 0, 0))
        self.rect: pygame.Rect = self.image.get_rect()

        self.images = {
            'down': [pygame.transform.scale(self.get_image(x*32, 0), (16, 16)) for x in range(3)],
            'left': [pygame.transform.scale(self.get_image(x*32, 32), (16, 16)) for x in range(3)],
            'right': [pygame.transform.scale(self.get_image(x*32, 64), (16, 16)) for x in range(3)],
            'up': [pygame.transform.scale(self.get_image(x*32, 96), (16, 16)) for x in range(3)]

        }
        self.image_index = 0
        self.image_reverse_cycle = False
        self.position: list[float] = [x, y]
        self.speed: float = 1
        self.direction = 'down'

    def change_image(self, direction: str, moving=True):
        if not moving:
            self.image = self.images[direction][1]
            self.image.set_colorkey((0, 0, 0))
            return

        self.image = self.images[direction][int(self.image_index // 10)]
        self.image_index += (-1) ** self.image_reverse_cycle * self.speed
        print(self.image_index)
        if self.image_index >= len(self.images[direction]) * 10:
            self.image_reverse_cycle = True
            self.image_index = len(self.images[direction]) * 10 - 1 
        elif self.image_index <= 0:
            self.image_reverse_cycle = False
            self.image_index = 0
        self.image.set_colorkey((0, 0, 0))

    def move_right(self):
        self.position[0] += self.speed

    def move_left(self):
        self.position[0] -= self.speed

    def move_up(self):
        self.position[1] -= self.speed

    def move_down(self):
        self.position[1] += self.speed

    def update(self) -> None:
        self.rect.topleft = self.position

    def get_image(self, x, y):
        image = pygame.Surface([32, 32])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 32, 32))
        return image
