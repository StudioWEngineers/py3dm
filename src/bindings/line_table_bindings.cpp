// System includes

// External includes

// Project includes
#include "../line_table.h"
#include "casters/uuid_caster.h"


nb::object LineWrapper(const std::shared_ptr<ON_Object>& geom) {
    if (ON_Curve* crv = dynamic_cast<ON_Curve*>(geom.get())) {

        if (ON_LineCurve* lc = dynamic_cast<ON_LineCurve*>(geom.get())) {
            return nb::cast(lc, nb::rv_policy::reference);
        }

        return nb::cast(crv, nb::rv_policy::reference);
    }
}

void LineTableBindings(nb::module_& m) {
    nb::class_<LineTable::Iterator>(m, "__LineTableIterator")

        .def("__iter__", [](LineTable::Iterator& it) -> LineTable::Iterator& { return it; })

        .def("__next__", [](LineTable::Iterator& it) -> nb::object {
                if (it.IsOver()) {
                    throw nb::stop_iteration();
                }

                auto geom = *it;
                ++it;

                if (geom != nullptr) {
                    return LineWrapper(geom);
                }
            }
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
