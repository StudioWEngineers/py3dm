/*
    src/bindings/object_attributes_bindings.h: Exposing ON_3dmObjectAttributes to Python

    Copyright (c) 2025 Studio W Engineers

    All rights reserved. Use of this source code is governed by a
    BSD-style license that can be found in the LICENSE file.
*/
#pragma once

// System includes

// External includes

// Project includes
#include "bindings.h"


namespace ObjectAttributesUtilities{
    bool SetName(ON_3dmObjectAttributes& obj_attr, const ON_wString name, bool fix_invalid_name);
};

void ObjectAttributesBindings(nb::module_& m);
