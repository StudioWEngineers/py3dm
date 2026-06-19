#include "layer_table.h"


/*constructors*/
LayerTable::LayerTable(std::shared_ptr<ONX_Model> model) {
    m_model = model;
}

/*deleters*/
bool LayerTable::DeleteByName(const ON_wString layer_name) const {
    return DeleteByUUID(GetUUID(layer_name));
}

bool LayerTable::DeleteByUUID(const ON_UUID on_uuid) const {
    return !m_model->RemoveModelComponent(
        ON_ModelComponent::Type::Layer,
        on_uuid
    ).IsEmpty();
}

/*getters*/
LayerView* LayerTable::Get(int index) const {
    if (index < 0) {
        throw std::out_of_range("index must be greater than equal to 0!");
    }

    ON_ModelComponentReference mcr = m_model->ComponentFromIndex(ON_ModelComponent::Type::Layer, index);
    if (mcr.IsEmpty()) {
        return nullptr;
    }

    return new LayerView(ON_Layer::Cast(mcr.ModelComponent()));
}

LayerView* LayerTable::Get(ON_wString full_name) const {
    return Get(GetUUID(full_name));
}

LayerView* LayerTable::Get(const ON_UUID on_uuid) const {
    ON_ModelComponentReference mcr = m_model->ComponentFromId(ON_ModelComponent::Type::Layer, on_uuid);
    if (mcr.IsEmpty()) {
        return nullptr;
    }

    return new LayerView(ON_Layer::Cast(mcr.ModelComponent()));
}

ON_Layer* LayerTable::GetExclusive(const ON_UUID on_uuid) const {
    const ON_ModelComponentReference& mcr = m_model->ComponentFromRuntimeSerialNumber(
        GetRuntimeSerialNumber(on_uuid)
    );

    if (mcr.IsEmpty()) {
        return nullptr;
    }

    return ON_Layer::Cast(mcr.ExclusiveModelComponent());
}

/*other methods*/
const ON_UUID LayerTable::Add(const ON_Layer& layer) const {
    const ON_Layer* m_layer = ON_Layer::FromModelComponentRef(m_model->AddModelComponent(layer), nullptr);

    return (nullptr != m_layer) ? m_layer->Id() : ON_nil_uuid;
}

int LayerTable::Count() const {
    return m_model.get()->ActiveComponentCount(ON_ModelComponent::Type::Layer);
}

const ON_wString LayerTable::GetFullPath(const ON_Layer* layer) const {
    ONX_Model* model = m_model.get();
    if (model == nullptr) {
        return layer->NameAsPointer();
    }

    ON_wString full_name = layer->Name();
    ON_UUID parent_id = layer->ParentId();
    while (ON_UuidIsNotNil(parent_id)) {
        ON_ModelComponentReference mcr = model->LayerFromId(parent_id);
        const ON_Layer* layer = ON_Layer::Cast(mcr.ModelComponent());
        if (layer == nullptr) {
            break;
        }

        ON_wString parent_name = layer->Name();
        full_name = parent_name + ON_ModelComponent::NamePathSeparator + full_name;
        parent_id = layer->ParentId();
    }

    return full_name.Array();
}

int LayerTable::GetIndex(ON_wString full_name) const {
    const int max_index = m_model->Manifest().ComponentIndexLimit(ON_ModelComponent::Type::Layer);

    for (unsigned int i = 0; i < max_index; ++i) {
        ON_ModelComponentReference mcr = m_model->ComponentFromIndex(ON_ModelComponent::Type::Layer, i);
        if (mcr.IsEmpty())
            continue;

        const ON_Layer* layer = ON_Layer::Cast(mcr.ModelComponent());
        if (layer == nullptr) {
            continue;
        }

        if (full_name == GetFullPath(layer)) {
            return layer->Index();
        }
    }

    return ON_UNSET_INT_INDEX;
}

ON__UINT64 LayerTable::GetRuntimeSerialNumber(const ON_UUID on_uuid) const {
    return m_model->Manifest().ItemFromId(
        ON_ModelComponent::Type::Layer,
        on_uuid
    ).ComponentRuntimeSerialNumber();
}

const ON_UUID LayerTable::GetUUID(ON_wString full_name) const {
    const int count = m_model->Manifest().ComponentIndexLimit(ON_ModelComponent::Type::Layer);

    for (unsigned int i = 0; i < count; ++i) {
        ON_ModelComponentReference mcr = m_model->ComponentFromIndex(ON_ModelComponent::Type::Layer, i);
        if (mcr.IsEmpty())
            continue;

        const ON_Layer* layer = ON_Layer::Cast(mcr.ModelComponent());
        if (!layer)
            continue;

        if (full_name == layer->Name()) {
            return layer->Id();
        }
    }
    return ON_nil_uuid;
}

bool LayerTable::Has(ON_wString full_name) const {
    const int max_index = m_model->Manifest().ComponentIndexLimit(ON_ModelComponent::Type::Layer);

    for (unsigned int i = 0; i < max_index; ++i) {
        ON_ModelComponentReference mcr = m_model->ComponentFromIndex(ON_ModelComponent::Type::Layer, i);
        if (mcr.IsEmpty()) {
            continue;
        }

        const ON_Layer* layer = ON_Layer::Cast(mcr.ModelComponent());
        if (layer == nullptr)
            continue;

        if (full_name == layer->Name().Array()) {
            return true;
        }

        ON_wString name = layer->Name();
        ON_UUID parent_uuid = layer->ParentId();
        while (ON_UuidIsNotNil(parent_uuid)) {
            ON_ModelComponentReference mcr = m_model->LayerFromId(parent_uuid);
            const ON_Layer* layer = ON_Layer::Cast(mcr.ModelComponent());
            if (layer == nullptr) {
                break;
            }

            ON_wString parent_name = layer->Name();
            name = parent_name + ON_ModelComponent::NamePathSeparator + name;
            parent_uuid = layer->ParentId();
        }

        if (full_name == name.Array()) {
            return true;
        }
    }
    return false;
}

int LayerTable::MaxIndex() const {
    return m_model->Manifest().ComponentIndexLimit(ON_ModelComponent::Type::Layer);
}

/*LayerTable Iterator*/
LayerTable::Iterator::Iterator(LayerTable* table, int index)
    : m_table(table), m_index(index), m_count(table->MaxIndex()) {}

LayerView* LayerTable::Iterator::operator*() const {
    return m_table->Get(m_index);
}

LayerTable::Iterator& LayerTable::Iterator::operator++() {
    ++m_index;
    return *this;
}

bool LayerTable::Iterator::IsOver() const {
    return m_index >= m_count;
}

LayerTable::Iterator LayerTable::Begin() {
    return Iterator(this, 0);
}
