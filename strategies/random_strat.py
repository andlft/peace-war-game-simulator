from random import choice
from typing import List, Tuple
from helpers.base_strategy import BaseStrategy

class RandomStrat (BaseStrategy):
    def take_decision(past_events: List[Tuple[bool, bool]]) -> bool:
        return choice([True, False])