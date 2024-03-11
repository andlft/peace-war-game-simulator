from typing import List, Tuple
from helpers.base_strategy import BaseStrategy

class CopyOpponent (BaseStrategy):
    def take_decision(past_events: List[Tuple[bool, bool]]) -> bool:
        if past_events:
            return past_events[-1][1]
        else:
            return True