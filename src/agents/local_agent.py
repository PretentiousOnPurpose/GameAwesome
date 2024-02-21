from game_anywhere.include.core import Agent
from .descriptors import AgentDescriptor
from typing import Optional, List, TypeVar

T = TypeVar('T')

class HumanAgent(Agent):
    class Descriptor(AgentDescriptor):
        def start_initialization(self, id : 'AgentId', context):
            pass
        def await_initialization(self, promise) -> 'HumanAgent':
            return HumanAgent()

    def message(self, message):
        print(message)

    @staticmethod
    def get_value(constructor, message = None):
        if message is None:
            message = f"Enter a value of type {constructor}"
        while True:
            raw_result : str = input(message + ":")
            try:
                return constructor(raw_result)
            except ValueError as err:
                print(err)
                print("Please try again.")

    @staticmethod
    def get_integer(min=None, max=None):
        def _suitable_int(st):
            i = int(st)
            if i < min or max < i:
                raise ValueError(f"{i} is out of bounds: [{min}, {max}] expected")
            return i
        return HumanAgent.get_value(_suitable_int, message=f"Enter a value between {min} and {max}")

    # override
    def get_2D_choice(self, dimensions):
        return tuple( self.get_integer(min=0, max=dim-1) for dim in dimensions )

    # override
    def choose_one_component_slot(self, slots : List['ComponentSlot'], indices : List[T]) -> T:
        for i, slot in enumerate(slots):
            print(f"[{i+1}]", slot)
        i = self.get_integer(min=1, max=len(slots)) - 1
        return indices[i]
