// System includes

// External includes

// Project includes
#include "object_utilities.h"


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
