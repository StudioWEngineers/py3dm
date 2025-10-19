"""
ObjectTableTestSuite
---------------------

Tests for the `ObjectTable` class.
"""
# standard library imports
from unittest import TestCase

# third party library imports
from py3dm import Line, LineCurve, Model, ObjectAttributes, PointGeometry, Point3d

# local library specific imports


class ObjectTableTestSuite(TestCase):
    """Tests for the `ObjectTable` class.
    """
    def setUp(self) -> None:
        model = Model()
        self.table = model.ObjectTable

    def test_add_line_with_attributes(self) -> None:
        """Tests for the `add_line` methods with attributes.
        """
        obj_attr = ObjectAttributes()
        line = Line(Point3d(0, 1, 0), Point3d(0, 0, 0))
        self.table.add_line(line, obj_attr)

        with self.subTest(msg="add_line with Line"):
            self.assertEqual(self.table.count(), 1)

        line_geometry = LineCurve(Point3d(1, 1, 0), Point3d(0, 0, 0))
        self.table.add_line(line_geometry, obj_attr)

        with self.subTest(msg="add_line with LineCurve"):
            self.assertEqual(self.table.count(), 2)

    def test_add_line_without_attributes(self) -> None:
        """Tests for the `add_line` methods without attributes.
        """
        line = Line(Point3d(0, 1, 0), Point3d(0, 0, 0))
        self.table.add_line(line)

        with self.subTest(msg="add_line with Line"):
            self.assertEqual(self.table.count(), 1)

        line_geometry = LineCurve(Point3d(1, 1, 0), Point3d(0, 0, 0))
        self.table.add_line(line_geometry)

        with self.subTest(msg="add_point with LineCurve"):
            self.assertEqual(self.table.count(), 2)

    def test_add_point_with_attributes(self) -> None:
        """Tests for the `add_point` methods with attributes. See also `test_count`.
        """
        obj_attr = ObjectAttributes()
        point3d = Point3d(0, 1, 0)
        self.table.add_point(point3d, obj_attr)

        with self.subTest(msg="add_point with Point3d"):
            self.assertEqual(self.table.count(), 1)

        point_geometry = PointGeometry(1, 1, 0)
        self.table.add_point(point_geometry, obj_attr)

        with self.subTest(msg="add_point with PointGeometry"):
            self.assertEqual(self.table.count(), 2)

    def test_add_point_without_attributes(self) -> None:
        """Tests for the `add_points` methods without attributes. See also `test_count`.
        """
        point3d = Point3d(0, 1, 0)
        self.table.add_point(point3d)

        with self.subTest(msg="add_point with Point3d"):
            self.assertEqual(self.table.count(), 1)

        point_geometry = PointGeometry(1, 1, 0)
        self.table.add_point(point_geometry)

        with self.subTest(msg="add_point with PointGeometry"):
            self.assertEqual(self.table.count(), 2)

    def test_count(self) -> None:
        """Tests for the `count` method. See also `test_delete_by_uuid`.
        """
        with self.subTest(msg="empty ObjectTable"):
            self.assertEqual(self.table.count(), 0)

        self.table.add_point(0, 0, 0)

        with self.subTest(msg="non-empty ObjectTable"):
            self.assertEqual(self.table.count(), 1)

    def test_delete_by_uuid(self) -> None:
        """Tests for the `delete_by_uuid` method.
        """
        obj_uuid = self.table.add_point(0, 0, 0)

        with self.subTest(msg="test successfull delete_by_uuid"):
            self.assertTrue(self.table.delete_by_uuid(obj_uuid))

        with self.subTest(msg="test successfull delete_by_uuid"):
            self.assertEqual(self.table.count(), 0)

    def test_get_by_uuid(self) -> None:
        """Tests for the `get_by_uuid` method.
        """
        obj_uuid = self.table.add_point(0, 1, 0)

        with self.subTest(msg="test successfull get_by_uuid"):
            returned_point: PointGeometry = self.table.get_by_uuid(obj_uuid)
            self.assertEqual(returned_point.point, Point3d(0, 1, 0))

        returned_point.point.z = 1.5

        with self.subTest(msg="test successfull get_by_uuid"):
            self.assertEqual(returned_point.point, Point3d(0, 1, 1.5))
        print("OK")


class ObjectTableIteratorTestSuite(TestCase):
    """Tests for the `ObjectTable` class, with focus on the iterator.
    """
    def setUp(self) -> None:
        model = Model()
        self.table = model.ObjectTable