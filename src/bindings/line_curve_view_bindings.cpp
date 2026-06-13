// System includes

// External includes

// Project includes
#include "../views/line_curve_view.h"
#include "casters/uuid_caster.h"
#include "line_curve_view_bindings.h"


void LineCurveViewBindings(nb::module_& m) {
    nb::class_<LineCurveView>(m, "LineCurveView")
        /*dunder methods*/
        .def("__eq__", &LineCurveView::operator==)
        .def("__ne__", &LineCurveView::operator!=)

        /*other methods*/
        .def("distance_to", &LineCurveView::DistanceTo)
        .def("get_uuid", &LineCurveView::GetUUID)
        .def("is_valid", &LineCurveView::IsValid, nb::arg("text_log") = nullptr)
        .def("length", &LineCurveView::Length)
    ;
}
