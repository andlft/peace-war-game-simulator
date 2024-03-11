
from helpers.base_strategy import BaseStrategy
from typing import List, Tuple, Dict

class Game:
    s1: BaseStrategy
    s2: BaseStrategy
    s1_points: int
    s2_points: int
    game_history_s1: List[Tuple[bool, bool]]
    game_history_s2: List[Tuple[bool, bool]]

    def __init__(self, s1: BaseStrategy, s2: BaseStrategy):
        self.s1 = s1
        self.s2 = s2
        self.s1_points = 0
        self.s2_points = 0
        self.game_history_s1 = []
        self.game_history_s2 = []
    
    def run_game(self, rounds: int) -> Dict[str, int]:
        for _ in range(rounds):
            d1 = self.s1.take_decision(self.game_history_s1)
            d2 = self.s2.take_decision(self.game_history_s2)

            if d1 == d2 == True:
                self.s1_points += 2
                self.s2_points += 2
            elif d1 == True and d2 == False:
                self.s2_points += 3
            elif d1 == False and d2 == True:
                self.s1_points += 3
            else:
                self.s1_points += 1
                self.s2_points += 1

            self.game_history_s1.append((d1, d2))
            self.game_history_s2.append((d2, d1))
            
        return {
            self.s1.__name__: self.s1_points,
            self.s2.__name__: self.s2_points
            }
