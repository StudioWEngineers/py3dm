// System includes

// External includes

// Project includes
#include "../views/mesh_view.h"
#include "casters/uuid_caster.h"
#include "mesh_view_bindings.h"


void MeshViewBindings(nb::module_& m) {
    nb::class_<MeshView>(m, "MeshView")
        /*query methods*/
        .def("is_corrupt", &MeshView::IsCorrupt)
        .def("is_empty", &MeshView::IsEmpty)
        .def("is_not_empty", &MeshView::IsNotEmpty)
        .def("is_valid", &MeshView::IsValid)

        /*count methods*/
        .def("face_count", &MeshView::FaceCount)
        .def("hidden_vertex_count", &MeshView::HiddenVertexCount)
        .def("invalid_face_count", &MeshView::InvalidFaceCount)
        .def("quad_count", &MeshView::QuadCount)
        .def("triangle_count", &MeshView::TriangleCount)
        .def("vertex_count", &MeshView::VertexCount)

        /*has methods*/
        .def("has_face_normals", &MeshView::HasFaceNormals)
        .def("has_ngons", &MeshView::HasNgons)
        .def("has_principal_curvatures", &MeshView::HasPrincipalCurvatures)
        .def("has_surface_parameters", &MeshView::HasSurfaceParameters)
        .def("has_vertex_colors", &MeshView::HasVertexColors)
        .def("has_vertex_normals", &MeshView::HasVertexNormals)
    ;
}
