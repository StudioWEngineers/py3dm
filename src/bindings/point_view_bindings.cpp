// System includes

// External includes

// Project includes
#include "casters/uuid_caster.h"
#include "../views/point_view.h"
#include "point_view_bindings.h"


void PointViewBindings(nb::module_& m) {
    nb::class_<PointView>(m, "PointView")
        /*magic methods*/
        .def(
            "__eq__",
            [] (const PointView& self, const ON_Point& other) {
                return self == other;
            }
        )
        .def(
            "__eq__",
            [] (const PointView& self, const ON_3dPoint& other) {
                return self == other;
            }
        )
        .def(
            "__ne__",
            [] (const PointView& self, const ON_Point& other) {
                return self != other;
            }
        )
        .def(
            "__ne__",
            [] (const PointView& self, const ON_3dPoint& other) {
                return self != other;
            }
        )

        /*read-only properties*/
        .def_prop_ro("obj_uuid", &PointView::GetUUID)
        .def_prop_ro("x", &PointView::X)
        .def_prop_ro("y", &PointView::Y)
        .def_prop_ro("z", &PointView::Z)

        /*other methods*/
        .def("distance_to", &PointView::DistanceTo)
        .def("is_coincident", &PointView::IsCoincident)
        .def("is_valid", &PointView::IsValid, nb::arg("text_log") = nullptr)
    ;
}
