/*
    src/bindings/layer_bindings.h: Exposing Layer to Python

    Copyright (c) 2025 Studio W Engineers

    All rights reserved. Use of this source code is governed by a
    BSD-style license that can be found in the LICENSE file.
*/
#pragma once

// System includes

// External includes

// Project includes
#include "bindings.h"


namespace LayerUtilities {
    bool SetName(ON_Layer& layer, const ON_wString& name);
    ON_wString ToString(const ON_Layer& layer);
}

void LayerBindings(nb::module_& m);
