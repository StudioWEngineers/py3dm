// System includes

// External includes

// Project includes
#include "../curve_table.h"
#include "casters/uuid_caster.h"


void CurveTableBindings(nb::module_& m) {
    nb::class_<CurveTable::Iterator>(m, "__CurveTableIterator")
        .def("__iter__", [](CurveTable::Iterator& it) -> CurveTable::Iterator& {
            return it;
        })
        .def("__next__", [](CurveTable::Iterator& it) {
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

    nb::class_<CurveTable>(m, "CurveTable")
        /*magic methods*/
        .def("__iter__", [](CurveTable& self) {return self.Begin();}, nb::keep_alive<0, 1>())
        .def("__len__", &CurveTable::Count)

        /*add methods*/
        .def(
            "add",
            nb::overload_cast<const ON_3dPoint&, const ON_3dPoint&, const ON_3dmObjectAttributes*>(&CurveTable::Add, nb::const_),
            nb::arg("start"),
            nb::arg("end"),
            nb::arg("attributes") = nullptr
        )
        .def(
            "add",
            nb::overload_cast<const ON_Line&, const ON_3dmObjectAttributes*>(&CurveTable::Add, nb::const_),
            nb::arg("line"),
            nb::arg("attributes") = nullptr
        )
        .def(
            "add",
            nb::overload_cast<const ON_LineCurve&, const ON_3dmObjectAttributes*>(&CurveTable::Add, nb::const_),
            nb::arg("line"),
            nb::arg("attributes") = nullptr
        )

        /*getters*/
        .def("get_by_uuid", &CurveTable::GetbyUUID, nb::rv_policy::reference_internal)

        /*other methods*/
        .def("count", &CurveTable::Count)
    ;
}
