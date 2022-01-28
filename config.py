from ast import Import
from distutils.command.config import config
import numpy as np

# resolution: 1440 * 3200
class Config:
    # suggest (5000 / (1440 * 3200)) of resolution
    MIN_AREA = 5000
    COEFFICIENT = 0.83
    SIZE = (1440, 3200)
    MIN_HSV = np.array([10, 60, 240])
    MAX_HSV = np.array([25, 100, 255])


config = Config()