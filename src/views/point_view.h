/*
    src/point_view.h: Tiny wrapper to read-only access ON_Point objects

    Copyright (c) 2026 Studio W Engineers

    All rights reserved. Use of this source code is governed by a
    BSD-style license that can be found in the LICENSE file.
*/
#pragma once

// System includes

// External includes

// Project includes
#include "../../lib/opennurbs/opennurbs.h"


class PointView {
public:
    /*constructor*/
    PointView(const ON_Point* source, const ON_UUID on_uuid);

    /*destructor*/
    ~PointView() = default;

    /*operators*/
    bool operator==(const ON_Point& other) const;
    bool operator==(const ON_3dPoint& other) const;
    bool operator!=(const ON_Point& other) const;
    bool operator!=(const ON_3dPoint& other) const;

    /*other methods*/
    double DistanceTo(const ON_3dPoint& point) const;
    ON_UUID GetUUID() const;
    bool IsCoincident(const ON_3dPoint& point) const;
    bool IsValid(ON_TextLog* text_log) const;
    double X() const;
    double Y() const;
    double Z() const;

private:
    /*member variables*/
    const ON_Point* m_point;
    const ON_UUID m_uuid;
};
