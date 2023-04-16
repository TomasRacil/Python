class Rep:
    def __init__(self, rep: str) -> None:
        self.repetitions: int = int(rep.split(" ")[0])
        self.weight: int = int(rep.split(" ")[2])

    def __repr__(self) -> str:
        return f"{self.repetitions} x {self.weight} kg\n"


class Exercise:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.reps: list[Rep] = []
        self.series: int = 0

    def addRep(self, rep: Rep) -> None:
        self.reps.append(rep)
        self.series = len(self.reps)

    def getBestRep(self) -> tuple[str, int]:
        max_weight = 0
        for rep in self.reps:
            if rep.weight > max_weight:
                max_weight = rep.weight
        return self.name, max_weight

    def __repr__(self) -> str:
        out: str = f"{self.name}({self.series}):\n"
        for rep in self.reps:
            out += rep.__repr__()
        return out
