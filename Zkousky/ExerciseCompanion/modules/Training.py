from __future__ import annotations
from .Exercise import Exercise, Rep


class Date:
    day: int
    month: int
    year: int

    def __init__(self, date: str) -> None:
        temp: list[str] = date.split(".")
        self.day = int(temp[0])
        self.month = int(temp[1])
        self.year = int(temp[2])

    def __lt__(self, other: Date) -> bool:
        if self.year < other.year:
            return True
        elif self.year > other.year:
            return False
        else:
            if self.month < other.month:
                return True
            elif self.month > other.month:
                return False
            else:
                if self.day < other.day:
                    return True
                else:
                    return False

    def __repr__(self) -> str:
        return f"{self.day}.{self.month}.{self.year}"


class Training:
    date: Date
    exercises: list[Exercise]

    def __init__(self, training: str) -> None:
        lines: list[str] = [t for t in training.split("\n") if t != ""]
        self.date = Date(lines[0])
        self.exercises = []
        l: int = 1
        while l < len(lines):
            temp = lines[l].split("(")
            exercise: Exercise = Exercise(temp[0])
            rep: int = int(temp[1].split(")")[0])
            l += 1
            while rep > 0:
                exercise.addRep(Rep(lines[l]))
                rep -= 1
                l += 1
            self.exercises.append(exercise)

    def getBests(self) -> list[tuple[str, int]]:
        return [exercise.getBestRep() for exercise in self.exercises]

    def __lt__(self, other: Training) -> bool:
        if self.date < other.date:
            return True
        else:
            return False

    def __repr__(self) -> str:
        out: str = f"{self.date.__repr__()}\n"
        for exercise in self.exercises:
            out += exercise.__repr__()
        return out
