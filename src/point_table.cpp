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
ON_Point* PointTable::GetbyUUID(const ON_UUID on_uuid) {
    const ON_ModelComponent* mc = m_model->ComponentFromId(ON_ModelComponent::Type::ModelGeometry, on_uuid).ModelComponent();

    if (!IsPoint(mc)) {
        return nullptr;
    }

    const ON_ModelGeometryComponent* mgc = ON_ModelGeometryComponent::Cast(mc);
    return const_cast<ON_Point*>(ON_Point::Cast(mgc->Geometry(nullptr)));
}

/*other methods*/
int PointTable::Count() {
    int count = 0;
    ONX_ModelComponentIterator mci(*m_model.get(), ON_ModelComponent::Type::ModelGeometry);
    ON_ModelComponentReference mcr = mci.FirstComponentReference();
    while (!mcr.IsEmpty()) {
        if (PointTable::IsPoint(mcr.ModelComponent())) {
            ++count;
        }
        mcr = mci.NextComponentReference();
    }

    return count;
}

bool PointTable::IsPoint(const ON_ModelComponent* mc) {
    const ON_ModelGeometryComponent* mgc = ON_ModelGeometryComponent::Cast(mc);
    if (mgc == nullptr) {
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

ON_Point* PointTable::Iterator::operator*() const {
    return m_table->GetbyUUID(m_current.ModelComponentId());
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
