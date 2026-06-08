# standard library imports
from typing import cast
from unittest import TestCase
from uuid import UUID, uuid4

# third party library imports
from py3dm import Layer, Model

# local library specific imports


class LayerTestSuite(TestCase):
    def setUp(self) -> None:
        self.layer = Layer()

    def test_get_and_set_color(self) -> None:
        with self.subTest(msg="Layer color before assignment"):
            self.assertEqual(self.layer.color, (0, 0, 0, 255))

        self.layer.color = (100, 50, 10, 255)

        with self.subTest(msg="Layer color after assignment"):
            self.assertEqual(self.layer.color, (100, 50, 10, 255))

    def test_get_and_set_iges_level(self) -> None:
        with self.subTest(msg="Layer iges_level before assignment"):
            self.assertEqual(self.layer.iges_level, -1)

        self.layer.iges_level = 10

        with self.subTest(msg="Layer iges_level after assignment"):
            self.assertEqual(self.layer.iges_level, 10)

    def test_get_index(self) -> None:
        self.assertEqual(self.layer.get_index(), -2147483647)

    def test_get_and_set_is_expanded(self) -> None:
        with self.subTest(msg="Layer is_expanded before assignment"):
            self.assertTrue(self.layer.is_expanded)

        self.layer.is_expanded = False

        with self.subTest(msg="Layer is_expanded after assignment"):
            self.assertFalse(self.layer.is_expanded)

    def test_get_and_set_is_locked(self) -> None:
        with self.subTest(msg="Layer is_locked before assignment"):
            self.assertFalse(self.layer.is_locked)

        self.layer.is_locked = True

        with self.subTest(msg="Layer is_locked after assignment"):
            self.assertTrue(self.layer.is_locked)

    def test_get_and_set_is_visible(self) -> None:
        with self.subTest(msg="Layer is_visible before assignment"):
            self.assertTrue(self.layer.is_visible)

        self.layer.is_visible = False

        with self.subTest(msg="Layer is_visible after assignment"):
            self.assertFalse(self.layer.is_visible)

    def test_get_and_set_layer_uuid(self) -> None:
        with self.subTest(msg="Layer layer_uuid before assignment"):
            self.assertEqual(self.layer.layer_uuid, UUID(int=0))

        new_id = uuid4()
        self.layer.layer_uuid = new_id

        with self.subTest(msg="Layer layer_uuid after assignment"):
            self.assertEqual(self.layer.layer_uuid, new_id)

    def test_get_and_set_line_type_index(self) -> None:
        with self.subTest(msg="Layer line_type_index before assignment"):
            self.assertEqual(self.layer.line_type_index, -1)

        self.layer.line_type_index = 3

        with self.subTest(msg="Layer line_type_index after assignment"):
            self.assertEqual(self.layer.line_type_index, 3)

    def test_get_and_set_name(self) -> None:
        with self.subTest(msg="Layer name before assignment"):
            self.assertEqual(self.layer.get_name(), "")

        with self.subTest(msg="Successfull set_name"):
            self.assertTrue(self.layer.set_name("My new layer"))

        with self.subTest(msg="Layer name after assignment"):
            self.assertEqual(self.layer.get_name(), "My new layer")

    def test_get_and_set_parent_uuid(self) -> None:
        with self.subTest(msg="Layer parent_uuid before assignment"):
            self.assertEqual(self.layer.parent_uuid, UUID(int=0))

        self.layer.parent_uuid = UUID(int=3)

        with self.subTest(msg="Layer parent_uuid after assignment"):
            self.assertEqual(self.layer.parent_uuid, UUID(int=3))

    def test_get_and_set_persistent_locking(self) -> None:
        with self.subTest(msg="Layer persistent_locking before assignment"):
            self.assertFalse(self.layer.persistent_locking)

        # NOTE: persistent_locking has effect only if parent_uuid is not null
        # and is_locked is True. In this case the following set has no effect
        # and persistent_locking is False
        self.layer.persistent_locking = True
        with self.subTest(msg="Layer persistent_locking after assignment"):
            self.assertFalse(self.layer.persistent_locking)

        self.layer.parent_uuid = uuid4()
        self.layer.is_locked = True
        self.layer.persistent_locking = True
        with self.subTest(msg="Layer persistent_locking after assignment"):
            self.assertTrue(self.layer.persistent_locking)

    def test_get_and_set_persistent_visibility(self) -> None:
        with self.subTest(msg="Layer persistent_visibility before assignment"):
            self.assertTrue(self.layer.persistent_visibility)

        # NOTE: persistent_visibility has effect only if parent_uuid is not
        # null and is_visible is False. In this case the following set has no
        # effect and persistent_visibility is False
        self.layer.persistent_visibility = False
        with self.subTest(msg="Layer persistent_visibility after assignment"):
            self.assertTrue(self.layer.persistent_visibility)

        self.layer.parent_uuid = uuid4()
        self.layer.is_visible = False
        self.layer.persistent_visibility = False
        with self.subTest(msg="Layer persistent_locking after assignment"):
            self.assertFalse(self.layer.persistent_visibility)

    def test_get_and_set_plot_color(self) -> None:
        with self.subTest(msg="Layer plot_color before assignment"):
            self.assertEqual(self.layer.plot_color, (0, 0, 0, 255))

        self.layer.plot_color = (100, 50, 10, 255)

        with self.subTest(msg="Layer plot_color after assignment"):
            self.assertEqual(self.layer.plot_color, (100, 50, 10, 255))

    def test_get_and_set_plot_weight(self) -> None:
        with self.subTest(msg="Layer plot_weight before assignment"):
            self.assertEqual(self.layer.plot_weight, 0)

        self.layer.plot_weight = 1.1

        with self.subTest(msg="Layer plot_weight after assignment"):
            self.assertEqual(self.layer.plot_weight, 1.1)

    def test_get_and_set_render_material_index(self) -> None:
        with self.subTest(msg="Layer render_material_index before assignment"):
            self.assertEqual(self.layer.render_material_index, -1)

        self.layer.render_material_index = 2

        with self.subTest(msg="Layer render_material_index after assignment"):
            self.assertEqual(self.layer.render_material_index, 2)

    def test_get_parent_uuid_is_not_null(self) -> None:
        with self.subTest(msg="Before assignment"):
            self.assertFalse(self.layer.parent_uuid_is_not_null())

        self.layer.parent_uuid = uuid4()

        with self.subTest(msg="After assignment"):
            self.assertTrue(self.layer.parent_uuid_is_not_null())

    def test_get_parent_uuid_is_null(self) -> None:
        with self.subTest(msg="Before assignment"):
            self.assertTrue(self.layer.parent_uuid_is_null())

        self.layer.parent_uuid = uuid4()

        with self.subTest(msg="After assignment"):
            self.assertFalse(self.layer.parent_uuid_is_null())

    def test_get_path_separator(self) -> None:
        self.assertEqual(self.layer.path_separator, "::")

    def test_is_valid(self) -> None:
        self.assertFalse(self.layer.is_valid())

    def test_repr(self) -> None:
        expected_repr = (
            "Layer with properties:\n"
            "\tcolor = (0, 0, 0, 255)\n"
            "\tiges_level = -1\n"
            "\tindex = -2147483647\n"
            "\tis_expanded = true\n"
            "\tis_locked = false\n"
            "\tis_visible = true\n"
            f"\tlayer_uuid = {UUID(int=0)}\n"
            "\tline_type_index = -1\n"
            "\tname = ''\n"
            f"\tparent_uuid = {UUID(int=0)}\n"
            "\tpath separator = ::\n"
            "\tpersistent_locking = false\n"
            "\tpersistent_visibility = true\n"
            "\tplot_color = (0, 0, 0, 255)\n"
            "\tplot_weight = 0\n"
            "\trender_material_index = -1\n"
        )

        self.assertEqual(str(self.layer), expected_repr)


class ExistingLayerModificationTestSuite(TestCase):
    def setUp(self) -> None:
        self.model = Model()
        layer_uuid = self.model.layer_table.add(Layer())

        # workaround to silent mypy complains
        layer = self.model.layer_table.get_by_uuid(layer_uuid)
        self.layer = cast(Layer, layer)

    def test_get_and_set_color(self) -> None:
        with self.subTest(msg="Layer color before assignment"):
            self.assertEqual(self.layer.color, (0, 0, 0, 255))

        self.layer.color = (100, 50, 10, 255)

        with self.subTest(msg="Layer color after assignment"):
            self.assertEqual(self.layer.color, (100, 50, 10, 255))

    def test_get_and_set_iges_level(self) -> None:
        with self.subTest(msg="Layer iges_level before assignment"):
            self.assertEqual(self.layer.iges_level, -1)

        self.layer.iges_level = 10

        with self.subTest(msg="Layer iges_level after assignment"):
            self.assertEqual(self.layer.iges_level, 10)

    def test_get_index(self) -> None:
        self.assertEqual(self.layer.get_index(), 0)

    def test_get_and_set_is_expanded(self) -> None:
        with self.subTest(msg="Layer is_expanded before assignment"):
            self.assertTrue(self.layer.is_expanded)

        self.layer.is_expanded = False

        with self.subTest(msg="Layer is_expanded after assignment"):
            self.assertFalse(self.layer.is_expanded)

    def test_get_and_set_is_locked(self) -> None:
        with self.subTest(msg="Layer is_locked before assignment"):
            self.assertFalse(self.layer.is_locked)

        self.layer.is_locked = True

        with self.subTest(msg="Layer is_locked after assignment"):
            self.assertTrue(self.layer.is_locked)

    def test_get_and_set_is_visible(self) -> None:
        with self.subTest(msg="Layer is_visible before assignment"):
            self.assertTrue(self.layer.is_visible)

        self.layer.is_visible = False

        with self.subTest(msg="Layer is_visible after assignment"):
            self.assertFalse(self.layer.is_visible)

    def test_get_and_set_layer_uuid(self) -> None:
        layer_uuid = self.model.layer_table.get_uuid("Layer 01")
        with self.subTest(msg="Layer layer_uuid before assignment"):
            self.assertEqual(self.layer.layer_uuid, layer_uuid)

        new_id = uuid4()
        self.layer.layer_uuid = new_id

        with self.subTest(msg="Layer layer_uuid after assignment"):
            self.assertEqual(self.layer.layer_uuid, new_id)

    def test_get_and_set_line_type_index(self) -> None:
        with self.subTest(msg="Layer line_type_index before assignment"):
            self.assertEqual(self.layer.line_type_index, -1)

        self.layer.line_type_index = 3

        with self.subTest(msg="Layer line_type_index after assignment"):
            self.assertEqual(self.layer.line_type_index, 3)

    def test_get_and_set_name(self) -> None:
        with self.subTest(msg="Layer name before assignment"):
            self.assertEqual(self.layer.get_name(), "Layer 01")

        with self.subTest(msg="Successfull set_name"):
            self.assertTrue(self.layer.set_name("My new layer"))

        with self.subTest(msg="Layer name after assignment"):
            self.assertEqual(self.layer.get_name(), "My new layer")

    def test_get_and_set_parent_uuid(self) -> None:
        with self.subTest(msg="Layer parent_uuid before assignment"):
            self.assertEqual(self.layer.parent_uuid, UUID(int=0))

        self.layer.parent_uuid = UUID(int=3)

        with self.subTest(msg="Layer parent_uuid after assignment"):
            self.assertEqual(self.layer.parent_uuid, UUID(int=3))

    def test_get_and_set_persistent_locking(self) -> None:
        with self.subTest(msg="Layer persistent_locking before assignment"):
            self.assertFalse(self.layer.persistent_locking)

        # NOTE: persistent_locking has effect only if parent_uuid is not null
        # and is_locked is True. In this case the following set has no effect
        # and persistent_locking is False
        self.layer.persistent_locking = True
        with self.subTest(msg="Layer persistent_locking after assignment"):
            self.assertFalse(self.layer.persistent_locking)

        self.layer.parent_uuid = uuid4()
        self.layer.is_locked = True
        self.layer.persistent_locking = True
        with self.subTest(msg="Layer persistent_locking after assignment"):
            self.assertTrue(self.layer.persistent_locking)

    def test_get_and_set_persistent_visibility(self) -> None:
        with self.subTest(msg="Layer persistent_visibility before assignment"):
            self.assertTrue(self.layer.persistent_visibility)

        # NOTE: persistent_visibility has effect only if parent_uuid is not
        # null and is_visible is False. In this case the following set has no
        # effect and persistent_visibility is False
        self.layer.persistent_visibility = False
        with self.subTest(msg="Layer persistent_visibility after assignment"):
            self.assertTrue(self.layer.persistent_visibility)

        self.layer.parent_uuid = uuid4()
        self.layer.is_visible = False
        self.layer.persistent_visibility = False
        with self.subTest(msg="Layer persistent_locking after assignment"):
            self.assertFalse(self.layer.persistent_visibility)

    def test_get_and_set_plot_color(self) -> None:
        with self.subTest(msg="Layer plot_color before assignment"):
            self.assertEqual(self.layer.plot_color, (0, 0, 0, 255))

        self.layer.plot_color = (100, 50, 10, 255)

        with self.subTest(msg="Layer plot_color after assignment"):
            self.assertEqual(self.layer.plot_color, (100, 50, 10, 255))

    def test_get_and_set_plot_weight(self) -> None:
        with self.subTest(msg="Layer plot_weight before assignment"):
            self.assertEqual(self.layer.plot_weight, 0)

        self.layer.plot_weight = 1.1

        with self.subTest(msg="Layer plot_weight after assignment"):
            self.assertEqual(self.layer.plot_weight, 1.1)

    def test_get_and_set_render_material_index(self) -> None:
        with self.subTest(msg="Layer render_material_index before assignment"):
            self.assertEqual(self.layer.render_material_index, -1)

        self.layer.render_material_index = 2

        with self.subTest(msg="Layer render_material_index after assignment"):
            self.assertEqual(self.layer.render_material_index, 2)

    def test_get_parent_uuid_is_not_null(self) -> None:
        with self.subTest(msg="Before assignment"):
            self.assertFalse(self.layer.parent_uuid_is_not_null())

        self.layer.parent_uuid = uuid4()

        with self.subTest(msg="After assignment"):
            self.assertTrue(self.layer.parent_uuid_is_not_null())

    def test_get_parent_uuid_is_null(self) -> None:
        with self.subTest(msg="Before assignment"):
            self.assertTrue(self.layer.parent_uuid_is_null())

        self.layer.parent_uuid = uuid4()

        with self.subTest(msg="After assignment"):
            self.assertFalse(self.layer.parent_uuid_is_null())

    def test_get_path_separator(self) -> None:
        self.assertEqual(self.layer.path_separator, "::")

    def test_is_valid(self) -> None:
        self.assertTrue(self.layer.is_valid())

    def test_repr(self) -> None:
        expected_repr = (
            "Layer with properties:\n"
            "\tcolor = (0, 0, 0, 255)\n"
            "\tiges_level = -1\n"
            "\tindex = 0\n"
            "\tis_expanded = true\n"
            "\tis_locked = false\n"
            "\tis_visible = true\n"
            f"\tlayer_uuid = {self.model.layer_table.get_uuid('Layer 01')}\n"
            "\tline_type_index = -1\n"
            "\tname = 'Layer 01'\n"
            f"\tparent_uuid = {UUID(int=0)}\n"
            "\tpath separator = ::\n"
            "\tpersistent_locking = false\n"
            "\tpersistent_visibility = true\n"
            "\tplot_color = (0, 0, 0, 255)\n"
            "\tplot_weight = 0\n"
            "\trender_material_index = -1\n"
        )

        self.assertEqual(str(self.layer), expected_repr)
