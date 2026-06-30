// System includes

// External includes

// Project includes
#include "3d_vector_bindings.h"


void Vector3dBindings(nb::module_& m) {
    nb::class_<ON_3dVector>(m, "Vector3d")
        /*dunder methods*/
        .def(nb::init<>())
        .def(nb::init<ON_3dVector>())
        .def(nb::init<double, double, double>())

        /*operators*/
        .def("__add__", &ON_3dVector::operator+=)
        .def("__eq__", &ON_3dVector::operator==)
        .def("__mul__", &ON_3dVector::operator*=)
        .def("__ne__", &ON_3dVector::operator!=)
        .def("__sub__", &ON_3dVector::operator-=)
        .def("__truediv__", &ON_3dVector::operator/=)

        /*read-write member variables*/
        .def_rw("x", &ON_3dVector::x)
        .def_rw("y", &ON_3dVector::y)
        .def_rw("z", &ON_3dVector::z)

        /*other methods*/
        .def("cross_product", &ON_3dVector::CrossProduct)
        .def("dot_product", &ON_3dVector::DotProduct)
    ;
}
