"""Example of a Point Class."""
from __future__ import annotations

__author__ = "730312274"


class Point:
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Initialize a Point with is x, y components."""
        self.x = x
        self.y = y

    def scale_by(self, factor: float) -> None:
        """Mutates: multiplies components."""
        self.x *= factor
        self.y *= factor
    
    def scale(self, factor: float) -> Point:
        """Immutable: multiplies components by a factor without mutation."""
        x: float = self.x * factor
        y: float = self.y * factor
        scaled_point: Point = Point(x, y)
        return scaled_point


p0: Point = Point(1.0, 2.0)
p0.scale(2.0)