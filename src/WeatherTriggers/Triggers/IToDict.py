from abc import ABC, abstractmethod


class IToDict(ABC):

    @abstractmethod
    def toDict(self) -> dict:
        pass
