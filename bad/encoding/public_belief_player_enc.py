# pylint: disable=missing-module-docstring, wrong-import-position, too-few-public-methods

import sys
import os

currentPath = os.path.dirname(os.path.realpath(__file__))
parentPath = os.path.dirname(currentPath)
parentPath2 = os.path.dirname(parentPath)
sys.path.append(parentPath2)

from bad.belief.public_belief_player import PublicBeliefPlayer
from bad.encoding.public_belief_hand_card_enc import PublicBeliefHandCardEnc

class PublicBeliefPlayerEnc():
    '''PublicBeliefPlayerEnc'''
    def __init__(self, public_belf_player: PublicBeliefPlayer):
        '''init'''
        self.hand_card1 = PublicBeliefHandCardEnc(public_belf_player[0])
        self.hand_card2 = PublicBeliefHandCardEnc(public_belf_player[1])
        self.hand_card3 = PublicBeliefHandCardEnc(public_belf_player[2])
        self.hand_card4 = PublicBeliefHandCardEnc(public_belf_player[3])
        self.hand_card5 = PublicBeliefHandCardEnc(public_belf_player[4])
