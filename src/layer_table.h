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


class LayerTable {
public:
    /*constructors*/
    LayerTable(std::shared_ptr<ONX_Model> model);

    /*deleters*/
    bool DeleteByName(ON_wString full_name);
    bool DeleteByUUID(ON_UUID on_uuid);

    /*getters*/
    ON_Layer* GetByIndex(int index);
    ON_Layer* GetByName(ON_wString full_name);
    ON_Layer* GetByUUID(ON_UUID on_uuid);

    /*other methods*/
    const ON_UUID Add(const ON_Layer& layer);
    int Count() const;
    const ON_wString GetFullPath(const ON_Layer* layer) const;
    int GetLayerIndex(ON_wString full_name);
    const ON_UUID GetLayerUUID(ON_wString full_name);
    bool Has(ON_wString full_name);
    int MaxIndex() const;

    /*LayerTable Iterator*/
    class Iterator {
    public:
        Iterator(LayerTable* table, int index);

        ON_Layer* operator*() const;
        Iterator& operator++();
        bool IsOver() const;

    private:
        LayerTable* m_table;
        unsigned int m_index;
        unsigned int m_count;
    };

    Iterator Begin();

private:
    std::shared_ptr<ONX_Model> m_model;
};
