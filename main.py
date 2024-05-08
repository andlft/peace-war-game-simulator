import argparse


from helpers.read_strategies import read_strategies
from GUI import run_GUI

parser = argparse.ArgumentParser()
parser.add_argument('--rounds', type=int, default=20)
args = parser.parse_args()

strategies = read_strategies(path="strategies")

run_GUI(
    strats=strategies,
    rounds=args.rounds
    )
