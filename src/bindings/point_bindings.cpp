// System includes

// External includes

// Project includes
#include "geometry_bindings.h"
#include "point_bindings.h"


void PointBindings(nb::module_& m) {
    nb::class_<ON_Point, ON_Geometry>(m, "Point")
        /*magic methods*/
        .def(nb::init<>())
        .def(nb::init<double, double, double>())
        .def(nb::init<const ON_3dPoint&>())

        /*read-write member variables*/
        .def_rw("point", &ON_Point::point)

        /*other methods*/
        .def("is_valid", &ON_Point::IsValid, nb::arg("text_log") = nullptr)
    ;
}
