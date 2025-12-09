"""
Point3dTestSuite
----------------

Tests for the `Point3d` class.
"""
# standard library imports
from math import sqrt
from unittest import TestCase

# third party library imports
from py3dm import Point3d

# local library specific imports


class Point3dTestSuite(TestCase):
    def test_distance_to(self) -> None:
        self.assertEqual(Point3d(0, 0, 0).distance_to(Point3d(1, 1, 1)), sqrt(3))

    def test_division(self) -> None:
        point = Point3d(0, 0, 1.1) / 2.1

        with self.subTest(msg="x-coordinate"):
            self.assertEqual(point.x, 0)

        with self.subTest(msg="y-coordinate"):
            self.assertEqual(point.y, 0)

        with self.subTest(msg="z-coordinate"):
            self.assertEqual(point.z, 1.1 / 2.1)

    def test_equal(self) -> None:
        self.assertTrue(Point3d(0, 0, 1.1) == Point3d(0, 0, 1.1))

    def test_equal_not(self) -> None:
        self.assertTrue(Point3d(0, 0, 1.1) != Point3d(1, 0, 1.1))

    def test_get_and_set_x_coordinate(self) -> None:
        point = Point3d(0, 0, 0)

        with self.subTest(msg="Get x-coordinate"):
            self.assertEqual(point.x, 0)

        point.x = 3.1

        with self.subTest(msg="Get x-coordinate after set"):
            self.assertEqual(point.x, 3.1)

    def test_get_and_set_y_coordinate(self) -> None:
        point = Point3d(0, 0, 0)

        with self.subTest(msg="Get y-coordinate"):
            self.assertEqual(point.y, 0)

        point.y = 3.1

        with self.subTest(msg="Get y-coordinate after set"):
            self.assertEqual(point.y, 3.1)

    def test_get_and_set_z_coordinate(self) -> None:
        point = Point3d(0, 0, 1.1)

        with self.subTest(msg="Get z-coordinate"):
            self.assertEqual(point.z, 1.1)

        point.z = 3.1

        with self.subTest(msg="Get z-coordinate after set"):
            self.assertEqual(point.z, 3.1)

    def test_is_coincident(self) -> None:
        self.assertTrue(Point3d(1, 2, 3.1).is_coincident(Point3d(1, 2, 3.1)))

    def test_multiplication(self) -> None:
        point = Point3d(0, 0, 1.1) * 2.1

        with self.subTest(msg="x-coordinate"):
            self.assertEqual(point.x, 0)

        with self.subTest(msg="y-coordinate"):
            self.assertEqual(point.y, 0)

        with self.subTest(msg="z-coordinate"):
            self.assertEqual(point.z, 1.1 * 2.1)

    def test_sum(self) -> None:
        point = Point3d(0, 0, 1.1) + Point3d(1, 2, 3)

        with self.subTest(msg="x-coordinate"):
            self.assertEqual(point.x, 1)

        with self.subTest(msg="y-coordinate"):
            self.assertEqual(point.y, 2)

        with self.subTest(msg="z-coordinate"):
            self.assertEqual(point.z, 4.1)
