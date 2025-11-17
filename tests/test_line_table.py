"""
LineTableTestSuite
------------------

Tests for the `LineTable` class.
"""
# standard library imports
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
        """Tests for the `add_line` methods with attributes.
        """
        line_id = self.table.add(
            Line(Point3d(0, 1, 0), Point3d(0, 0, 0)), ObjectAttributes()
        )

        with self.subTest(msg="add with Line"):
            self.assertNotEqual(line_id, UUID(int=0))

        line_geometry = LineCurve(Point3d(1, 1, 0), Point3d(0, 0, 0))
        line_id = self.table.add(line_geometry, ObjectAttributes())

        with self.subTest(msg="add with LineCurve"):
            self.assertNotEqual(line_id, UUID(int=0))

#    def test_add_line_without_attributes(self) -> None:
#        """Tests for the `add_line` methods without attributes.
#        """
#        line = Line(Point3d(0, 1, 0), Point3d(0, 0, 0))
#        self.table.add_line(line)
#
#        with self.subTest(msg="add_line with Line"):
#            self.assertEqual(self.table.count(), 1)
#
#        line_geometry = LineCurve(Point3d(1, 1, 0), Point3d(0, 0, 0))
#        self.table.add_line(line_geometry)
#
#        with self.subTest(msg="add_point with LineCurve"):
#            self.assertEqual(self.table.count(), 2)
#
#    def test_get_by_uuid(self) -> None:
#        """Tests for the `get_by_uuid` method.
#        """
#        obj_uuid = self.table.add_point(0, 1, 0)
#
#        with self.subTest(msg="test successfull get_by_uuid"):
#            returned_point: PointGeometry = self.table.get_by_uuid(obj_uuid)
#            self.assertEqual(returned_point.point, Point3d(0, 1, 0))
#
#        returned_point.point.z = 1.5
#
#        with self.subTest(msg="test successfull get_by_uuid"):
#            self.assertEqual(returned_point.point, Point3d(0, 1, 1.5))
#        print("OK")


class LineTableIteratorTestSuite(TestCase):
    """Tests for the `LineTable` class, with focus on the iterator.
    """
    def setUp(self) -> None:
        model = Model()
        self.table = model.LineTable