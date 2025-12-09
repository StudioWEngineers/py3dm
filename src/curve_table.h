/*
    src/curve_table.h: Implementation details related to CurveTable.

    Copyright (c) 2025 Studio W Engineers

    All rights reserved. Use of this source code is governed by a
    BSD-style license that can be found in the LICENSE file.
*/
#pragma once

// System includes

// External includes

// Project includes
#include "opennurbs_includes.h"


class CurveTable {
public:
    /*constructors*/
    CurveTable(std::shared_ptr<ONX_Model> model);

    /*add methods*/
    ON_UUID Add(const ON_3dPoint& start, const ON_3dPoint& end, const ON_3dmObjectAttributes* obj_attr) const;
    ON_UUID Add(const ON_Line& line, const ON_3dmObjectAttributes* obj_attr) const;
    ON_UUID Add(const ON_LineCurve& line, const ON_3dmObjectAttributes* obj_attr) const;

    /*getters*/
    ON_Object* GetbyUUID(const ON_UUID on_uuid);

    /*other methods*/
    int Count();
    bool IsCurve(const ON_ModelComponent* mc);

    /*CurveTable Iterator*/
    class Iterator {
    public:
        Iterator(CurveTable* table);

        ON_Object* operator*() const;
        Iterator& operator++();
        bool IsOver() const;

    private:
        CurveTable* m_table;
        ONX_ModelComponentIterator m_iterator;
        mutable ON_ModelComponentReference m_current;
    };

    Iterator Begin();

private:
    std::shared_ptr<ONX_Model> m_model;
};
