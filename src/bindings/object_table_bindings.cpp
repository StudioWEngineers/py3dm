// System includes

// External includes

// Project includes
#include "../object_table.h"
#include "casters/uuid_caster.h"
#include "point_geometry_bindings.h"


nb::object GeometryObjectWrapper(const std::shared_ptr<ON_Object>& geom) {
    if (geom == nullptr) {
        throw nb::stop_iteration();
    }

    if (ON_Point* pt = dynamic_cast<ON_Point*>(geom.get())) {
        return nb::cast(pt, nb::rv_policy::reference);
    }

    if (ON_Curve* crv = dynamic_cast<ON_Curve*>(geom.get())) {

        if (ON_LineCurve* lc = dynamic_cast<ON_LineCurve*>(geom.get())) {
            return nb::cast(lc, nb::rv_policy::reference);
        }

        return nb::cast(crv, nb::rv_policy::reference);
    }

    return nb::cast(geom.get(), nb::rv_policy::reference);
}

void ObjectTableBindings(nb::module_& m) {
    nb::class_<ObjectTable::Iterator>(m, "__ObjectTableIterator")

        .def("__iter__", [](ObjectTable::Iterator& it) -> ObjectTable::Iterator& { return it; })

        .def("__next__", [](ObjectTable::Iterator& it) -> nb::object {
                if (it.IsOver()) {
                    throw nb::stop_iteration();
                }

                auto geom = *it;
                ++it;

                if (geom != nullptr) {
                    return GeometryObjectWrapper(geom);
                }

                return nb::none();
            }
        )
    ;

    nb::class_<ObjectTable>(m, "ObjectTable")
        /*magic methods*/
        .def("__iter__", [](ObjectTable& self) {return self.Begin();}, nb::keep_alive<0, 1>())

        /*add methods*/
        .def(
            "add_line",
            nb::overload_cast<const ON_3dPoint&, const ON_3dPoint&, const ON_3dmObjectAttributes*>(&ObjectTable::AddLine, nb::const_),
            nb::arg("start"),
            nb::arg("end"),
            nb::arg("obj_attr") = nullptr
        )
        .def(
            "add_line",
            nb::overload_cast<const ON_Line&, const ON_3dmObjectAttributes*>(&ObjectTable::AddLine, nb::const_),
            nb::arg("line"),
            nb::arg("obj_attr") = nullptr
        )
        .def(
            "add_line",
            nb::overload_cast<const ON_LineCurve&, const ON_3dmObjectAttributes*>(&ObjectTable::AddLine, nb::const_),
            nb::arg("line"),
            nb::arg("obj_attr") = nullptr
        )
        .def(
            "add_point",
            nb::overload_cast<double, double, double, const ON_3dmObjectAttributes*>(&ObjectTable::AddPoint, nb::const_),
            nb::arg("x"),
            nb::arg("y"),
            nb::arg("z"),
            nb::arg("obj_attr") = nullptr
        )
        .def(
            "add_point",
            nb::overload_cast<const ON_3dPoint&, const ON_3dmObjectAttributes*>(&ObjectTable::AddPoint, nb::const_),
            nb::arg("point"),
            nb::arg("obj_attr") = nullptr
        )
        .def(
            "add_point",
            nb::overload_cast<const ON_Point&, const ON_3dmObjectAttributes*>(&ObjectTable::AddPoint, nb::const_),
            nb::arg("point"),
            nb::arg("obj_attr") = nullptr
        )

        /*getters*/
        .def("get_by_uuid", &ObjectTable::GetbyUUID, nb::rv_policy::reference_internal)

        /*other methods*/
        .def("count", &ObjectTable::Count)
        .def("delete_by_uuid", &ObjectTable::DeleteByUUID)
    ;
}
