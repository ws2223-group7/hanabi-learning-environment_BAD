# pylint: disable=missing-module-docstring, wrong-import-position, too-few-public-methods
import string
import sys
import os

currentPath = os.path.dirname(os.path.realpath(__file__))
parentPath = os.path.dirname(currentPath)
parentPath2 = os.path.dirname(parentPath)
sys.path.append(parentPath2)

from bad.encoding.ranktointconverter import RankToIntConverter
from bad.encoding.colortointconverter import ColorToIntConverter

class Card:
    '''card'''
    def __init__(self, color: string, rank: int) -> None:
        rank_converter: RankToIntConverter = RankToIntConverter()
        self.rank = rank_converter.convert(rank)
        color_converter: ColorToIntConverter = ColorToIntConverter()
        self.color = color_converter.convert(color)
