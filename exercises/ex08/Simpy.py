"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730312274"


class Simpy:
    """A class that holds and manipulates a list of float values."""
    values: list[float]

    def __init__(self, values: list[float]):
        """Initialize a new Simpy object."""
        self.values = values
    
    def __str__(self) -> str:
        """String representation of a Simpy."""
        return f"Simpy({self.values})"
    
    def fill(self, value: float, times: int) -> None:
        """Fills  our values array my mutating an object called on."""
        self.values = []
        i: int = 0
        while i < times:
            self.values.append(value)
            i += 1
    
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fill in a range of values."""
        self.values = []
        assert step != 0.0
        if step > 0.0:
            next_value: float = start
            while next_value < stop:
                self.values.append(next_value)
                next_value += step
        else:
            next_value: float = start
            while next_value > stop:
                self.values.append(next_value)
                next_value += step
    
    def sum(self) -> float:
        """Delegate this algo to the built-in sum function."""
        return sum(self.values)
    
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Operator overload for addition."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for value in self.values:
                result.values.append(value + rhs)
        elif isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                result.values.append(self.values[i] + rhs.values[i])
                i += 1
        return result
    
    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Operator overload for powers."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for value in self.values:
                result.values.append(value ** rhs)
        elif isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                result.values.append(self.values[i] ** rhs.values[i])
                i += 1
        return result
    
    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Checks if each item in a Simpy is equal to a value."""
        result: list = []
        if isinstance(rhs, float):
            for value in self.values:
                if value == rhs:
                    result.append(True)
                else:
                    result.append(False)
        elif isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                if self.values[i] == rhs.values[i]:
                    result.append(True)
                else:
                    result.append(False)
                i += 1
        return result
    
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Checks if each item in a Simpy is greater than a value."""
        result: list = []
        if isinstance(rhs, float):
            for value in self.values:
                if value > rhs:
                    result.append(True)
                else:
                    result.append(False)
        elif isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                if self.values[i] > rhs.values[i]:
                    result.append(True)
                else:
                    result.append(False)
                i += 1
        return result
    
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Pulls a specific float value from a Simpy or masks a Simpy with a list of booleans."""
        if isinstance(rhs, int):
            floatresult: float = self.values[rhs]
            return floatresult
        elif isinstance(rhs, list):
            simpyresult: Simpy = Simpy([])
            mask: list[bool] = rhs
            i: int = 0
            while i < len(mask):
                if mask[i]:
                    simpyresult.values.append(self.values[i])
                i += 1
            return simpyresult