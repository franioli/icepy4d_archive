import numpy as np
import cv2
import logging

from typing import List

from ..core.features import Features
from ..core.camera import Camera
from ..core.images import Image, ImageDS

from .triangulation import Triangulate
from .geometry import (
    estimate_pose,
    undistort_image,
    undistort_points,
    project_points,
)
from ..matching.matching_tracking import MatchingAndTracking


class IncrementalReconstruction:
    """
    _summary_
    """

    def __init__(
        self,
        cameras: List[Camera],
        feautres: List[np.ndarray],
        preselection: str = "exaustive",
        use_tiles: bool = False,
    ) -> None:
        """
        __init__ _summary_

        Args:
            cameras (List[Camera]): _description_
            feautres (List[np.ndarray]): _description_
            preselection (str, optional): _description_. Defaults to "exaustive".
        """
        self.cameras = cameras
        self.features = feautres
        self.use_tiles = use_tiles
        self.preselection = preselection

        if len(cameras) < 4 and preselection != "exaustive":
            logging.warning(
                "Less than 4 cameras availabe. Performing exaustive preseleection"
            )

    def matching(self, cfg: dict, images: List[ImageDS], epoch_dict: dict, epoch: int):
        pass
