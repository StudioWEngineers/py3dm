# standard library imports
from typing import cast
from unittest import TestCase
from uuid import UUID

# third party library imports
from py3dm import Layer, LayerView, Model

# local library specific imports


class LayerViewTestSuite(TestCase):
    def setUp(self) -> None:
        model = Model()

        # create a layer and set some properties
        layer = Layer()
        layer.color = (100, 50, 10, 255)
        layer.plot_color = (100, 50, 10, 255)
        layer.plot_weight = 1.1
        layer.iges_level = 10
        layer.set_name("My new layer")
        self.layer_uuid = model.layer_table.add(layer)

        # NOTE: workaround to silent type checker complains
        self.layer_view = cast(
            LayerView,
            model.layer_table.get_by_uuid(self.layer_uuid)
        )

    def test_color(self) -> None:
        self.assertEqual(self.layer_view.color, (100, 50, 10, 255))

    def test_get_and_set_iges_level(self) -> None:
        self.assertEqual(self.layer_view.iges_level, 10)

    def test_get_index(self) -> None:
        with self.subTest(msg=""):
            self.assertEqual(self.layer_view.index(), 0)

        with self.subTest(msg="overload variant"):
            self.assertEqual(self.layer_view.index(2), 0)

    def test_is_expanded(self) -> None:
        self.assertTrue(self.layer_view.is_expanded)

    def test_is_locked(self) -> None:
        self.assertFalse(self.layer_view.is_locked)

    def test_is_visible(self) -> None:
        self.assertTrue(self.layer_view.is_visible)

    def test_uuid(self) -> None:
        self.assertEqual(self.layer_view.layer_uuid, self.layer_uuid)

    def test_line_type_index(self) -> None:
        self.assertEqual(self.layer_view.line_type_index, -1)

    def test_name(self) -> None:
        self.assertEqual(self.layer_view.name, "My new layer")

    def test_parent_uuid(self) -> None:
        self.assertEqual(self.layer_view.parent_uuid, UUID(int=0))

    def test_plot_color(self) -> None:
        self.assertEqual(self.layer_view.plot_color, (100, 50, 10, 255))

    def test_plot_weight(self) -> None:
        self.assertEqual(self.layer_view.plot_weight, 1.1)

    def test_render_material_index(self) -> None:
        self.assertEqual(self.layer_view.render_material_index, -1)

    def test_parent_uuid_is_not_null(self) -> None:
        self.assertFalse(self.layer_view.parent_uuid_is_not_null)

    def test_parent_uuid_is_null(self) -> None:
        self.assertTrue(self.layer_view.parent_uuid_is_null)

    def test_path_separator(self) -> None:
        self.assertEqual(self.layer_view.path_separator, "::")

    def test_is_valid(self) -> None:
        self.assertTrue(self.layer_view.is_valid())
