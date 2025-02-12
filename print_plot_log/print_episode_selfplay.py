# pylint: disable=missing-module-docstring, wrong-import-position, import-error, too-few-public-methods
import sys
import os

currentPath = os.path.dirname(os.path.realpath(__file__))
parentPath = os.path.dirname(currentPath)
sys.path.append(parentPath)

from bad.run_episode_result import RunEpisodeResult


class PrintEpisodeSelfPlay:
    '''print episode self play'''
    def __init__(self, run_episode_result: RunEpisodeResult) -> None:
        '''init'''
        self.run_episode_result = run_episode_result

    def print(self) -> None:
        '''print'''
        print(f"episode {self.run_episode_result.number} result:")
        print(f"episode reward: {self.run_episode_result.reward}")
        #print(f"finish: {self.run_episode_result.hanabi_environment.state}")
        #print(f"score: {self.run_episode_result.hanabi_environment.state.score}")
        print(f"life tokens: {self.run_episode_result.hanabi_environment.state.life_tokens}")
        total_steps = len(self.run_episode_result.agent_step_times)
        total_time = self.run_episode_result.agent_step_times.sum()
        print(f"Average training steps per second: {total_steps / total_time}")
