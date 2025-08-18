import pygame

from graphics.components.component import Color


class Screen:
    def __init__(self, surface: pygame.Surface):
        self.surface = surface

    def clear(self, background_color: Color | None = None):
        background_color = background_color or Color.white()
        self.surface.fill(background_color.to_tuple())

    def update(self):
        pygame.display.flip()

    def draw_line(
        self,
        x1: float,
        y1: float,
        x2: float,
        y2: float,
        color: Color,
        thickness: int = 1,
    ):
        pygame.draw.line(self.surface, color.to_tuple(), (x1, y1), (x2, y2), thickness)

    def draw_rectangle(
        self, x: float, y: float, width: float, height: float, color: Color
    ):
        pygame.draw.rect(self.surface, color.to_tuple(), (x, y, width, height))
