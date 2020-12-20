from unittest import TestCase

from week_0.assignments.percolation.Percolation import Percolation


class TestPercolation(TestCase):

    def setUp(self) -> None:
        self.n: int = 3
        self.percolation: Percolation = Percolation(self.n)

    def tearDown(self) -> None:
        self.n = None
        self.percolation = None

    def test_open_middle_node(self):
        self.percolation.open(1, 1)
        self.assertTrue(self.percolation.is_open(1, 1))

    def test_open_edge_node(self):
        self.percolation.open(0, 2)
        self.assertTrue(self.percolation.is_open(0, 2))

    def test_is_open_equals_False(self):
        self.assertFalse(self.percolation.is_open(1, 1))

    def test_is_open_equals_True(self):
        self.percolation.open(1, 1)
        self.assertTrue(self.percolation.is_open(1, 1))

    def test_is_full_equals_False_in_top_row(self):
        self.assertFalse(self.percolation.is_full(0, 0))

    def test_is_full_equals_False_in_general_case(self):
        self.assertFalse(self.percolation.is_full(1, 2))

    def test_is_full_equals_True(self):
        self.percolation.open(0, 0)
        self.assertTrue(self.percolation.is_full(0, 0))

    def test_number_of_open_sites_on_initial_state(self):
        expected: int = 0
        actual: int = self.percolation.number_of_open_sites()
        self.assertEqual(expected, actual)

    def test_number_of_open_sites_in_general_case(self):
        self.percolation.open(1, 1)
        expected: int = 1
        actual: int = self.percolation.number_of_open_sites()
        self.assertEqual(expected, actual)

    def test_percolates_is_False_on_initial_state(self):
        self.assertFalse(self.percolation.percolates())

    def test_percolates_is_False_in_general_case(self):
        self.percolation.open(0, 0)
        self.percolation.open(1, 2)
        self.assertFalse(self.percolation.percolates())

    def test_percolates_is_True(self):
        self.percolation.open(0, 1)
        self.percolation.open(1, 1)
        self.percolation.open(2, 1)
        self.assertTrue(self.percolation.percolates())
