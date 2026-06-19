# standard library imports
from unittest import TestCase
from uuid import UUID

# third party library imports
from py3dm import Mesh, Model, ObjectAttributes, Point3d

# local library specific imports


class MeshTableTestSuite(TestCase):
    def setUp(self) -> None:
        model = Model()
        self.table = model.mesh_table

    def test_add_with_attributes(self) -> None:
        mesh = Mesh()
        mesh.reserve_vertex_capacity(3)
        mesh.set_vertex(0, Point3d(0, 0, 0))
        mesh.set_vertex(1, Point3d(1, 0, 0))
        mesh.set_vertex(2, Point3d(0, 1, 0))
        mesh.set_triangle(0, 0, 1, 2)
        mesh_uuid = self.table.add(mesh)

        with self.subTest():
            self.assertNotEqual(mesh_uuid, UUID(int=0))

        with self.subTest():
            retrieved_mesh = self.table.get(mesh_uuid)
            self.assertEqual(retrieved_mesh.face_count(), 1)  #type: ignore

        with self.subTest():
            retrieved_mesh = self.table.get(mesh_uuid)
            self.assertEqual(retrieved_mesh.triangle_count(), 1)  #type: ignore

    def test_count(self) -> None:
        with self.subTest(msg="empty table"):
            self.assertEqual(self.table.count(), 0)

        self.table.add(Mesh())

        with self.subTest(msg="non-empty table"):
            self.assertEqual(self.table.count(), 1)

        with self.subTest(msg="non-empty table"):
            self.assertEqual(len(self.table), 1)

    def test_get_by_uuid(self) -> None:
        obj_uuid = self.table.add(Mesh())
        self.assertTrue(self.table.get(obj_uuid).is_empty())  #type: ignore
