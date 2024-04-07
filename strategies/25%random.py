from random import choice
from typing import List, Tuple
from helpers.base_strategy import BaseStrategy

class Random25 (BaseStrategy):
    def take_decision(past_events: List[Tuple[bool, bool]]) -> bool:
        random_choice = choice([0,1,1,1])
        if random_choice == 1:
            return True
        else:
            return False