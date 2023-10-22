"""
Rethink's Generic Mount (Officially used on Sawyer).
"""
import numpy as np

from robosuite.models.mounts.mount_model import MountModel
from robosuite.utils.mjcf_utils import xml_path_completion

from robosuite.utils.mjcf_utils import recolor_collision_geoms


class TableMount(MountModel):
    """
    Mount officially used for Rethink's Sawyer Robot. Includes a controller box and wheeled pedestal.

    Args:
        idn (int or str): Number or some other unique identification string for this mount instance
    """

    def __init__(self, idn=0):
        super().__init__(xml_path_completion("mounts/table_mount.xml"), idn=idn)

        self.tabletop = self.worldbody.find("./body[@name='table_top']")

        WHITE = [1, 1, 1, 1]

        # Recolor all geoms
        recolor_collision_geoms(
            root=self.worldbody,
            rgba=WHITE,
            exclude=lambda e: True if e.get("name", None) == "table_top" else False,
        )

    @property
    def top_offset(self):
        return np.array((0, 0.5, 0.0))

    @property
    def horizontal_radius(self):
        # TODO: This may be inaccurate; just a placeholder for now
        return 0.0
