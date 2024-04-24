from typing import List, Tuple
from helpers.base_strategy import BaseStrategy

# ChatGPT generated
# Cooperates if both players have the same action in the previous round; otherwise, it changes its strategy

class Pavlov(BaseStrategy):
    def take_decision(past_events: List[Tuple[bool, bool]]) -> bool:
        if past_events:
            last_round = past_events[-1]
            if last_round[0] == last_round[1]:
                return last_round[1]
        return True