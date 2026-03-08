#include "point_table.h"

/*constructors*/
PointTable::PointTable(std::shared_ptr<ONX_Model> model) {
    m_model = model;
}

/*add methods*/
ON_UUID PointTable::Add(double x, double y, double z, const ON_3dmObjectAttributes* obj_attr) const {
    if (m_model == nullptr) {
        return ON_nil_uuid;
    }

    ON_Point point(x, y, z);
    const ON_ModelComponent* mc = m_model->AddModelGeometryComponent(&point, obj_attr).ModelComponent();

    return (mc != nullptr) ? mc->Id() : ON_nil_uuid;
}

ON_UUID PointTable::Add(const ON_3dPoint& point, const ON_3dmObjectAttributes* obj_attr) const {
    return PointTable::Add(point.x, point.y, point.z, obj_attr);
}

ON_UUID PointTable::Add(const ON_Point& point, const ON_3dmObjectAttributes* obj_attr) const {
    return PointTable::Add(point.point, obj_attr);
}

/*getters*/
const ON_Point* PointTable::GetByUUID(const ON_UUID on_uuid) const {
    const ON_ModelComponent* mc = m_model->ComponentFromId(
        ON_ModelComponent::Type::ModelGeometry,
        on_uuid
    ).ModelComponent();
    const ON_ModelGeometryComponent* mgc = ON_ModelGeometryComponent::Cast(mc);

    if (!IsPoint(mgc)) {
        return nullptr;
    }
    return ON_Point::Cast(mgc->Geometry(nullptr));
}

ON_Point* PointTable::GetByUUIDExclusive(const ON_UUID on_uuid) const {
    const ON_ModelComponentReference& mcr = m_model->ComponentFromRuntimeSerialNumber(
        GetRuntimeSerialNumber(on_uuid)
    );
    ON_ModelGeometryComponent* mgc = ON_ModelGeometryComponent::Cast(
        mcr.ExclusiveModelComponent()
    );

    if (!IsPoint(mgc)) {
        return nullptr;
    }
    return ON_Point::Cast(mgc->ExclusiveGeometry());
}

ON__UINT64 PointTable::GetRuntimeSerialNumber(const ON_UUID on_uuid) const {
    return m_model->Manifest().ItemFromId(
        ON_ModelComponent::Type::ModelGeometry,
        on_uuid
    ).ComponentRuntimeSerialNumber();
}

/*other methods*/
int PointTable::Count() const {
    int count = 0;
    ONX_ModelComponentIterator mci(*m_model.get(), ON_ModelComponent::Type::ModelGeometry);
    ON_ModelComponentReference mcr = mci.FirstComponentReference();
    while (!mcr.IsEmpty()) {
        if (IsPoint(ON_ModelGeometryComponent::Cast(mcr.ModelComponent()))) {
            ++count;
        }
        mcr = mci.NextComponentReference();
    }

    return count;
}

bool PointTable::IsPoint(const ON_ModelGeometryComponent* mgc) {
    if (!mgc) {
        return false;
    }
    const ON_Geometry* geom = mgc->Geometry(nullptr);
    return (geom && geom->ObjectType() == ON::point_object);
}

/*PointTable Iterator*/
PointTable::Iterator::Iterator(PointTable* table)
    : m_table(table),
      m_iterator(*table->m_model.get(), ON_ModelComponent::Type::ModelGeometry) {
    m_current = m_iterator.FirstComponentReference();
}

const ON_Point* PointTable::Iterator::operator*() const {
    return m_table->GetByUUID(m_current.ModelComponentId());
}

PointTable::Iterator& PointTable::Iterator::operator++() {
    m_current = m_iterator.NextComponentReference();
    return *this;
}

bool PointTable::Iterator::IsOver() const {
    return m_current.IsEmpty();
}

PointTable::Iterator PointTable::Begin() {
    return Iterator(this);
}
