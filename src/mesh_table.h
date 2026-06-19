/*
    src/point_table.h: Implementation details related to MeshTable.

    Copyright (c) 2026 Studio W Engineers

    All rights reserved. Use of this source code is governed by a
    BSD-style license that can be found in the LICENSE file.
*/
#pragma once

// System includes

// External includes

// Project includes
#include "../lib/opennurbs/opennurbs.h"
#include "views/mesh_view.h"


class MeshTable {
public:
    /*constructors*/
    MeshTable(std::shared_ptr<ONX_Model> model);

    /*destructor*/
    ~MeshTable() = default;

    /*add methods*/
    ON_UUID Add(const ON_3dmObjectAttributes* obj_attr) const;
    ON_UUID Add(const ON_Mesh& mesh, const ON_3dmObjectAttributes* obj_attr) const;
    ON_UUID Add(
        int initial_face_array_capacity,
        int initial_vertex_array_capacity,
        bool has_vertex_normals,
        bool has_texture_coordinates,
        const ON_3dmObjectAttributes* obj_attr
    ) const;

    /*getters*/
    MeshView* Get(const ON_UUID obj_uuid) const;
    ON_Mesh* GetExclusive(const ON_UUID obj_uuid) const;
    ON__UINT64 GetRuntimeSerialNumber(const ON_UUID obj_uuid) const;

    /*other methods*/
    int Count() const;
    static bool IsMesh(const ON_ModelComponent* mc);

    /*MeshTable Iterator*/
    class Iterator {
    public:
        Iterator(MeshTable* table);

        MeshView* operator*() const;
        Iterator& operator++();
        bool IsOver() const;

    private:
        MeshTable* m_table;
        ONX_ModelComponentIterator m_iterator;
        mutable ON_ModelComponentReference m_current;
    };

    Iterator Begin();

private:
    std::shared_ptr<ONX_Model> m_model;
};
