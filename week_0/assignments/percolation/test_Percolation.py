from unittest import TestCase

from week_0.assignments.percolation.Percolation import Percolation


class TestPercolation(TestCase):

    def test_that_all_sites_are_created(self):
        n: int = 4
        percolation: Percolation = Percolation(n)
        expected: int = n**2 + 2
        actual: int = len(percolation.__union_find.roots)
        self.assertEqual(expected, actual)

    def test_open(self):
        self.fail()

    def test_is_open(self):
        self.fail()

    def test_is_full(self):
        self.fail()

    def test_number_of_open_sites(self):
        self.fail()

    def test_percolates(self):
        self.fail()
