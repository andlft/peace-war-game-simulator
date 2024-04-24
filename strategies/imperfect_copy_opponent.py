from random import random
from typing import List, Tuple
from helpers.base_strategy import BaseStrategy

# ChatGPT generated based on description in https://plato.stanford.edu/entries/prisoner-dilemma/strategy-table.html
# This strategy imitates the opponent's last move with a high (but less than one) probability.

class ImperfectCopyOpponent(BaseStrategy):
    def take_decision(past_events: List[Tuple[bool, bool]]) -> bool:
        if past_events:
            last_opponent_move = past_events[-1][1]
            if random() < 0.9:
                return last_opponent_move
        return True