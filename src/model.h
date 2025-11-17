/*
    src/model.h: Helper class for managing the openNURBS ONX_Model class.

    Copyright (c) 2025 Studio W Engineers

    All rights reserved. Use of this source code is governed by a
    BSD-style license that can be found in the LICENSE file.
*/
#pragma once

// System includes

// External includes

// Project includes
#include "layer_table.h"
#include "line_table.h"
#include "object_table.h"


class Model {
public:
    /*constructors*/
    Model();

    /*getters*/
    ON_wString GetApplicationDetails() const;
    ON_wString GetApplicationName() const;
    ON_wString GetApplicationUrl() const;
    int GetArchiveVersion() const;
    ON_wString GetCreatedBy() const;
    ON_wString GetLastEditedBy() const;
    int GetRevision() const;

    /*setters*/
    int NewRevision();
    void SetApplicationDetails(ON_wString details);
    void SetApplicationName(ON_wString name);
    void SetApplicationUrl(ON_wString url);
    void SetCreatedBy(ON_wString author);
    void SetLastEditedBy(ON_wString author);

    /*other methods*/
    bool Read(ON_wString path);
    void Reset();
    bool Write(ON_wString path, int version);

    /*tables*/
    LayerTable ModelLayerTable();
    LineTable ModelLineTable();
    ObjectTable ModelObjectTable();

private:
    std::shared_ptr<ONX_Model> p_model;
};