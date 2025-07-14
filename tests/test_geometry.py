"""
GeometryTestSuite
-----------------

Tests for the `Geometry` class.
"""
# standard library imports
from unittest import TestCase

# third party library imports
from py3dm import Geometry

# local library specific imports


class GeometryTestSuite(TestCase):
    """Tests for the `Geometry` class.
    """
    def test_dimension(self) -> None:
        """Tests for the `dimension` method.
        """
        self.assertEqual(Geometry().dimension(), 3)

    def test_is_deformable(self) -> None:
        """Tests for the `is_deformable` method.
        """
        self.assertFalse(Geometry().is_deformable())

    def test_is_valid(self) -> None:
        """Tests for the `is_valid` method.
        """
        self.assertFalse(Geometry().is_valid())
