from week_0.assignments.percolation.interfaces.PercolationStatsInterface import PercolationStatsInterface
from week_0.assignments.percolation.Percolation import Percolation


class PercolationStats(PercolationStatsInterface):

    def __init__(self, n: int, trials: int):
        self.percolation: Percolation = Percolation(n)
        self.trials: int = trials

    def mean(self) -> float:
        return 0.0

    def standard_deviation(self) -> float:
        return 0.0

    def confidence_low(self) -> float:
        pass

    def confidence_high(self) -> float:
        pass
