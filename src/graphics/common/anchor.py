from graphics.common.enums import AnchorTypeEnum
from graphics.components.component import Position, Size


def get_anchored_position(
    position: Position, size: Size, anchor: AnchorTypeEnum
) -> Position:
    dx = 0.0
    dy = 0.0
    match anchor:
        case AnchorTypeEnum.TOP_LEFT:
            dx = 0
            dy = 0
        case AnchorTypeEnum.TOP_CENTER:
            dx = -size.width / 2
            dy = 0
        case AnchorTypeEnum.TOP_RIGHT:
            dx = -size.width
            dy = 0
        case AnchorTypeEnum.CENTER_LEFT:
            dx = 0
            dy = -size.height / 2
        case AnchorTypeEnum.CENTER:
            dx = size.width / 2
            dy = size.height / 2
        case AnchorTypeEnum.CENTER_RIGHT:
            dx = -size.width
            dy = -size.height / 2
        case AnchorTypeEnum.BOTTOM_LEFT:
            dx = 0
            dy = -size.height
        case AnchorTypeEnum.BOTTOM_CENTER:
            dx = -size.width / 2
            dy = -size.height
        case AnchorTypeEnum.BOTTOM_RIGHT:
            dx = -size.width
            dy = -size.height
    return Position(x=position.x + dx, y=position.y + dy)
