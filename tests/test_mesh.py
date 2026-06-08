# standard library imports
from unittest import TestCase

# third party library imports
from py3dm import Mesh, Point3d

# local library specific imports


class MeshTestSuite(TestCase):
    def test_set_quad(self) -> None:
        mesh = Mesh(1, 4, False, False)
        with self.subTest(msg="Empty mesh"):
            self.assertEqual(mesh.quad_count(), 0)

        mesh.set_vertex(0, Point3d(0, 0, 0))
        mesh.set_vertex(1, Point3d(1, 0, 0))
        mesh.set_vertex(2, Point3d(0, 1, 0))
        mesh.set_vertex(3, Point3d(0, 0, 1))
        mesh.set_quad(0, 0, 1, 2, 3)

        with self.subTest(msg="Non-empty mesh"):
            self.assertEqual(mesh.quad_count(), 1)

        with self.subTest(msg="Valid mesh"):
            self.assertTrue(mesh.is_valid())

    def test_set_triangle(self) -> None:
        mesh = Mesh()
        mesh.reserve_vertex_capacity(3)
        with self.subTest(msg="Empty mesh"):
            self.assertEqual(mesh.triangle_count(), 0)

        mesh.set_vertex(0, Point3d(0, 0, 0))
        mesh.set_vertex(1, Point3d(1, 0, 0))
        mesh.set_vertex(2, Point3d(0, 1, 0))
        mesh.set_triangle(0, 0, 1, 2)

        with self.subTest(msg="Non-empty mesh"):
            self.assertEqual(mesh.triangle_count(), 1)
