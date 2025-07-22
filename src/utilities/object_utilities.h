/*
    src/utilities/object_utilities.h: Helper functions for the ON_Object class.

    Copyright (c) 2025 Studio W Engineers

    All rights reserved. Use of this source code is governed by a
    BSD-style license that can be found in the LICENSE file.
*/
#pragma once

// System includes

// External includes

// Project includes
#include "../opennurbs_includes.h"


namespace ObjectUtilities {

    ON_wString GetUserString(const ON_Object& on_obj, const ON_wString& key);

    bool RemoveUserString(ON_Object& on_obj, const ON_wString& key);

    bool SetUserString(ON_Object& on_obj, const ON_wString& key, const ON_wString& value);

}
