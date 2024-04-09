from typing import List, Tuple
from helpers.base_strategy import BaseStrategy


class Majority(BaseStrategy):
    def take_decision(past_events: List[Tuple[bool, bool]]) -> bool:
        countTrue = 0
        countFalse = 0
        if past_events:
            for i in past_events:
                if i[1]:
                    countTrue += 1
                else:
                    countFalse += 1
            if countTrue >= countFalse:
                return True
            else:
                return False
        else:
            return True
