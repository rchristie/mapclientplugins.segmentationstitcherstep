
"""
MAP Client Plugin - Generated from MAP Client v0.21.4
"""

__version__ = '0.2.0'
__author__ = 'Richard Christie'
__stepname__ = 'Segmentation Stitcher'
__location__ = 'https://github.com/ABI-Software/mapclientplugins.segmentationstitcherstep'

# import class that derives itself from the step mountpoint.
from mapclientplugins.segmentationstitcherstep import step

# Import the resource file when the module is loaded,
# this enables the framework to use the step icon.
from . import resources_rc