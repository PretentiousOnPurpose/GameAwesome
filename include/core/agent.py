from typing import Tuple, List, Any, TypeVar
from abc import ABC, abstractmethod

AgentId = int

T = TypeVar('T')

class Agent(ABC):
    class Surrendered(Exception):
        pass

    @abstractmethod
    def message(self, message: str) -> None:
        raise NotImplementedError()

    @abstractmethod
    def update(self, diff : List[Any]):
        pass

    @abstractmethod
    def get_2D_choice(self, dimensions: Tuple[int, int]) -> Tuple[int, int]:
        raise NotImplementedError()

    @abstractmethod
    def choose_one_component_slot(self, components : List['ComponentSlot'], indices : List[T]) -> T:
        ...
