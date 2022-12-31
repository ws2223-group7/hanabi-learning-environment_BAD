# pylint: disable=missing-module-docstring, wrong-import-position, import-error
import sys
import os

currentPath = os.path.dirname(os.path.realpath(__file__))
parentPath = os.path.dirname(currentPath)
sys.path.append(parentPath)

from hanabi_learning_environment.rl_env import Agent

class BadAgent(Agent):
    ''' bad agent '''
    def __init__(self) -> None:
        print('init')
    def reset(self, config):
        print('reset')
    def act(self, observation):
        print('act')
