from typing import List, Tuple
from helpers.base_strategy import BaseStrategy

# ChatGPT generated based on description in https://plato.stanford.edu/entries/prisoner-dilemma/strategy-table.html
# This strategy punishes defections by the opponent by responding with defections for an increasing number of rounds, and then apologizes by cooperating in the subsequent two rounds.

class GradualCopyOpponent(BaseStrategy):
    defection_count = 0
    forgiveness_count = 0

    def take_decision(past_events: List[Tuple[bool, bool]]) -> bool:
        if GradualCopyOpponent.defection_count > 0:
            GradualCopyOpponent.defection_count -= 1
            return False
        elif GradualCopyOpponent.forgiveness_count > 0:
            GradualCopyOpponent.forgiveness_count -= 1
            return True
        elif past_events:
            last_opponent_move = past_events[-1][1]
            if not last_opponent_move:
                GradualCopyOpponent.defection_count += 1
                GradualCopyOpponent.forgiveness_count = 2
                return False
            else:
                return True
        return True