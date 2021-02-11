import random
from math import sqrt
from typing import List

from week_0.union_find.percolation.interfaces.PercolationStatsInterface import PercolationStatsInterface
from week_0.union_find.percolation.Percolation import Percolation


class PercolationStats(PercolationStatsInterface):

    def __init__(self, n: int, trials: int):
        self.__n: int = n
        self.__trials: int = trials
        self.__p_experiment = None
        self.__total_number_of_sites: int = n ** 2
        self.__p_experiment_thresholds: List[float] = []
        self.__run_trials()

    def __run_trials(self):  # O(T*n^2*log(n))
        for _ in range(self.__trials):
            self.__perform_monte_carlo_percolation_experiment()

    def __perform_monte_carlo_percolation_experiment(self):  # O(n^2*log(n))
        self.__p_experiment = Percolation(self.__n)
        while not self.__p_experiment.percolates():  # O(n^2*log(n))
            random_row: int = random.randrange(0, self.__n)
            random_col: int = random.randrange(0, self.__n)
            if not self.__p_experiment.is_open(random_row, random_col):
                self.__p_experiment.open(random_row, random_col)  # O(log(n))

        percolation_threshold: float = self.__p_experiment.number_of_open_sites() / self.__total_number_of_sites
        self.__p_experiment_thresholds.append(percolation_threshold)
        self.__p_experiment = None

    def mean(self) -> float:
        return sum(self.__p_experiment_thresholds) / self.__trials

    def standard_deviation(self) -> float:
        sample_mean: float = self.mean()
        sum_of_differences_squared: float = 0.0
        for threshold in self.__p_experiment_thresholds:
            sum_of_differences_squared += (threshold - sample_mean) ** 2
        variance: float = sum_of_differences_squared / (self.__trials - 1)
        sample_standard_deviation: float = sqrt(variance)
        return sample_standard_deviation

    def confidence_low(self) -> float:
        sample_mean: float = self.mean()
        sample_standard_deviation: float = self.standard_deviation()
        return sample_mean - (1.96 * sqrt(sample_standard_deviation)) / sqrt(self.__trials)

    def confidence_high(self) -> float:
        sample_mean: float = self.mean()
        sample_standard_deviation: float = self.standard_deviation()
        return sample_mean + (1.96 * sqrt(sample_standard_deviation)) / sqrt(self.__trials)
