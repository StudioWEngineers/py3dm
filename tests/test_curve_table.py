"""
CurveTableTestSuite
-------------------

Tests for the `CurveTable` class.
"""
# standard library imports
from math import sqrt
from unittest import TestCase
from uuid import UUID

# third party library imports
from py3dm import Line, LineCurve, Model, ObjectAttributes, Point3d

# local library specific imports


class CurveTableTestSuite(TestCase):
    def setUp(self) -> None:
        model = Model()
        self.table = model.CurveTable

    def test_add_with_attributes(self) -> None:
        line_id = self.table.add(
            Line(Point3d(0, 1, 0), Point3d(0, 0, 0)), ObjectAttributes()
        )

        with self.subTest(msg="add with Line part I"):
            self.assertNotEqual(line_id, UUID(int=0))

        with self.subTest(msg="add with Line part II"):
            retrieved_line = self.table.get_by_uuid(line_id)
            self.assertEqual(retrieved_line.line.length(), 1.0)

        line_curve = LineCurve(Point3d(0, 1, 0), Point3d(0, 0, 0))
        line_curve_id = self.table.add(line_curve, ObjectAttributes())

        with self.subTest(msg="add with LineCurve part I"):
            self.assertNotEqual(line_id, UUID(int=0))

        with self.subTest(msg="add with LineCurve part II"):
            retrieved_line_curve = self.table.get_by_uuid(line_curve_id)
            self.assertEqual(
                retrieved_line_curve.line, Line(Point3d(0, 1, 0), Point3d(0, 0, 0))
            )

    def test_add_line_without_attributes(self) -> None:
        line = Line(Point3d(0, 1, 0), Point3d(0, 0, 0))
        line_id = self.table.add(line)

        with self.subTest(msg="add with Line part I"):
            self.assertNotEqual(line_id, UUID(int=0))

        with self.subTest(msg="add with Line part II"):
            retrieved_line = self.table.get_by_uuid(line_id)
            self.assertEqual(retrieved_line.line, line)

        line_curve = LineCurve(Point3d(1, 1, 0), Point3d(0, 0, 0))
        line_curve_id = self.table.add(line_curve)

        with self.subTest(msg="add with LineCurve part I"):
            self.assertNotEqual(line_curve_id, UUID(int=0))

        with self.subTest(msg="add with LineCurve part II"):
            retrieved_line_curve = self.table.get_by_uuid(line_curve_id)
            self.assertEqual(retrieved_line_curve.line.length(), sqrt(2))

    def test_get_by_uuid(self) -> None:
        obj_uuid = self.table.add(Line(Point3d(0, 0, 0), Point3d(1, 1, 1)))
        returned_curve = self.table.get_by_uuid(obj_uuid)

        self.assertEqual(returned_curve.line.point_at(1), Point3d(1, 1, 1))


class CurveTableIteratorTestSuite(TestCase):
    def setUp(self) -> None:
        model = Model()
        self.table = model.CurveTable

        # adding few objects of different types
        model.PointTable.add(0, 1, 2)
        self.table.add(Point3d(0, 0, 1), Point3d(1, 1, 1))
        self.table.add(Point3d(2, 0, 1), Point3d(2, 1, 1))
        model.PointTable.add(2, 1, 2)

    def test_line_iterator(self) -> None:
        self.assertEqual(len(self.table), 2)
