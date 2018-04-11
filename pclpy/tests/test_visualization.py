import os
import numpy as np
import pytest

import pclpy
from pclpy import pcl


def test_data(*args):
    return os.path.join("test_data", *args)


def test_cloud_viewer():
    pc = pclpy.io.read_las(test_data("street.las"))
    viewer = pcl.visualization.CloudViewer("viewer")
    viewer.show_cloud(pc, "hi")
    # while not viewer.was_stopped(1):
    #     pass


def test_pcl_visualizer_simple():
    pc = pclpy.io.read_las(test_data("street.las"), read_colors=False)
    viewer = pcl.visualization.PCLVisualizer("viewer")
    viewer.set_background_color(0, 0, 0, 0)
    print(dir(pcl.visualization))
    viewer.add_point_cloud(pc, "sample cloud")
    viewer.set_point_cloud_rendering_properties(pcl.visualization.PCL_VISUALIZER_POINT_SIZE, 3, "sample cloud")
    viewer.add_coordinate_system(1.0)
    viewer.init_camera_parameters()

    while not viewer.was_stopped(100):
        pass
