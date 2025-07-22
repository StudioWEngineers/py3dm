/*
    src/utilities/layer_utilities.h: Helper functions for the ON_layer class.

    Copyright (c) 2025 Studio W Engineers

    All rights reserved. Use of this source code is governed by a
    BSD-style license that can be found in the LICENSE file.
*/
#pragma once

// System includes
#include <string>

// External includes

// Project includes
#include "../opennurbs_includes.h"


namespace LayerUtilities {

    std::string GetPathSeparator();

    bool SetName(ON_Layer& layer, const ON_wString& name);

    std::string ToString(const ON_Layer& layer);

}
