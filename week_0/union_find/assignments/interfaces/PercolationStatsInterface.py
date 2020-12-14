

class PercolationStatsInterface:

    def __init__(self, n: int, trials: int) -> None:
        """
        Perform independent trials on an nxn grid
        """
        pass

    def mean(self) -> float:
        """
        Sample mean of percolation threshold
        """
        pass

    def standard_deviation(self) -> float:
        pass

    def confidence_low(self) -> float:
        """
        Low endpoint of the 95% confidence interval
        """
        pass

    def confidence_high(self) -> float:
        """
        High endpoint of the 95% confidence interval
        """
        pass
