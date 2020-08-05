"""
molecool
A python package for analysing and visualizing molecular structures for MSF bootcamp
"""

# Add imports here
from .functions import *
from .measure  import calculate_distance, calculate_angle
from .molecule import build_bond_list
from .visualize import draw_molecule, bond_histogram
from .pdb import open_pdb
from .xyz import open_xyz, write_xyz

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
