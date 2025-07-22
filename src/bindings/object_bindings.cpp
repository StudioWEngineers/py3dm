// System includes

// External includes

// Project includes
#include "casters/on_wstring_caster.h"
#include "object_bindings.h"


namespace ObjectUtilities {
    ON_wString GetUserString(const ON_Object& on_obj, const ON_wString& key) {
        ON_wString string_value;
        on_obj.GetUserString(key, string_value);

        return string_value;
    }

    bool RemoveUserString(ON_Object& on_obj, const ON_wString& key) {
        return on_obj.SetUserString(key, nullptr);
    }

    bool SetUserString(ON_Object& on_obj, const ON_wString& key, const ON_wString& value) {
        return on_obj.SetUserString(key, value);
    }
} // namespace ObjectUtilities

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
