from typing import List, Tuple
from helpers.base_strategy import BaseStrategy


class AlwaysSwitch(BaseStrategy):
    def take_decision(past_events: List[Tuple[bool, bool]]) -> bool:
        if past_events:
            return not past_events[-1][0]
        return True
