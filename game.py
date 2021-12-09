import typing

import pyscroll
import pygame
from pytmx.util_pygame import load_pygame

from player import Player


if typing.TYPE_CHECKING:
    from pygame.event import Event
    from pygame.surface import Surface


class Game:
    size: tuple[int, int]
    width: int
    heigth: int

    size = width, height = 640, 640

    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("A lowcost copy of pokemon !")

        self.clock = pygame.time.Clock()
        self.screen: 'Surface' = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        tmxdata = load_pygame("map.tmx")
        map_data = pyscroll.data.TiledMapData(tmxdata)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 4

        player_position = tmxdata.get_object_by_name('player')
        self.player = Player(player_position.x, player_position.y)

        self.group = pyscroll.group.PyscrollGroup(map_layer=map_layer, default_layer=3)
        self.group.add(self.player)

    def handle_input(self) -> None:
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_a]:
            self.player.speed = 1.35
        else:
            self.player.speed = 1

        if pressed[pygame.K_UP]:
            self.player.direction = 'up'
            self.player.move_up()
            self.player.change_image('up', True)
        elif pressed[pygame.K_DOWN]:
            self.player.direction = 'down'
            self.player.move_down()
            self.player.change_image('down', True)
        elif pressed[pygame.K_LEFT]:
            self.player.direction = 'left'
            self.player.move_left()
            self.player.change_image('left', True)
        elif pressed[pygame.K_RIGHT]:
            self.player.direction = 'right'
            self.player.move_right()
            self.player.change_image('right', True)
        else:
            self.player.change_image(self.player.direction, False)

    def get_center(self) -> tuple[int, int]:
        return (self.width // 2, self.height // 2)

    def loop(self) -> None:
        while True:
            self.handle_input()
            self.player.update()
            self.group.center(self.player.rect.center)
            self.group.draw(self.screen)
            pygame.display.flip()
            for event in pygame.event.get():
                self.on_event(event)

            self.clock.tick(60)

    def on_event(self, event: 'Event') -> None:
        if event.type == pygame.QUIT:
            self.quit()

    def quit(self) -> None:
        print('Bye !')
        pygame.quit()
        exit()
