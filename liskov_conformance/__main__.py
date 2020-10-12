"""
Liskov Substitution Principle - example derived from:
https://web.archive.org/web/20151128004108/http://www.objectmentor.com/resources/articles/lsp.pdf
"""
from liskov_conformance.rectangle import Rectangle
from liskov_conformance.square import Square

rectangle = Rectangle()
square = Square()

print('Setting rectangle width to 5.0 and height to 4.0')
rectangle.width = 5.0
rectangle.height = 4.0
print(f"All good: rectangle.width = {rectangle.width}, rectangle.height = {rectangle.height}")
print()

print('Calling rectangle.multiply(multiplier=2.0)')
rectangle.multiply(multiplier=2.0)
print(f"All good: rectangle.width = {rectangle.width}, rectangle.height = {rectangle.height}")
print()

print('Setting square width to 5.0')
square.width = 5.0
print(f"All good: square.width = {square.width}, square.height = {square.height}")
print()

print('Setting square height to 4.0')
square.height = 4.0
print(f"All good: square.width = {square.width}, square.height = {square.height}")
print()

print('Calling square.multiply(multiplier=2.0)')
square.multiply(multiplier=2.0)
print(f"All good: square.width = {square.width}, square.height = {square.height}")
print()
