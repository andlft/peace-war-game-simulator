from typing import List, Tuple
from helpers.base_strategy import BaseStrategy

class HoldsGrudges (BaseStrategy):
    def take_decision(past_events: List[Tuple[bool, bool]]) -> bool:
        ok = True
        for i in past_events:
            if not i[1]:
                ok = False
                break
        return ok