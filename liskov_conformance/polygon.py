import abc


class Polygon(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def height(self):
        raise NotImplementedError

    @abc.abstractmethod
    def height(self, height: float):
        raise NotImplementedError

    @abc.abstractmethod
    def width(self):
        raise NotImplementedError

    @abc.abstractmethod
    def width(self, width: float):
        raise NotImplementedError

    @abc.abstractmethod
    def multiply(self, multiplier: float) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def area(self) -> float:
        raise NotImplementedError
