"""
ModelComponentTestSuite
-----------------------

Tests for the `ModelComponent` class.
"""
# standard library imports
from unittest import TestCase
from uuid import UUID, uuid4

# third party library imports
from py3dm import ModelComponent

# local library specific imports


class ModelComponentTestSuite(TestCase):
    """Tests for the `ModelComponent` class.
    """
    def setUp(self) -> None:
        self.model_comp = ModelComponent()

    def test_get_index(self) -> None:
        """Tests for the `get_index` method.
        """
        with self.subTest(msg="without input parameter overload"):
            self.assertEqual(self.model_comp.get_index(), -2147483647)

        with self.subTest(msg="with input parameter overload"):
            self.assertEqual(self.model_comp.get_index(2), 2)

    def test_get_uuid(self) -> None:
        """Test for the `get_uuid` method.
        """
        self.assertEqual(self.model_comp.get_uuid(), UUID(int=0))

    def test_parent_uuid_is_not_null(self) -> None:
        """Test for the `parent_uuid_is_not_null` method.
        """
        self.assertFalse(self.model_comp.parent_uuid_is_not_null())

    def test_get_parent_uuid_is_null(self) -> None:
        """Test for the `parent_uuid_is_null` method.
        """
        self.assertTrue(self.model_comp.parent_uuid_is_null())

    def test_set_uuid(self) -> None:
        """Tests for the `set_uuid` method.
        """
        new_uuid = uuid4()
        self.model_comp.set_uuid(new_uuid)

        with self.subTest(msg="with input parameter overload"):
            self.assertEqual(self.model_comp.get_uuid(), new_uuid)

        new_uuid = self.model_comp.set_uuid()
        with self.subTest(msg="no input parameter overload variant"):
            self.assertEqual(self.model_comp.get_uuid(), new_uuid)

    def test_uuid_is_not_null(self) -> None:
        """Test for the `uuid_is_not_null` method.
        """
        self.assertFalse(self.model_comp.uuid_is_not_null())

    def test_get_uuid_is_null(self) -> None:
        """Test for the `uuid_is_null` method.
        """
        self.assertTrue(self.model_comp.uuid_is_null())
