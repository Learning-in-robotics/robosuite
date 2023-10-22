from robosuite.models.arenas import Arena
from robosuite.utils.mjcf_utils import xml_path_completion


class FloorArena(Arena):
    """Empty workspace."""

    def __init__(self):
        super().__init__(xml_path_completion("arenas/floor_arena.xml"))
