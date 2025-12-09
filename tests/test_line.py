"""
LineTestSuite
-------------

Tests for the `Line` class.
"""
# standard library imports
from math import sqrt
from unittest import TestCase

# third party library imports
from py3dm import Line, Point3d

# local library specific imports


class LineTestSuite(TestCase):
    def setUp(self) -> None:
        self.line = Line(Point3d(0, 0, 0), Point3d(1, 1, 1))

    def test_create(self) -> None:
        with self.subTest(msg="Successful create"):
            self.assertTrue(self.line.create(Point3d(1, 2, 3), Point3d(0, 0, 0)))

        with self.subTest(msg="Successful create"):
            self.assertEqual(self.line[0], Point3d(1, 2, 3))

        with self.subTest(msg="Unsuccessful create"):
            self.assertFalse(self.line.create(Point3d(1, 2, 3), Point3d(1, 2, 3)))

    def test_distance_to(self) -> None:
        point = Point3d(-0.4, 0.0, 0.2)
        with self.subTest(msg="with True argument"):
            self.assertEqual(self.line.distance_to(point, True), 0.447213595499958)

        with self.subTest(msg="with default argument"):
            self.assertEqual(self.line.distance_to(point), 0.4320493798938574)

        with self.subTest(msg="with False argument"):
            self.assertEqual(self.line.distance_to(point, False), 0.4320493798938574)

    def test_getitem(self) -> None:
        with self.subTest(msg="Successful getitem"):
            self.assertEqual(self.line[0], Point3d(0, 0, 0))

        with self.assertRaises(IndexError):
            self.line[2]

    def test_equal(self) -> None:
        with self.subTest(msg="Negative check"):
            self.assertFalse(self.line == Line())

        with self.subTest(msg="Positive check"):
            self.assertTrue(self.line == Line(Point3d(0, 0, 0), Point3d(1, 1, 1)))

    def test_is_valid(self) -> None:
        with self.subTest(msg="Positive check"):
            self.assertTrue(self.line.is_valid())

        with self.subTest(msg="Negative check"):
            self.assertFalse(Line().is_valid())

    def test_length(self) -> None:
        self.assertEqual(self.line.length(), sqrt(3))

    def test_point_at(self) -> None:
        self.assertEqual(self.line.point_at(0.5), Point3d(0.5, 0.5, 0.5))

    def test_setitem(self) -> None:
        self.line[0] = Point3d(-1, 0, 0)

        with self.subTest(msg="Successful getitem"):
            self.assertEqual(self.line[0], Point3d(-1, 0, 0))

        with self.assertRaises(IndexError):
            self.line[2] = Point3d(0, 0, 0)
