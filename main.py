import argparse

from collections import defaultdict
from helpers.game import Game
from itertools import combinations
from helpers.read_strategies import read_strategies
from helpers.plot_results import plot_results

parser = argparse.ArgumentParser()
parser.add_argument('--rounds', type=int, default=100)
args = parser.parse_args()

strategies = read_strategies(path="strategies")

game_strats = combinations(strategies, 2)

results = defaultdict(lambda : 0)

for strats in game_strats:
    game = Game(*strats)
    game_result = game.run_game(args.rounds)

    for key, value in game_result.items():
        results[key] += value

plot_results(results=results)
