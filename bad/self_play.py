# pylint: disable=missing-module-docstring, wrong-import-position, too-few-public-methods
import sys
import os

currentPath = os.path.dirname(os.path.realpath(__file__))
parentPath = os.path.dirname(currentPath)
sys.path.append(parentPath)

from bad.run_eposiode import RunEpisode
from bad.action_network import ActionNetwork
from print_plot_log.print_episode_selfplay import PrintEpisodeSelfPlay
from print_plot_log.print_total_selfplay import PrintTotalSelfPlay
from print_plot_log.plot_total_selfplay import PlotTotalSelfPlay

class SelfPlay:
    '''self play'''
    def __init__(self, network: ActionNetwork) -> None:
        self.network = network

    def run(self, episodes: int) -> None:
        '''self play'''
        print('self play')

        total_reward = 0
        max_reward = 0
        perfect_games = 0
        episodes_result = []

        for episode in range(episodes):

            run_episode = RunEpisode(self.network)
            episode_result = run_episode.run(episode)
            episodes_result.append(episode_result)

            if episode_result.reward > max_reward:
                max_reward = episode_result.reward
            total_reward += episode_result.reward

            if episode_result.reward == 25:
                perfect_games = perfect_games+1

            print_selfplay = PrintEpisodeSelfPlay(episode_result)
            print_selfplay.print()

        print('')
        print_total_selfplay = PrintTotalSelfPlay(episodes, total_reward,
                                                  max_reward, perfect_games)
        print_total_selfplay.print()

        # Plot the results
        plot_total_selfplay = PlotTotalSelfPlay(episodes_result, episodes,
                                                total_reward,max_reward, perfect_games)
        plot_total_selfplay.plot()
