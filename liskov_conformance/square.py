"""
Liskov Substitution Principle - example derived from:
https://web.archive.org/web/20151128004108/http://www.objectmentor.com/resources/articles/lsp.pdf
"""
from liskov_conformance.polygon import Polygon


class Square(Polygon):

    def __init__(self):
        self._side_length = None

    @property
    def height(self):
        return self._side_length

    @height.setter
    def height(self, height: float):
        self._side_length = height

    @property
    def width(self):
        return self._side_length

    @width.setter
    def width(self, width: float):
        self._side_length = width

    def multiply(self, multiplier: float) -> None:
        """
        Function to demonstrate Liskov Substitution violation
        """
        self._side_length *= multiplier

    def area(self):
        return self._side_length * self._side_length
