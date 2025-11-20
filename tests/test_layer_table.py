"""
LayerTableTestSuite
-------------------

Tests for the `LayerTable` class.
"""
# standard library imports
from unittest import TestCase
from uuid import UUID

# third party library imports
from py3dm import Layer, Model

# local library specific imports


class LayerTableTestSuite(TestCase):
    """Tests for the `LayerTable` class.
    """
    def setUp(self) -> None:
        self.model = Model()

    def test_add(self) -> None:
        """Tests for the `add` method.
        """
        layer1 = Layer()
        layer1.set_name("Layer A")
        layer1.color = (255, 0, 255, 255)

        layer2 = Layer()
        layer2.set_name("layer 2")

        layer_1_uuid = self.model.LayerTable.add(layer1)
        layer_2_uuid = self.model.LayerTable.add(layer2)

        with self.subTest(msg="Number of layers with using Count"):
            self.assertEqual(self.model.LayerTable.count(), 2)

        with self.subTest(msg="Number of layers with using __len__"):
            self.assertEqual(len(self.model.LayerTable), 2)

        with self.subTest(msg="Name of 1st layer"):
            self.assertEqual(
                self.model.LayerTable.get_by_uuid(layer_1_uuid).get_name(),
                "Layer A"
            )

        with self.subTest(msg="Name of 2nd layer"):
            self.assertEqual(
                self.model.LayerTable.get_by_uuid(layer_2_uuid).get_name(),
                "layer 2"
            )

        with self.subTest(msg="Color of 1st layer"):
            self.assertEqual(self.model.LayerTable.get_by_index(0).color, (255, 0, 255, 255))

    def test_count(self) -> None:
        """Tests for the `count` method.
        """
        with self.subTest(msg="Number of layers for an empty model"):
            self.assertEqual(self.model.LayerTable.count(), 0)

        self.model.LayerTable.add(Layer())

        with self.subTest(msg="Current number of layers"):
            self.assertEqual(self.model.LayerTable.count(), 1)

    def test_delete_by_name(self) -> None:
        """Tests for the `delete_by_name` method.
        """
        layer_1 = Layer()
        layer_2 = Layer()
        layer_1.set_name("New layer 1")
        layer_2.set_name("New layer 2")
        self.model.LayerTable.add(layer_1)
        self.model.LayerTable.add(layer_2)

        with self.subTest("Successfull delete"):
            self.assertTrue(self.model.LayerTable.delete_by_name("New layer 1"))

        with self.subTest("Unsuccessfull delete"):
            self.assertFalse(self.model.LayerTable.delete_by_name("New layer 3"))

        with self.subTest(msg="Current number of layers"):
            self.assertEqual(self.model.LayerTable.count(), 1)

    def test_delete_by_uuid(self) -> None:
        """Tests for the `delete_by_uuid` method.
        """
        layer_1 = Layer()
        layer_2 = Layer()
        layer_1.set_name("New layer 1")
        layer_2.set_name("New layer 2")
        layer_1_uuid = self.model.LayerTable.add(layer_1)
        self.model.LayerTable.add(layer_2)

        with self.subTest("Successfull delete"):
            self.assertTrue(self.model.LayerTable.delete_by_uuid(layer_1_uuid))

        with self.subTest("Unsuccessfull delete"):
            self.assertFalse(self.model.LayerTable.delete_by_uuid(UUID(int=0)))

        with self.subTest(msg="Current number of layers"):
            self.assertEqual(self.model.LayerTable.count(), 1)

    def test_getitem(self) -> None:
        """Tests for the `__getitem__` method.
        """
        self.model.LayerTable.add(Layer())
        self.model.LayerTable.add(Layer())

        with self.subTest(msg="Not existing index"):
            self.assertIsNone(self.model.LayerTable[3])

        with self.subTest(msg="Existing index"):
            self.assertEqual(self.model.LayerTable[1].get_name(), "Layer 02")

        with self.subTest(msg="Negative index"):
            with self.assertRaises(IndexError):
                self.model.LayerTable[-1]

    def test_get_by_index(self) -> None:
        """Tests for the `get_by_index` method.
        """
        layer_1 = Layer()
        layer_1.set_name("Layer A")
        layer_1.color = (255, 0, 255, 255)

        layer_2 = Layer()
        layer_2.set_name("layer 2")

        self.model.LayerTable.add(layer_1)
        self.model.LayerTable.add(layer_2)

        layer_1 = self.model.LayerTable.get_by_index(0)
        layer_2 = self.model.LayerTable.get_by_index(1)

        with self.subTest(msg="Retrieving not existing layer"):
            self.assertIsNone(self.model.LayerTable.get_by_index(3))

        with self.subTest(msg="Name of 2nd layer"):
            self.assertEqual(layer_2.get_name(), "layer 2")

        with self.subTest(msg="Color of 1st layer"):
            self.assertEqual(layer_1.color, (255, 0, 255, 255))

        with self.subTest(msg="Negative index"):
            with self.assertRaises(IndexError):
                self.model.LayerTable.get_by_index(-1)

    def test_get_by_name(self) -> None:
        """Tests for the `get_by_name` method.
        """
        layer_1 = Layer()
        layer_1.set_name("Layer A")
        layer_1.color = (255, 0, 255, 255)

        layer_2 = Layer()
        layer_2.set_name("layer 2")

        self.model.LayerTable.add(layer_1)
        self.model.LayerTable.add(layer_2)

        layer_1 = self.model.LayerTable.get_by_name("Layer A")
        layer_2 = self.model.LayerTable.get_by_name("layer 2")

        with self.subTest(msg="Retrieving not existing layer"):
            self.assertIsNone(self.model.LayerTable.get_by_name("not existing"))

        with self.subTest(msg="Name of 2nd layer"):
            self.assertEqual(layer_2.get_name(), "layer 2")

        with self.subTest(msg="Color of 1st layer"):
            self.assertEqual(layer_1.color, (255, 0, 255, 255))

    def test_get_by_uuid(self) -> None:
        """Tests for the `get_by_uuid` method.
        """
        layer_1 = Layer()
        layer_1.set_name("Layer A")
        layer_1.color = (255, 0, 255, 255)

        layer_2 = Layer()
        layer_2.set_name("layer 2")

        layer_1_uuid = self.model.LayerTable.add(layer_1)
        layer_2_uuid = self.model.LayerTable.add(layer_2)

        retrieved_layer_1 = self.model.LayerTable.get_by_uuid(layer_1_uuid)
        retrieved_layer_2 = self.model.LayerTable.get_by_uuid(layer_2_uuid)

        with self.subTest(msg="Retrieving not existing layer"):
            self.assertIsNone(self.model.LayerTable.get_by_uuid(UUID(int=0)))

        with self.subTest(msg="Name of 2nd layer"):
            self.assertEqual(retrieved_layer_2.get_name(), "layer 2")

        with self.subTest(msg="Color of 1st layer"):
            self.assertEqual(retrieved_layer_1.color, (255, 0, 255, 255))

    def test_get_index(self) -> None:
        """Tests for the `get_index` method.
        """
        self.model.LayerTable.add(Layer())
        self.model.LayerTable.add(Layer())

        with self.subTest(msg="Retrieving index of not existing layer"):
            self.assertEqual(self.model.LayerTable.get_index(""), -2147483647)

        with self.subTest(msg="Index of 1st layer"):
            self.assertEqual(self.model.LayerTable.get_index("Layer 01"), 0)

        with self.subTest(msg="Index of 2nd layer"):
            self.assertEqual(self.model.LayerTable.get_index("Layer 02"), 1)

    def test_get_uuid(self) -> None:
        """Tests for the `get_uuid` method.
        """
        layer_1_uuid = self.model.LayerTable.add(Layer())
        layer_2_uuid = self.model.LayerTable.add(Layer())

        with self.subTest(msg="Retrieving uuid of not existing layer"):
            self.assertEqual(
                self.model.LayerTable.get_uuid("Not existing"),
                UUID(int=0)
            )

        with self.subTest(msg="Index of 1st layer"):
            self.assertEqual(
                self.model.LayerTable.get_uuid("Layer 01"),
                layer_1_uuid
            )

        with self.subTest(msg="Index of 2nd layer"):
            self.assertEqual(
                self.model.LayerTable.get_uuid("Layer 02"),
                layer_2_uuid
            )

    def test_has(self) -> None:
        """Tests for the `has` method.
        """
        self.model.LayerTable.add(Layer())

        with self.subTest(msg="Not existing layer"):
            self.assertFalse(self.model.LayerTable.has("Not existing"))

        with self.subTest(msg="1st layer"):
            self.assertTrue(self.model.LayerTable.has("Layer 01"))

    def test_max_index(self) -> None:
        """Tests for the `max_index` method.
        """
        with self.subTest(msg="max_index before adding layers to model"):
            self.assertEqual(self.model.LayerTable.max_index(), 0)

        self.model.LayerTable.add(Layer())
        self.model.LayerTable.add(Layer())

        with self.subTest(msg="max_index after adding layers to model"):
            self.assertEqual(self.model.LayerTable.max_index(), 2)

        self.model.LayerTable.delete_by_name("Layer 02")
        self.model.LayerTable.add(Layer())

        with self.subTest(msg="max_index after adding and deleting layers to model"):
            self.assertEqual(self.model.LayerTable.max_index(), 3)


class NestedLayerTableTestSuite(TestCase):
    """Tests for the `LayerTable` class, with nested layers.
    """
    def test_nested_layer(self) -> None:
        """Test for creating a nested layer.
        """

        model = Model()
        model.LayerTable.add(Layer())
        parent_layer_uuid = model.LayerTable.get_uuid("layer 01")

        child_layer = Layer()
        child_layer.parent_uuid = parent_layer_uuid
        child_layer.set_name("my child layer")

        model.LayerTable.add(child_layer)
        child_uuid = model.LayerTable.get_uuid("my child layer")

        self.assertEqual(
            model.LayerTable.get_by_uuid(child_uuid).parent_uuid,
            parent_layer_uuid
        )


class LayerTableTeIteratorstSuite(TestCase):
    """Tests for the `LayerTable` class, with focus on the iterator.
    """
    def test_iter(self) -> None:
        """Tests for the `__iter__` method.
        """
        model = Model()

        model.LayerTable.add(Layer())
        model.LayerTable.add(Layer())

        for layer_index, layer in enumerate(model.LayerTable):
            with self.subTest(layer_index = layer_index):
                self.assertEqual(layer.get_name(), f"Layer 0{layer_index + 1}")

            with self.subTest(layer_index = layer_index):
                self.assertEqual(layer.get_index(), layer_index)

    def test_modify_layer_in_iter(self) -> None:
        """Tests for the `__iter__` method.
        """
        model = Model()

        model.LayerTable.add(Layer())
        model.LayerTable.add(Layer())

        for layer_index, layer in enumerate(model.LayerTable):
            with self.subTest(layer_index = layer_index):
                layer.set_name(f"new_layer_{layer_index}")

            with self.subTest(layer_index = layer_index):
                self.assertEqual(layer.get_name(), f"new_layer_{layer_index}")
