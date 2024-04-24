import matplotlib.pyplot as plt
from typing import Dict

def plot_results(results: Dict[str, int]) -> None:
    strategy_names = []
    strategy_scores = []

    sorted_results = sorted([(key, value) for key, value in results.items()], key = lambda x : x[1])

    for key, value in sorted_results:
        strategy_names.append(key)
        strategy_scores.append(value)

    plt.barh(strategy_names, strategy_scores)
    plt.xlabel("Score")
    plt.ylabel("Strategy")

    plt.show()