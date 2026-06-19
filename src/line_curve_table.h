/*
    src/line_curve_table.h: Implementation details related to LineCurveTable.

    Copyright (c) 2025 Studio W Engineers

    All rights reserved. Use of this source code is governed by a
    BSD-style license that can be found in the LICENSE file.
*/
#pragma once

// System includes

// External includes

// Project includes
#include "views/line_curve_view.h"
#include "../lib/opennurbs/opennurbs.h"


class LineCurveTable {
public:
    /*constructors*/
    LineCurveTable(std::shared_ptr<ONX_Model> model);

    /*add methods*/
    ON_UUID Add(const ON_3dPoint& start, const ON_3dPoint& end, const ON_3dmObjectAttributes* obj_attr) const;
    ON_UUID Add(const ON_Line& line, const ON_3dmObjectAttributes* obj_attr) const;
    ON_UUID Add(const ON_LineCurve& line, const ON_3dmObjectAttributes* obj_attr) const;

    /*getters*/
    LineCurveView* Get(const ON_UUID on_uuid);

    /*other methods*/
    int Count();
    bool IsLineCurve(const ON_ModelComponent* mc);

    /*LineCurveTable Iterator*/
    class Iterator {
    public:
        Iterator(LineCurveTable* table);

        LineCurveView* operator*() const;
        Iterator& operator++();
        bool IsOver() const;

    private:
        LineCurveTable* m_table;
        ONX_ModelComponentIterator m_iterator;
        mutable ON_ModelComponentReference m_current;
    };

    Iterator Begin();

private:
    std::shared_ptr<ONX_Model> m_model;
};
