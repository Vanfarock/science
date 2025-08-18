from dataclasses import dataclass


@dataclass
class Component:
    pass


@dataclass
class Color(Component):
    r: int
    g: int
    b: int
    a: int

    @staticmethod
    def white() -> "Color":
        return Color(r=255, g=255, b=255, a=255)

    @staticmethod
    def black() -> "Color":
        return Color(r=0, g=0, b=0, a=255)

    @staticmethod
    def red() -> "Color":
        return Color(r=255, g=0, b=0, a=255)

    def to_tuple(self) -> tuple[int, int, int, int]:
        return (self.r, self.g, self.b, self.a)


@dataclass
class Position(Component):
    x: float
    y: float


@dataclass
class Velocity(Component):
    dx: float
    dy: float


@dataclass
class Size(Component):
    width: float
    height: float


@dataclass
class Thickness(Component):
    value: float


@dataclass
class Trail(Component):
    color: Color
    thickness: Thickness
    history: list[Position]
