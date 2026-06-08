# standard library imports
from unittest import TestCase

# third party library imports
from py3dm import PointGeometry, Point3d

# local library specific imports


class PointGeometryTestSuite(TestCase):
    def test_constructor(self) -> None:
        with self.subTest(msg="Default constructor"):
            self.assertEqual(PointGeometry().point, Point3d(0, 0, 0))

        with self.subTest(msg="Constructor with coordinates"):
            self.assertEqual(
                PointGeometry(1, 2, 1.1).point,
                Point3d(1, 2, 1.1)
            )

        with self.subTest(msg="Constructor with Point3d"):
            self.assertEqual(
                PointGeometry(Point3d(1, 2, 1.1)).point,
                Point3d(1, 2, 1.1)
            )

    def test_is_valid(self) -> None:
        self.assertTrue(PointGeometry().is_valid())

    def test_point_member_variable(self) -> None:
        self.assertIsInstance(PointGeometry().point, Point3d)
