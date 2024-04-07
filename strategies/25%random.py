from random import choice
from typing import List, Tuple
from helpers.base_strategy import BaseStrategy

class Random25 (BaseStrategy):
    def take_decision(past_events: List[Tuple[bool, bool]]) -> bool:
        random_choice = choice([False,True,True,True])
        return random_choice