/*
    src/mesh_view.h: Tiny wrapper to read-only access ON_Mesh objects

    Copyright (c) 2026 Studio W Engineers

    All rights reserved. Use of this source code is governed by a
    BSD-style license that can be found in the LICENSE file.
*/
#pragma once

// System includes

// External includes

// Project includes
#include "../../lib/opennurbs/opennurbs.h"


class MeshView {
public:
    /*constructor*/
    MeshView(const ON_Mesh* source, const ON_UUID on_uuid);

    /*destructor*/
    ~MeshView() = default;

    /*query methods*/
    bool IsCorrupt() const;
    bool IsEmpty() const ;
    bool IsNotEmpty() const ;
    bool IsValid() const ;

    /*count methods*/
    int FaceCount() const;
    int HiddenVertexCount() const;
    int InvalidFaceCount() const;
    int QuadCount() const;
    int TriangleCount() const;
    int VertexCount() const;

    /*has methods*/
    bool HasFaceNormals() const;
    bool HasNgons() const;
    bool HasPrincipalCurvatures() const;
    bool HasSurfaceParameters() const;
    bool HasVertexColors() const;
    bool HasVertexNormals() const;

    /*other methods*/
    ON_UUID GetUUID() const;

private:
    /*member variables*/
    const ON_Mesh* m_mesh;
    const ON_UUID m_uuid;
};