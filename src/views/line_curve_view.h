/*
    src/line_curve_view.h: Tiny wrapper to read-only access ON_LineCurve objects

    Copyright (c) 2026 Studio W Engineers

    All rights reserved. Use of this source code is governed by a
    BSD-style license that can be found in the LICENSE file.
*/
#pragma once

// System includes

// External includes

// Project includes
#include "../../lib/opennurbs/opennurbs.h"


class LineCurveView {
public:
    /*constructor*/
    LineCurveView(const ON_LineCurve* source, const ON_UUID on_uuid);

    /*destructor*/
    ~LineCurveView() = default;

    /*operators*/
    bool operator==(const ON_Line& other) const;
    bool operator!=(const ON_Line& other) const;

    /*other methods*/
    double DistanceTo(const ON_3dPoint& point, bool finite_chord) const;
    ON_UUID GetUUID() const;
    bool IsValid(ON_TextLog* text_log) const;
    double Length() const;

private:
    /*member variables*/
    const ON_LineCurve* m_line_curve;
    const ON_UUID m_uuid;
};
