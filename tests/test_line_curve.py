"""
LineCurveTestSuite
------------------

Tests for the `LineCurve` class.
"""
# standard library imports
from unittest import TestCase

# third party library imports
from py3dm import LineCurve, Point3d

# local library specific imports


class LineCurveTestSuite(TestCase):
    def setUp(self) -> None:
        self.line = LineCurve(Point3d(0, 0, 0), Point3d(1, 1, 2))

    def test_dimension(self) -> None:
        self.assertEqual(self.line.dimension(), 3)

    def test_is_valid(self) -> None:
        with self.subTest(msg="Positive check"):
            self.assertTrue(self.line.is_valid())

        with self.subTest(msg="Negative check"):
            self.assertFalse(LineCurve().is_valid())

    def test_reverse(self) -> None:
        self.assertTrue(self.line.reverse())

    def test_set_end_point(self) -> None:
        self.line.set_end_point(Point3d(1, 1, 1.2))

        self.assertTrue(self.line.line.point_at(1) == Point3d(1, 1, 1.2))

    def test_set_start_point(self) -> None:
        self.line.set_start_point(Point3d(1, 1, 1.2))

        self.assertTrue(self.line.line.point_at(0) == Point3d(1, 1, 1.2))

    def test_swap_coordinates(self) -> None:
        with self.subTest(msg="Positive swap"):
            self.assertTrue(self.line.swap_coordinates(1, 2))

        with self.subTest(msg="Check updated cooridnates"):
            self.assertTrue(self.line.line.point_at(1) == Point3d(1, 2, 1))
