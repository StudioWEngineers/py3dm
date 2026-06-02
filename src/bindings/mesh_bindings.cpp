// System includes

// External includes

// Project includes
#include "mesh_bindings.h"


void MeshBindings(nb::module_& m) {
    nb::class_<ON_Mesh, ON_Geometry>(m, "Mesh")
        /*magic methods*/
        .def(nb::init<>())
        .def(nb::init<int, int, bool, bool>())
        .def(nb::init<ON_Mesh>())

        /*query methods*/
        .def(
            "is_corrupt",
            &ON_Mesh::IsCorrupt,
            nb::arg("repair"),
            nb::arg("silent_error") ,
            nb::arg("text_log") = nullptr
        )
        .def("is_deformable", &ON_Mesh::IsDeformable)
        .def("is_empty", &ON_Mesh::IsEmpty)
        .def("is_not_empty", &ON_Mesh::IsNotEmpty)
        .def("is_valid", &ON_Mesh::IsValid, nb::arg("text_log") = nullptr)

        /*count methods*/
        .def("face_count", &ON_Mesh::FaceCount)
        .def("hidden_vertex_count", &ON_Mesh::HiddenVertexCount)
        .def("invalid_face_count", &ON_Mesh::InvalidFaceCount)
        .def("quad_count", &ON_Mesh::QuadCount)
        .def("triangle_count", &ON_Mesh::TriangleCount)
        .def("vertex_count", &ON_Mesh::VertexCount)

        /*has methods*/
        .def("has_face_normals", &ON_Mesh::HasFaceNormals)
        .def("has_ngons", &ON_Mesh::HasNgons)
        .def("has_principal_curvatures", &ON_Mesh::HasPrincipalCurvatures)
        .def("has_surface_parameters", &ON_Mesh::HasSurfaceParameters)
        .def("has_vertex_colors", nb::overload_cast<>(&ON_Mesh::HasVertexColors, nb::const_))
        .def("has_vertex_normals", &ON_Mesh::HasVertexNormals)

        /*other methods*/
        .def("clear_vertex_colors", &ON_Mesh::ClearVertexColors)
        .def("flip", &ON_Mesh::Flip)
        .def("reserve_vertex_capacity", &ON_Mesh::ReserveVertexCapacity)
        .def("set_quad", &ON_Mesh::SetQuad)
        .def("set_triangle", &ON_Mesh::SetTriangle)
        .def("set_vertex", nb::overload_cast<int, const ON_3dPoint&>(&ON_Mesh::SetVertex))
        .def("swap_coordinates", &ON_Mesh::SwapCoordinates)
    ;
}
