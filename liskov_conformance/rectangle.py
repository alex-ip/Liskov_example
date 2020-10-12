"""
Liskov Substitution Principle - example derived from:
https://web.archive.org/web/20151128004108/http://www.objectmentor.com/resources/articles/lsp.pdf
"""
from liskov_conformance.polygon import Polygon


class Rectangle(Polygon):

    def __init__(self):
        self._width = None
        self._height = None

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, h: float):
        self._height = h

    @property
    def width(self) -> float:
        return self._width

    @width.setter
    def width(self, w: float):
        self._width = w

    def multiply(self, multiplier: float) -> None:
        self.height *= multiplier
        self.width *= multiplier

    def area(self) -> float:
        return self.height * self.width
