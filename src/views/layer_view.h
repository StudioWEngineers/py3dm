/*
    src/point_view.h: Tiny wrapper to read-only access ON_Layer objects

    Copyright (c) 2026 Studio W Engineers

    All rights reserved. Use of this source code is governed by a
    BSD-style license that can be found in the LICENSE file.
*/
#pragma once

// System includes

// External includes

// Project includes
#include "../opennurbs_includes.h"


class LayerView {
public:
    /*constructor*/
    LayerView(const ON_Layer* source);

    /*destructor*/
    ~LayerView() = default;

    /*other methods*/
    ON_Color Color() const;
    ON_UUID GetParentUUID() const;
    ON_UUID GetUUID() const;
    int IgesLevel() const;
    int Index() const;
    int Index(int return_value) const;
    bool IsExpanded() const;
    bool IsLocked() const;
    bool IsValid(ON_TextLog* text_log) const;
    bool IsVisible() const;
    int LineTypeIndex() const;
    ON_wString Name() const;
    bool ParentIdIsNil() const;
    bool ParentIdIsNotNil() const;
    ON_Color PlotColor() const;
    double PlotWeight() const;
    int RenderMaterialIndex() const;

private:
    /*member variables*/
    const ON_Layer* m_layer;
};
