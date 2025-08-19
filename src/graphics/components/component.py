from dataclasses import dataclass

from graphics.common.enums import AnchorTypeEnum


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

    @staticmethod
    def navy() -> "Color":
        return Color(r=67, g=56, b=202, a=255)

    @staticmethod
    def light_purple() -> "Color":
        return Color(r=139, g=92, b=246, a=255)

    def gradient(self, other: "Color", p: float) -> "Color":
        return Color(
            r=int(self.r * p + other.r * (1 - p)),
            g=int(self.g * p + other.g * (1 - p)),
            b=int(self.b * p + other.b * (1 - p)),
            a=int(self.a * p + other.a * (1 - p)),
        )

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
    max_length: int | None = None


@dataclass
class Anchor(Component):
    anchor: AnchorTypeEnum
