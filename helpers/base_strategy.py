from abc import ABC, abstractmethod
from typing import List, Tuple

class BaseStrategy(ABC):
    @abstractmethod
    def take_decision(past_events: List[Tuple[bool, bool]]) -> bool:
        raise NotImplementedError("Method not implemented")