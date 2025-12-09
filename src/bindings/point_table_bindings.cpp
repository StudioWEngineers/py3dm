// System includes

// External includes

// Project includes
#include "../point_table.h"
#include "casters/uuid_caster.h"


void PointTableBindings(nb::module_& m) {
    nb::class_<PointTable::Iterator>(m, "__CurveTableIterator")
        .def("__iter__", [](PointTable::Iterator& it) -> PointTable::Iterator& {
            return it;
        })
        .def("__next__", [](PointTable::Iterator& it) {
            while (!it.IsOver()) {
                ON_Object* object = *it;
                ++it;

                if (object != nullptr) {
                    return object;
                }
            }
            throw nb::stop_iteration();
            }, nb::rv_policy::reference_internal
        )
    ;

    nb::class_<PointTable>(m, "PointTable")
        /*magic methods*/
        .def("__iter__", [](PointTable& self) {return self.Begin();}, nb::keep_alive<0, 1>())
        .def("__len__", &PointTable::Count)

        /*add methods*/
        .def(
            "add",
            nb::overload_cast<double, double, double, const ON_3dmObjectAttributes*>(&PointTable::Add, nb::const_),
            nb::arg("x"),
            nb::arg("y"),
            nb::arg("z"),
            nb::arg("obj_attr") = nullptr
        )
        .def(
            "add",
            nb::overload_cast<const ON_Point&, const ON_3dmObjectAttributes*>(&PointTable::Add, nb::const_),
            nb::arg("point"),
            nb::arg("obj_attr") = nullptr
        )
        .def(
            "add",
            nb::overload_cast<const ON_3dPoint&, const ON_3dmObjectAttributes*>(&PointTable::Add, nb::const_),
            nb::arg("point"),
            nb::arg("obj_attr") = nullptr
        )

        /*getters*/
        .def("get_by_uuid", &PointTable::GetbyUUID, nb::rv_policy::reference_internal)

        /*other methods*/
        .def("count", &PointTable::Count)
    ;
}
