from typing import List, Tuple
from helpers.base_strategy import BaseStrategy

class AlwaysTrue (BaseStrategy):
    def take_decision(past_events: List[Tuple[bool, bool]]) -> bool:
        return True