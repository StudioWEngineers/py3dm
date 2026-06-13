// System includes

// External includes

// Project includes
#include "point3d_bindings.h"


void Point3dBindings(nb::module_& m) {
    nb::class_<ON_3dPoint>(m, "Point3d")
        /*dunder methods*/
        .def(nb::init<double, double, double>())
        .def("__eq__", &ON_3dPoint::operator==)
        .def("__mul__", &ON_3dPoint::operator*=)
        .def("__ne__", &ON_3dPoint::operator!=)
        .def("__truediv__", &ON_3dPoint::operator/=)

        /*read-write member variables*/
        .def_rw("x", &ON_3dPoint::x)
        .def_rw("y", &ON_3dPoint::y)
        .def_rw("z", &ON_3dPoint::z)

        /*other methods*/
        .def("distance_to", &ON_3dPoint::DistanceTo)
        .def("is_coincident", &ON_3dPoint::IsCoincident)
    ;
}
