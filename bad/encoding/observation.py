# pylint: disable=missing-module-docstring, wrong-import-position, import-error too-few-public-methods too-many-arguments
import sys
import os
import numpy as np

currentPath = os.path.dirname(os.path.realpath(__file__))
parentPath = os.path.dirname(currentPath)
sys.path.append(parentPath)

from bad.encoding.publicfeatures import PublicFeatures
from bad.encoding.privatefeatures import PrivateFeatures

class Observation:
    '''observation'''
    def __init__(self, observation: dict):
        self.public_features = PublicFeatures(observation)
        self.private_features = PrivateFeatures(observation)

    def to_array(self) -> list:
        '''one single vecor'''
        return np.concatenate((self.public_features.firework.red, \
            self.public_features.firework.yellow, \
            self.public_features.firework.green, self.public_features.firework.white, \
            self.public_features.firework.blue))
