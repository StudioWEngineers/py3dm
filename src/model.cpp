#include "model.h"


Model::Model() : p_model(std::make_shared<ONX_Model>()) {}


bool Model::Read(ON_wString path) {
    p_model.reset(new ONX_Model());

    if (p_model->Read(path)) {
        return true;
    }

    p_model.reset();
    return false;
}

void Model::Reset() {
    p_model.reset();
}

bool Model::Write(ON_wString path, int version) {
    return p_model->Write(path, version);
}


ON_wString Model::GetApplicationDetails() const {
    if (p_model.get() != nullptr) {
        return p_model->m_properties.m_Application.m_application_details;
    }
    return ON_wString::EmptyString;
}

ON_wString Model::GetApplicationName() const {
    if (p_model.get() != nullptr) {
        return p_model->m_properties.m_Application.m_application_name;
    }
    return ON_wString::EmptyString;
}

ON_wString Model::GetApplicationUrl() const {
    if (p_model.get() != nullptr) {
        return p_model->m_properties.m_Application.m_application_URL;
    }
    return ON_wString::EmptyString;
}

int Model::GetArchiveVersion() const {
    if (p_model.get() != nullptr) {
        return p_model->m_3dm_file_version;
    }
    return 0;
}

ON_wString Model::GetCreatedBy() const {
    if (p_model.get() != nullptr) {
        return p_model->m_properties.m_RevisionHistory.m_sCreatedBy;
    }
    return ON_wString::EmptyString;
}

ON_wString Model::GetLastEditedBy() const {
    if (p_model.get() != nullptr) {
        return p_model->m_properties.m_RevisionHistory.m_sLastEditedBy;
    }
    return ON_wString::EmptyString;
}

int Model::GetRevision() const {
    int revision_number = 0;
    if (p_model.get() != nullptr) {
        revision_number = p_model->m_properties.m_RevisionHistory.m_revision_count;
    }
    return revision_number;
}


int Model::NewRevision() {
    if (p_model.get() != nullptr) {
        return p_model->m_properties.m_RevisionHistory.NewRevision();
    }
    return 0;
}

void Model::SetApplicationDetails(ON_wString details) {
    if (p_model.get() != nullptr) {
        p_model->m_properties.m_Application.m_application_details = details;
    }
}

void Model::SetApplicationName(ON_wString name) {
    if (p_model.get() != nullptr) {
        p_model->m_properties.m_Application.m_application_name = name;
    }
}

void Model::SetApplicationUrl(ON_wString url) {
    if (p_model.get() != nullptr) {
        p_model->m_properties.m_Application.m_application_URL = url;
    }
}

void Model::SetCreatedBy(ON_wString author) {
    if (p_model.get() != nullptr) {
        p_model->m_properties.m_RevisionHistory.m_sCreatedBy = author;
    }
}

void Model::SetLastEditedBy(ON_wString author) {
    if (p_model.get() != nullptr) {
        p_model->m_properties.m_RevisionHistory.m_sLastEditedBy = author;
    }
}


LayerTable Model::ModelLayerTable() {
    return LayerTable(p_model);
}

ObjectTable Model::ModelObjectTable() {
    return ObjectTable(p_model);
}
