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
    /*constructor*/
    PointTable(std::shared_ptr<ONX_Model> model);

    /*destructor*/
    ~PointTable() = default;

    /*add methods*/
    ON_UUID Add(double x, double y, double z, const ON_3dmObjectAttributes* obj_attr) const;
    ON_UUID Add(const ON_Point& point, const ON_3dmObjectAttributes* obj_attr) const;
    ON_UUID Add(const ON_3dPoint& point, const ON_3dmObjectAttributes* obj_attr) const;

    /*getters*/
    const ON_Point* GetByUUID(const ON_UUID obj_uuid) const;
    ON_Point* GetByUUIDExclusive(const ON_UUID obj_uuid) const;
    ON__UINT64 GetRuntimeSerialNumber(const ON_UUID on_uuid) const;

    /*other methods*/
    int Count() const;
    static bool IsPoint(const ON_ModelGeometryComponent* mgc);

    /*PointTable Iterator*/
    class Iterator {
    public:
        Iterator(PointTable* table);

        const ON_Point* operator*() const;
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
