from typing import List, Tuple
from helpers.base_strategy import BaseStrategy

# ChatGPT generated
# Cooperates in response to cooperation, but forgives after one retaliation.

class ForgivingCopyOpponent(BaseStrategy):
    defect_count = 0

    def take_decision(past_events: List[Tuple[bool, bool]]) -> bool:
        if past_events:
            last_opponent_move = past_events[-1][1]
            if last_opponent_move:
                ForgivingCopyOpponent.defect_count = 0
                return True
            else:
                ForgivingCopyOpponent.defect_count += 1
                if ForgivingCopyOpponent.defect_count >= 2:
                    ForgivingCopyOpponent.defect_count = 0
                    return False
                else:
                    return True 
        return True