// System includes

// External includes

// Project includes
#include "../line_table.h"
#include "casters/uuid_caster.h"


void LineTableBindings(nb::module_& m) {
    nb::class_<LineTable::Iterator>(m, "__LineTableIterator")
        .def("__iter__", [](LineTable::Iterator& it) -> LineTable::Iterator& {
            return it;
        })
        .def("__next__", [](LineTable::Iterator& it) {
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

    nb::class_<LineTable>(m, "LineTable")
        /*magic methods*/
        .def("__iter__", [](LineTable& self) {return self.Begin();}, nb::keep_alive<0, 1>())

        /*add methods*/
        .def(
            "add",
            nb::overload_cast<const ON_3dPoint&, const ON_3dPoint&, const ON_3dmObjectAttributes*>(&LineTable::Add, nb::const_),
            nb::arg("start"),
            nb::arg("end"),
            nb::arg("attributes") = nullptr
        )
        .def(
            "add",
            nb::overload_cast<const ON_Line&, const ON_3dmObjectAttributes*>(&LineTable::Add, nb::const_),
            nb::arg("line"),
            nb::arg("attributes") = nullptr
        )
        .def(
            "add",
            nb::overload_cast<const ON_LineCurve&, const ON_3dmObjectAttributes*>(&LineTable::Add, nb::const_),
            nb::arg("line"),
            nb::arg("attributes") = nullptr
        )

        /*getters*/
        .def("get_by_uuid", &LineTable::GetbyUUID, nb::rv_policy::reference_internal)
    ;
}
