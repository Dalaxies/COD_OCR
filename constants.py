from readers.screen import BoundingBox
from readers.screen import Coordinate


class Images:
    MENU = "images/menu.png"
    ALLIANCE = "images/menu_alliance.png"
    ALLIANCE_SETTINGS = "images/menu_alliance_settings.png"
    ALLIANCE_RANKINGS = "images/menu_alliance_rankings.png"
    COPY_NAME = "images/copy_name.png"
    RANKINGS_INTERFACE = "images/rankings.png"
    INFO_BUTTON = "images/info_top_right.png"
    OWN_POSITION = "images/rankings_own_entry.png"


class BoundingBoxes:
    POWER = BoundingBox(min_x=450, min_y=205, max_x=700, max_y=245)
    MERIT = BoundingBox(min_x=900, min_y=205, max_x=1140, max_y=245)
    LORD_ID = BoundingBox(min_x=240, min_y=295, max_x=355, max_y=320)
    ALLIANCE_MEMBERS = BoundingBox(min_x=360, min_y=595, max_x=460, max_y=625)
    ALLIANCE_NAME = BoundingBox(min_x=100, min_y=415, max_x=450, max_y=455)
    OWN_POSITION = BoundingBox(min_x=0, min_y=0, max_x=69, max_y=69)


class Coordinates:
    MENU_TOGGLE = Coordinate(1237, 660)
    OPEN_ALLIANCE = Coordinate(960, 667)
    OPEN_ALLIANCE_SETTINGS = Coordinate(992, 120)
    OPEN_ALLIANCE_RANKINGS = Coordinate(570, 510)
    LIST_ENTRY = Coordinate(500, 350)
    INFO_BUTTON = Coordinate(478, 415)
    LIST_ENTRY_MIDDLE = Coordinate(800, 350)
    LIST_ENTRY_MIDDLE_UP = Coordinate(800, 259)


class Offsets:
    ENTRY_DISTANCE = 75
    INFO_BUTTON_X = 90
    INFO_BUTTON_Y = 30


def increase_list_entry_constants_by_one_entry() -> None:
    """
    Increases constants where the y position is a specific entry position in the
    rankings list by one entry.
    This is needed to skip the own entry and to reach entries at the bottom of the list.
    """
    Coordinates.LIST_ENTRY.y += Offsets.ENTRY_DISTANCE
    Coordinates.INFO_BUTTON.y += Offsets.ENTRY_DISTANCE
    Coordinates.LIST_ENTRY_MIDDLE.y += Offsets.ENTRY_DISTANCE
    Coordinates.LIST_ENTRY_MIDDLE_UP.y += Offsets.ENTRY_DISTANCE
