from typing import List, Tuple
from helpers.base_strategy import BaseStrategy
# ChatGPT generated based on description in https://plato.stanford.edu/entries/prisoner-dilemma/strategy-table.html
# A generous strategy is a ZD strategy that guarantees that an opponent's average payoff can be lower than the reward payoff only if one's own long term average payoff is even lower. GEN-n guarantees that one's loss relative to the reward is n times one's opponent's. As it turns out, for a PD with the payoffs above, GEN-2=S(1, 9⁄16,1⁄2,1⁄8)).

class GenerousStrategy(BaseStrategy):
    opponent_defections = 0
    own_defections = 0
    last_action = None

    def take_decision(past_events: List[Tuple[bool, bool]]) -> bool:
        if past_events:
            GenerousStrategy.last_action = past_events[-1][1]
            if not GenerousStrategy.last_action:  # If opponent defected
                GenerousStrategy.opponent_defections += 1
                return False
        return True

    def update_own_defections(own_defection):
        GenerousStrategy.own_defections += own_defection

    def get_next_action() -> bool:
        if GenerousStrategy.own_defections * 2 >= GenerousStrategy.opponent_defections:
            return False
        else:
            return True
