"""
Liskov Substitution Principle - example derived from:
https://web.archive.org/web/20151128004108/http://www.objectmentor.com/resources/articles/lsp.pdf
"""
from liskov_badness.rectangle import Rectangle

class Square(Rectangle):

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, h: float):
        self._height = h
        self._width = h  # Side effect to try to avoid breaking model

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, w: float):
        self._width = w
        self._height = w  # Side effect to try to avoid breaking model


