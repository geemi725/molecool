"""
Unit and regression test for the measure module
"""

import molecool
import numpy as np

def test_calculate_distance():
    r1 = np.array([0,0,0])
    r2 = np.array([0,0.1,0])
    exp_dist = 0.1

    obs_dist = molecool.calculate_distance(r1,r2)

    assert exp_dist == obs_dist
