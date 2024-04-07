from random import randint
from typing import List, Tuple
from helpers.base_strategy import BaseStrategy

class CrazyStrat (BaseStrategy):
    def take_decision(past_events: List[Tuple[bool, bool]]) -> bool:
        random_choice = randint(0,99)
        if random_choice < 40:
            return True
        elif random_choice < 65:
            return False
        else:
            if past_events:
                return not past_events[-1][1]
        return True