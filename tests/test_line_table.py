"""
LineTableTestSuite
------------------

Tests for the `LineTable` class.
"""
# standard library imports
from math import sqrt
from unittest import TestCase
from uuid import UUID

# third party library imports
from py3dm import Line, LineCurve, Model, ObjectAttributes, Point3d

# local library specific imports


class LineTableTestSuite(TestCase):
    """Tests for the `LineTable` class.
    """
    def setUp(self) -> None:
        model = Model()
        self.table = model.LineTable

    def test_add_with_attributes(self) -> None:
        """Tests for the `add` methods with attributes.
        """
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
        """Tests for the `add` methods without attributes.
        """
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
        """Tests for the `get_by_uuid` method.
        """
        obj_uuid = self.table.add(Line(Point3d(0, 0, 0), Point3d(1, 1, 1)))
        returned_curve = self.table.get_by_uuid(obj_uuid)

        self.assertEqual(returned_curve.line.point_at(1), Point3d(1, 1, 1))


class LineTableIteratorTestSuite(TestCase):
    """Tests for the `LineTable` class, with focus on the iterator.
    """
    def setUp(self) -> None:
        model = Model()
        self.table = model.LineTable

        # adding few objects of different types
        model.ObjectTable.add_point(0, 1, 2)
        self.table.add(Point3d(0, 0, 1), Point3d(1, 1, 1))
        self.table.add(Point3d(2, 0, 1), Point3d(2, 1, 1))
        model.ObjectTable.add_point(2, 1, 2)

    def test_line_iterator(self) -> None:
        """Test for the `LineTable` iterator.
        """
        self.assertEqual(len(list(self.table)), 2)
