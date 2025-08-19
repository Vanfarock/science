import pygame

from graphics.screen import Screen
from graphics.systems.movement import MovementSystem
from graphics.systems.render import RenderSystem
from graphics.systems.system import System
from graphics.systems.trail import TrailSystem
from graphics.world import World

pygame.init()


class View:
    def __init__(self, world: World, width: int, height: int, fps: int = 60) -> None:
        self.width = width
        self.height = height
        self.screen = Screen(pygame.display.set_mode((width, height)))
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.running = False

        self.world = world
        self.systems: list[System] = []

    def add_system(self, system: System) -> None:
        self.systems.append(system)

    def show(self) -> None:
        self.systems.append(TrailSystem(self.screen))
        self.systems.append(MovementSystem())
        self.systems.append(RenderSystem(self.screen))
        self.world.systems.extend(self.systems)

        self.running = True

        while self.running:
            dt = self.clock.tick(self.fps) / 1_000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.clear()

            self.world.update(dt)

            self.screen.update()

        self.quit()

    def quit(self) -> None:
        pygame.quit()
