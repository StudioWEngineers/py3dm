"""
ObjectAttributesTestSuite
-------------------------

Tests for the `ObjectAttributes` class.
"""
# standard library imports
from unittest import TestCase, expectedFailure

# third party library imports
from py3dm import ObjectAttributes, ObjectColorSource, ObjectMode, PlotColorSource

# local library specific imports


class ObjectAttributesTestSuite(TestCase):
    """Tests for the `ObjectAttributes` class.
    """
    def setUp(self) -> None:
        self.obj_attr = ObjectAttributes()
    @expectedFailure
    def test_get_and_set_name(self) -> None:
        """Tests for the `get_name` and `set_name` methods.
        """
        with self.subTest(msg="Test default name"):
            self.assertEqual(self.obj_attr.get_name(), "")

        with self.subTest(msg="Test successfull assign name - part I"):
            self.assertTrue(self.obj_attr.set_name("my attributes"))

        with self.subTest(msg="Test successfull assign name - part II"):
            self.assertEqual(self.obj_attr.get_name(), "my attributes")

        with self.subTest(msg="Test unsuccessfull assign name"):
            self.assertFalse(self.obj_attr.set_name(""))

    def test_color(self) -> None:
        """Tests for the `color` method.
        """
        with self.subTest(msg="Test default color"):
            self.assertEqual(self.obj_attr.color, (0, 0, 0, 255))

        self.obj_attr.color = (1, 25, 30, 255)

        with self.subTest(msg="Test assign color"):
            self.assertEqual(self.obj_attr.color, (1, 25, 30, 255))

    def test_color_source(self) -> None:
        """Tests for the `color_source` property.
        """
        with self.subTest(msg="Test default color_soucre"):
            self.assertEqual(self.obj_attr.color_source, ObjectColorSource.from_layer)

        self.obj_attr.color_source = ObjectColorSource.from_parent

        with self.subTest(msg="Test assign color_source"):
            self.assertEqual(self.obj_attr.color_source, ObjectColorSource.from_parent)

    def test_default(self) -> None:
        """Tests for the `default` method.
        """
        self.obj_attr.color = (1, 2, 4, 255)
        self.obj_attr.color_source = ObjectColorSource.from_material
        self.obj_attr.default()

        with self.subTest(msg="Test default color"):
            self.assertEqual(self.obj_attr.color, (0, 0, 0, 255))

        with self.subTest(msg="Test default color_source"):
            self.assertEqual(self.obj_attr.color_source, ObjectColorSource.from_layer)

    def test_equal(self) -> None:
        """Test for the `==` operator.
        """
        self.obj_attr.color = (10, 20, 50, 255)

        other_obj_attr = ObjectAttributes()
        other_obj_attr.color = (10, 20, 50, 255)

        self.assertTrue(self.obj_attr == other_obj_attr)

    def test_equal_not(self) -> None:
        """Test for the `!=` operator.
        """
        other_obj_attr = ObjectAttributes()
        other_obj_attr.color = (10, 20, 50, 255)

        self.assertTrue(self.obj_attr != other_obj_attr)

    def test_is_visible(self) -> None:
        """Tests for the `is_visible` property.
        """
        with self.subTest(msg="Test default is_visible"):
            self.assertTrue(self.obj_attr.is_visible)

        self.obj_attr.is_visible = False

        with self.subTest(msg="Test assign is_visible"):
            self.assertFalse(self.obj_attr.is_visible)

    def test_layer_index(self) -> None:
        """Tests for the `layer_index` method.
        """
        with self.subTest(msg="Test default layer_index"):
            self.assertEqual(self.obj_attr.layer_index, 0)

        self.obj_attr.layer_index = 2

        with self.subTest(msg="Test assign layer_index"):
            self.assertEqual(self.obj_attr.layer_index, 2)

    def test_line_type_index(self) -> None:
        """Tests for the `line_type_index` method.
        """
        with self.subTest(msg="Test default line_type_index"):
            self.assertEqual(self.obj_attr.line_type_index, -1)

        self.obj_attr.line_type_index = 2

        with self.subTest(msg="Test assign line_type_index"):
            self.assertEqual(self.obj_attr.line_type_index, 2)

    def test_material_index(self) -> None:
        """Tests for the `material_index` method.
        """
        with self.subTest(msg="Test default material_index"):
            self.assertEqual(self.obj_attr.material_index, -1)

        self.obj_attr.material_index = 2

        with self.subTest(msg="Test assign material_index"):
            self.assertEqual(self.obj_attr.material_index, 2)

    def test_mode(self) -> None:
        """Tests for the `mode` property.
        """
        with self.subTest(msg="Test default mode"):
            self.assertEqual(self.obj_attr.mode, ObjectMode.normal)

        self.obj_attr.mode = ObjectMode.hidden

        with self.subTest(msg="Test assign mode"):
            self.assertEqual(self.obj_attr.mode, ObjectMode.hidden)

    def test_plot_color(self) -> None:
        """Tests for the `plot_color` method.
        """
        with self.subTest(msg="Test default plot_color"):
            self.assertEqual(self.obj_attr.plot_color, (0, 0, 0, 255))

        self.obj_attr.plot_color = (1, 25, 30, 255)

        with self.subTest(msg="Test assign plot_color"):
            self.assertEqual(self.obj_attr.plot_color, (1, 25, 30, 255))

    def test_plot_color_source(self) -> None:
        """Tests for the `plot_color_source` property.
        """
        with self.subTest(msg="Test default plot_color_soucre"):
            self.assertEqual(self.obj_attr.plot_color_source, PlotColorSource.from_object)

        self.obj_attr.plot_color_source = PlotColorSource.from_parent

        with self.subTest(msg="Test assign plot_color_source"):
            self.assertEqual(self.obj_attr.plot_color_source, PlotColorSource.from_parent)
