from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Interval:
    lower : float
    upper : float

    def subtract(self, b : Interval) -> list[Interval]:
        a1, a2 = self.lower, self.upper
        b1, b2 = b.lower, b.upper

        if b1 <= a1:
            if b2 < a1:
                return [Interval(a1, a2)]
            elif b2 < a2:
                return [Interval(b2, a2)]
            else:
                return []

        elif a1 < b1 < a2:
            if b2 < a2:
                return [Interval(a1, b1), Interval(b2, a2)]
            else:
                return [Interval(a1,b1)]

        else:
            return [Interval(a1,a2)]


    def __sub__(self, other):
        if not isinstance(other, Interval):
            raise TypeError("Subtraction is only supported between two Interval objects.")
        return self.subtract(other)

    def __eq__(self, other):
        return self.lower == other.lower and self.upper == other.upper