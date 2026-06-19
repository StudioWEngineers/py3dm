#include "mesh_table.h"

/*constructors*/
MeshTable::MeshTable(std::shared_ptr<ONX_Model> model) {
    m_model = model;
}

/*add methods*/
ON_UUID MeshTable::Add(const ON_3dmObjectAttributes* obj_attr) const {
    ON_Mesh mesh;
    const ON_ModelComponent* mc = m_model->AddModelGeometryComponent(&mesh, obj_attr).ModelComponent();
    return (mc != nullptr) ? mc->Id() : ON_nil_uuid;
}

ON_UUID MeshTable::Add(const ON_Mesh& mesh, const ON_3dmObjectAttributes* obj_attr) const {
    const ON_ModelComponent* mc = m_model->AddModelGeometryComponent(&mesh, obj_attr).ModelComponent();
    return (mc != nullptr) ? mc->Id() : ON_nil_uuid;
}

ON_UUID MeshTable::Add(
    int initial_face_array_capacity,
    int initial_vertex_array_capacity,
    bool has_vertex_normals,
    bool has_texture_coordinates,
    const ON_3dmObjectAttributes* obj_attr
) const {
    ON_Mesh mesh(
        initial_face_array_capacity,
        initial_vertex_array_capacity,
        has_vertex_normals,
        has_texture_coordinates
    );
    const ON_ModelComponent* mc = m_model->AddModelGeometryComponent(&mesh, obj_attr).ModelComponent();
    return (mc != nullptr) ? mc->Id() : ON_nil_uuid;
}

/*getters*/
MeshView* MeshTable::Get(const ON_UUID on_uuid) const {
    const ON_ModelComponent* mc = m_model->ComponentFromId(ON_ModelComponent::Type::ModelGeometry, on_uuid).ModelComponent();

    if (!IsMesh(mc)) {
        return nullptr;
    }

    const ON_ModelGeometryComponent* mgc = ON_ModelGeometryComponent::Cast(mc);
    return new MeshView(ON_Mesh::Cast(mgc->Geometry(nullptr)), mgc->ModelObjectId());
}

ON_Mesh* MeshTable::GetExclusive(const ON_UUID obj_uuid) const {
    const ON_ModelComponentReference& mcr = m_model->ComponentFromRuntimeSerialNumber(
        GetRuntimeSerialNumber(obj_uuid)
    );
    ON_ModelGeometryComponent* mgc = ON_ModelGeometryComponent::Cast(
        mcr.ExclusiveModelComponent()
    );

    return mgc? ON_Mesh::Cast(mgc->ExclusiveGeometry()) : nullptr;
}

ON__UINT64 MeshTable::GetRuntimeSerialNumber(const ON_UUID obj_uuid) const {
    return m_model->Manifest().ItemFromId(
        ON_ModelComponent::Type::ModelGeometry,
        obj_uuid
    ).ComponentRuntimeSerialNumber();
}

/*other methods*/
int MeshTable::Count() const {
    int count = 0;
    ONX_ModelComponentIterator mci(*m_model.get(), ON_ModelComponent::Type::ModelGeometry);
    ON_ModelComponentReference mcr = mci.FirstComponentReference();
    while (!mcr.IsEmpty()) {
        if (MeshTable::IsMesh(mcr.ModelComponent())) {
            ++count;
        }
        mcr = mci.NextComponentReference();
    }

    return count;
}

bool MeshTable::IsMesh(const ON_ModelComponent* mc) {
    const ON_ModelGeometryComponent* mgc = ON_ModelGeometryComponent::Cast(mc);
    if (mgc == nullptr) {
        return false;
    }

    const ON_Geometry* geom = mgc->Geometry(nullptr);
    return (geom && geom->ObjectType() == ON::mesh_object);
}

/*MeshTable Iterator*/
MeshTable::Iterator::Iterator(MeshTable* table)
    : m_table(table),
      m_iterator(*table->m_model.get(), ON_ModelComponent::Type::ModelGeometry) {
    m_current = m_iterator.FirstComponentReference();
}

MeshView* MeshTable::Iterator::operator*() const {
    return m_table->Get(m_current.ModelComponentId());
}

MeshTable::Iterator& MeshTable::Iterator::operator++() {
    m_current = m_iterator.NextComponentReference();
    return *this;
}

bool MeshTable::Iterator::IsOver() const {
    return m_current.IsEmpty();
}

MeshTable::Iterator MeshTable::Begin() {
    return Iterator(this);
}
