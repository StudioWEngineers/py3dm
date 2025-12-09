"""
PointTableTestSuite
-------------------

Tests for the `PointTable` class.
"""
# standard library imports
from unittest import TestCase
from uuid import UUID

# third party library imports
from py3dm import Model, ObjectAttributes, PointGeometry, Point3d

# local library specific imports


class PointTableTestSuite(TestCase):
    def setUp(self) -> None:
        model = Model()
        self.table = model.PointTable

    def test_add_with_attributes(self) -> None:
        point_id = self.table.add(Point3d(0, 1, 0), ObjectAttributes())

        with self.subTest(msg="add with Point3d part I"):
            self.assertNotEqual(point_id, UUID(int=0))

        with self.subTest(msg="add with Point3d part II"):
            retrieved_point = self.table.get_by_uuid(point_id)
            self.assertEqual(retrieved_point.point, Point3d(0, 1, 0))

        point_geo = PointGeometry(0, 2, 0)
        point_geo_id = self.table.add(point_geo, ObjectAttributes())

        with self.subTest(msg="add with PointGeometry part I"):
            self.assertNotEqual(point_geo_id, UUID(int=0))

        with self.subTest(msg="add with PointGeometry part II"):
            retrieved_point_geo = self.table.get_by_uuid(point_geo_id)
            self.assertEqual(retrieved_point_geo.point, Point3d(0, 2, 0))

    def test_count(self) -> None:
        with self.subTest(msg="empty table"):
            self.assertEqual(self.table.count(), 0)

        self.table.add(0, 0, 0)

        with self.subTest(msg="non-empty table"):
            self.assertEqual(self.table.count(), 1)

    def test_get_by_uuid(self) -> None:
        obj_uuid = self.table.add(Point3d(0, 0, 3))
        returned_point = self.table.get_by_uuid(obj_uuid)

        self.assertEqual(returned_point.point, Point3d(0, 0, 3))


class PointTableIteratorTestSuite(TestCase):
    def setUp(self) -> None:
        self.model = Model()

        self.model.PointTable.add(0, 1, 2)
        self.model.CurveTable.add(Point3d(0, 0, 1), Point3d(1, 1, 1))
        self.model.CurveTable.add(Point3d(2, 0, 1), Point3d(2, 1, 1))
        self.model.PointTable.add(2, 1, 2)

    def test_point_iterator(self) -> None:
        for point in self.model.PointTable:
            point.point.x = 1

        for point_index, point in enumerate(self.model.PointTable):
            with self.subTest(point_index = point_index):
                self.assertEqual(point.point.x, 1)
