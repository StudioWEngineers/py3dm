# standard library imports
from unittest import TestCase
from uuid import UUID, uuid4

# third party library imports
from py3dm import ModelComponent

# local library specific imports


class ModelComponentTestSuite(TestCase):
    def setUp(self) -> None:
        self.model_comp = ModelComponent()

    def test_get_index(self) -> None:
        with self.subTest(msg="without input parameter overload"):
            self.assertEqual(self.model_comp.get_index(), -2147483647)

        with self.subTest(msg="with input parameter overload"):
            self.assertEqual(self.model_comp.get_index(2), 2)

    def test_get_uuid(self) -> None:
        self.assertEqual(self.model_comp.get_uuid(), UUID(int=0))

    def test_parent_uuid_is_not_null(self) -> None:
        self.assertFalse(self.model_comp.parent_uuid_is_not_null())

    def test_get_parent_uuid_is_null(self) -> None:
        self.assertTrue(self.model_comp.parent_uuid_is_null())

    def test_set_uuid(self) -> None:
        new_uuid = uuid4()
        self.model_comp.set_uuid(new_uuid)

        with self.subTest(msg="with input parameter overload"):
            self.assertEqual(self.model_comp.get_uuid(), new_uuid)

        new_uuid = self.model_comp.set_uuid()
        with self.subTest(msg="no input parameter overload variant"):
            self.assertEqual(self.model_comp.get_uuid(), new_uuid)

    def test_uuid_is_not_null(self) -> None:
        self.assertFalse(self.model_comp.uuid_is_not_null())

    def test_get_uuid_is_null(self) -> None:
        self.assertTrue(self.model_comp.uuid_is_null())
