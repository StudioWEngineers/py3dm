/*
    src/layer_table.h: Implementation details related to LayerTable.

    Copyright (c) 2025 Studio W Engineers

    All rights reserved. Use of this source code is governed by a
    BSD-style license that can be found in the LICENSE file.
*/
#pragma once

// System includes

// External includes

// Project includes
#include "opennurbs_includes.h"

#include "views/layer_view.h"


class LayerTable {
public:
    /*constructor*/
    LayerTable(std::shared_ptr<ONX_Model> model);

    /*destructor*/
    ~LayerTable() = default;

    /*deleters*/
    bool DeleteByName(const ON_wString full_name) const;
    bool DeleteByUUID(const ON_UUID on_uuid) const;

    /*getters*/
    LayerView* GetByIndex(int index) const;
    LayerView* GetByName(ON_wString full_name) const;
    LayerView* GetByUUID(const ON_UUID on_uuid) const;
    ON_Layer* GetByUUIDExclusive(const ON_UUID on_uuid) const;

    /*other methods*/
    const ON_UUID Add(const ON_Layer& layer) const;
    int Count() const;
    const ON_wString GetFullPath(const ON_Layer* layer) const;
    int GetIndex(ON_wString full_name) const;
    ON__UINT64 GetRuntimeSerialNumber(const ON_UUID on_uuid) const;
    const ON_UUID GetUUID(ON_wString full_name) const;
    bool Has(ON_wString full_name) const;
    int MaxIndex() const;

    /*LayerTable Iterator*/
    class Iterator {
    public:
        /*constructor*/
        Iterator(LayerTable* table, int index);

        /*destructor*/
        ~Iterator() = default;

        /*operators*/
        LayerView* operator*() const;
        Iterator& operator++();

        /*other methods*/
        bool IsOver() const;

    private:
        /*member variables*/
        LayerTable* m_table;
        unsigned int m_index;
        unsigned int m_count;
    };

    Iterator Begin();

private:
    std::shared_ptr<ONX_Model> m_model;
};
