from unittest import TestCase

from week_0.union_find.percolation.PercolationStats import PercolationStats


class TestPercolationStats(TestCase):

    def test_mean(self):
        p_stats: PercolationStats = PercolationStats(2, 10000)
        expected: float = 0.66
        actual: float = p_stats.mean()
        self.assertAlmostEqual(expected, actual, delta=0.1)

    def test_standard_deviation(self):
        p_stats: PercolationStats = PercolationStats(2, 10000)
        expected: float = 0.1177
        actual: float = p_stats.standard_deviation()
        self.assertAlmostEqual(expected, actual, delta=0.1)

    def test_confidence_low(self):
        p_stats: PercolationStats = PercolationStats(2, 10000)
        expected: float = 0.66
        actual: float = p_stats.confidence_low()
        self.assertAlmostEqual(expected, actual, delta=0.1)

    def test_confidence_high(self):
        p_stats: PercolationStats = PercolationStats(2, 10000)
        expected: float = 0.66
        actual: float = p_stats.confidence_high()
        self.assertAlmostEqual(expected, actual, delta=0.1)
