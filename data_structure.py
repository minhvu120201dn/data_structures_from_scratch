from abc import ABC, abstractmethod

class DataStructure(ABC):
    @abstractmethod
    # Initialize the data structure
    def __init__(self): pass

    @abstractmethod
    # Return the number of elements in the data structure
    def __len__(self) -> int: pass

    @abstractmethod
    # Add a value to the data structure
    def add(self, value:int) -> None: pass

    @abstractmethod
    # Return true if the value was removed, false otherwise
    def remove(self, value:int) -> bool: pass

    @abstractmethod
    # Return true if the value was found, false otherwise
    def find(self, value:int) -> bool: pass

    @abstractmethod
    # Find the largest element in the data structure
    def findMax(self) -> int: pass