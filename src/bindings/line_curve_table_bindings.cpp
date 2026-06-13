// System includes

// External includes

// Project includes
#include "../line_curve_table.h"
#include "casters/uuid_caster.h"


void LineCurveTableBindings(nb::module_& m) {
    nb::class_<LineCurveTable::Iterator>(m, "__LineCurveTableIterator")
        .def("__iter__", [](LineCurveTable::Iterator& it) -> LineCurveTable::Iterator& {
            return it;
        })
        .def("__next__", [](LineCurveTable::Iterator& it) {
            while (!it.IsOver()) {
                LineCurveView* object = *it;
                ++it;

                if (object != nullptr) {
                    return object;
                }
            }
            throw nb::stop_iteration();
            }, nb::rv_policy::reference_internal
        )
    ;

    nb::class_<LineCurveTable>(m, "LineCurveTable")
        /*magic methods*/
        .def("__iter__", [](LineCurveTable& self) {return self.Begin();}, nb::keep_alive<0, 1>())
        .def("__len__", &LineCurveTable::Count)

        /*add methods*/
        .def(
            "add",
            nb::overload_cast<const ON_3dPoint&, const ON_3dPoint&, const ON_3dmObjectAttributes*>(&LineCurveTable::Add, nb::const_),
            nb::arg("start"),
            nb::arg("end"),
            nb::arg("attributes") = nullptr
        )
        .def(
            "add",
            nb::overload_cast<const ON_Line&, const ON_3dmObjectAttributes*>(&LineCurveTable::Add, nb::const_),
            nb::arg("line"),
            nb::arg("attributes") = nullptr
        )
        .def(
            "add",
            nb::overload_cast<const ON_LineCurve&, const ON_3dmObjectAttributes*>(&LineCurveTable::Add, nb::const_),
            nb::arg("line"),
            nb::arg("attributes") = nullptr
        )

        /*getters*/
        .def("get_by_uuid", &LineCurveTable::GetbyUUID, nb::rv_policy::reference_internal)

        /*other methods*/
        .def("count", &LineCurveTable::Count)
    ;
}
