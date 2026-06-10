/*
    src/curve_view.h: Tiny wrapper to read-only access ON_Curve objects

    Copyright (c) 2026 Studio W Engineers

    All rights reserved. Use of this source code is governed by a
    BSD-style license that can be found in the LICENSE file.
*/
#pragma once

// System includes

// External includes

// Project includes
#include "../../lib/opennurbs/opennurbs.h"


class CurveView {
public:
    /*constructor*/
    CurveView(const ON_Curve* source, const ON_UUID on_uuid);

    /*destructor*/
    ~CurveView() = default;

    /*other methods*/
    ON_UUID GetUUID() const;
    bool IsClosed() const;
    bool IsLinear() const;
    bool IsValid(ON_TextLog* text_log) const;

private:
    /*member variables*/
    const ON_Curve* m_line_curve;
    const ON_UUID m_uuid;
};
