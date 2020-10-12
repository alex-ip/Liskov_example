# Liskov_example
Example of Liskov Substitution Principle (LSP) violation in Python.

The violation example has a subclass "Square" of a superclass "Rectangle". The Square class overrides the setter methods
for height and width as a bodgy work-around which causes problems in the "multiply" base class function.

The conformance example has a subclasses "Square" and "Rectangle" of a superclass "Polygon". The Square and Rectangle
classes both implement their own getters and setters for height and width.

## Demonstration of LSP violation
python -m liskov_badness

## Demonstration of LSP correctness
python -m liskov_conformance