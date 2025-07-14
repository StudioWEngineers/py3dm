/*
    src/bindings/casters/color_caster.h: Direct conversion ON_Color <-> Python tuple[int, int, int, int]

    Copyright (c) 2025 Studio W Engineers

    All rights reserved. Use of this source code is governed by a
    BSD-style license that can be found in the LICENSE file.
*/
#pragma once

#include "../bindings.h"

namespace nb = nanobind;

namespace nanobind::detail {

template <>
struct type_caster<ON_Color> {
public:
    NB_TYPE_CASTER(ON_Color, const_name("tuple"))

    bool from_python(handle src, uint8_t flags, cleanup_list* cleanup) noexcept {
        if (!nb::isinstance<nb::tuple>(src) || nb::len(src) != 4)
            return false;

        try {
            int r = cast<int>(src[0]);
            int g = cast<int>(src[1]);
            int b = cast<int>(src[2]);
            int a = cast<int>(src[3]);

            // Invert alpha channel (Python uses standard alpha, OpenNURBS inverts)
            value = ON_Color(r, g, b, 255 - a);
            return true;
        } catch (...) {
            return false;
        }
    }

    static handle from_cpp(const ON_Color& color, rv_policy, cleanup_list*) noexcept {
        int r = color.Red();
        int g = color.Green();
        int b = color.Blue();
        int a = 255 - color.Alpha();  // Invert alpha to match Python expectation
        return nb::make_tuple(r, g, b, a).release();
    }
};

} // namespace nanobind::detail
