import abc


class Polygon(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def height(self):
        pass

    @abc.abstractmethod
    def height(self, height: float):
        pass

    @abc.abstractmethod
    def width(self):
        pass

    @abc.abstractmethod
    def width(self, width: float):
        pass

    @abc.abstractmethod
    def multiply(self, multiplier: float) -> None:
        pass

    @abc.abstractmethod
    def area(self) -> float:
        pass
