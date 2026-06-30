# standard library imports
from unittest import TestCase

# third party library imports
from py3dm import Vector3d

# local library specific imports


class Vector3dTestSuite(TestCase):
    def test_division(self) -> None:
        vector = Vector3d(0, 0, 1.1)
        vector /= 2.1
        self.assertEqual(vector.z, 1.1 / 2.1)

    def test_equal(self) -> None:
        self.assertTrue(Vector3d(0, 0, 1.1) == Vector3d(0, 0, 1.1))

    def test_equal_not(self) -> None:
        self.assertTrue(Vector3d(0, 0, 1.1) != Vector3d(1, 0, 1.1))

    def test_get_and_set_component(self) -> None:
        vector = Vector3d(0, 0, 0)
        vector.x = 3.1
        self.assertEqual(vector.x, 3.1)

    def test_multiplication(self) -> None:
        vector = Vector3d(0, 0, 1.1)
        vector *= 2.1
        self.assertEqual(vector.z, 1.1 * 2.1)
