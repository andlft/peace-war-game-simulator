from typing import List, Tuple
from helpers.base_strategy import BaseStrategy


class XorStrat(BaseStrategy):
    def take_decision(past_events: List[Tuple[bool, bool]]) -> bool:
        if past_events:
            return past_events[-1][0] ^ past_events[-1][1]
        return True
