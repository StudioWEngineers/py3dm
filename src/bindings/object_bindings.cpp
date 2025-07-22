// System includes

// External includes

// Project includes
#include "../utilities/object_utilities.h"
#include "casters/on_wstring_caster.h"
#include "object_bindings.h"


void ObjectBindings(nb::module_& m) {
    nb::class_<ON_Object>(m, "OpenNURBSObject")
        /*magic methods*/
        .def(nb::init<>())

        /*other methods*/
        .def("get_user_string", &ObjectUtilities::GetUserString)
        .def("is_corrupt", &ON_Object::IsCorrupt)
        .def("is_valid", &ON_Object::IsValid, nb::arg("text_log") = nullptr)
        .def("remove_user_string", &ObjectUtilities::RemoveUserString)
        .def("set_user_string", &ObjectUtilities::SetUserString)
        .def("user_string_count", &ON_Object::UserStringCount)
    ;
}
