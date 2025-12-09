/*
    src/point_table.h: Implementation details related to PointTable.

    Copyright (c) 2025 Studio W Engineers

    All rights reserved. Use of this source code is governed by a
    BSD-style license that can be found in the LICENSE file.
*/
#pragma once

// System includes

// External includes

// Project includes
#include "opennurbs_includes.h"


class PointTable {
public:
    /*constructors*/
    PointTable(std::shared_ptr<ONX_Model> model);

    /*add methods*/
    ON_UUID Add(double x, double y, double z, const ON_3dmObjectAttributes* obj_attr) const;
    ON_UUID Add(const ON_Point& point, const ON_3dmObjectAttributes* obj_attr) const;
    ON_UUID Add(const ON_3dPoint& point, const ON_3dmObjectAttributes* obj_attr) const;

    /*getters*/
    ON_Point* GetbyUUID(const ON_UUID obj_uuid);

    /*other methods*/
    int Count();
    bool IsPoint(const ON_ModelComponent* mc);

    /*PointTable Iterator*/
    class Iterator {
    public:
        Iterator(PointTable* table);

        ON_Point* operator*() const;
        Iterator& operator++();
        bool IsOver() const;

    private:
        PointTable* m_table;
        ONX_ModelComponentIterator m_iterator;
        mutable ON_ModelComponentReference m_current;
    };

    Iterator Begin();

private:
    std::shared_ptr<ONX_Model> m_model;
};
