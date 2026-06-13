// System includes

// External includes

// Project includes
#include "../mesh_table.h"
#include "casters/uuid_caster.h"


void MeshTableBindings(nb::module_& m) {
    nb::class_<MeshTable::Iterator>(m, "__MeshTableIterator")
        .def("__iter__", [](MeshTable::Iterator& it) -> MeshTable::Iterator& {
            return it;
        })
        .def("__next__", [](MeshTable::Iterator& it) {
            while (!it.IsOver()) {
                MeshView* object = *it;
                ++it;

                if (object != nullptr) {
                    return object;
                }
            }
            throw nb::stop_iteration();
            }, nb::rv_policy::reference_internal
        )
    ;

    nb::class_<MeshTable>(m, "MeshTable")
        /*magic methods*/
        .def("__iter__", [](MeshTable& self) {return self.Begin();}, nb::keep_alive<0, 1>())
        .def("__len__", &MeshTable::Count)

        /*add methods*/
        .def(
            "add",
            nb::overload_cast<const ON_3dmObjectAttributes*>(&MeshTable::Add, nb::const_),
            nb::arg("obj_attr") = nullptr
        )
        .def(
            "add",
            nb::overload_cast<const ON_Mesh&, const ON_3dmObjectAttributes*>(&MeshTable::Add, nb::const_),
            nb::arg("mesh"),
            nb::arg("obj_attr") = nullptr
        )
        .def(
            "add",
            nb::overload_cast<int, int, bool, bool, const ON_3dmObjectAttributes*>(&MeshTable::Add, nb::const_),
            nb::arg("initial_face_array_capacity"),
            nb::arg("initial_vertex_array_capacity"),
            nb::arg("has_vertex_normals") = false,
            nb::arg("has_texture_coordinates") = false,
            nb::arg("obj_attr") = nullptr
        )

        /*getters*/
        .def("get_by_uuid", &MeshTable::GetbyUUID, nb::rv_policy::reference_internal)

        /*other methods*/
        .def("count", &MeshTable::Count)
    ;
}
