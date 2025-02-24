from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Interval:
    lower : float
    upper : float

    def subtract(self, b : Interval) -> list[Interval]:
        a = self
        if b.lower <= a.lower:
            if b.upper < a.upper:
                return [Interval(b.upper, a.upper)]
            else:
                return []
        else:
            if b.upper < a.lower:
                return [Interval(a.lower, b.lower), Interval(b.upper, a.upper)]
            else:
                return [Interval(a.lower, b.lower)]
