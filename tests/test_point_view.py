# standard library imports
from typing import cast
from unittest import TestCase

# third party library imports
from py3dm import Model, Point, PointView, Point3d

# local library specific imports


class PointViewTestSuite(TestCase):
    def setUp(self) -> None:
        model = Model()
        self.table = model.point_table
        self.uuid_1 = self.table.add(0, 1, 2)
        self.point_1 = cast(PointView, self.table.get(self.uuid_1))

    def test_distance_to(self) -> None:
        self.assertEqual(self.point_1.distance_to(Point3d(0, 2, 2)), 1)

    def test_eq(self) -> None:
        with self.subTest(msg="overload with Point"):
            self.assertTrue(self.point_1 == Point(0, 1, 2))

        with self.subTest(msg="overload with Point3d"):
            self.assertTrue(self.point_1 == Point3d(0, 1, 2))

    def test_is_coincident(self) -> None:
        self.assertTrue(self.point_1.is_coincident(Point3d(0, 1, 2)))

    def test_is_valid(self) -> None:
        self.assertTrue(self.point_1.is_valid())

    def test_ne(self) -> None:
        with self.subTest(msg="overload with Point"):
            self.assertTrue(self.point_1 != Point(1, 1, 2))

        with self.subTest(msg="overload with Point3d"):
            self.assertTrue(self.point_1 != Point3d(0, 2, 2))

    def test_uuid(self) -> None:
        self.assertEqual(self.uuid_1, self.point_1.obj_uuid)

    def test_x(self) -> None:
        self.assertEqual(0, self.point_1.x)

    def test_y(self) -> None:
        self.assertEqual(1, self.point_1.y)

    def test_z(self) -> None:
        self.assertEqual(2, self.point_1.z)
