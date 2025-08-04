#include "object_table.h"


/*constructors*/
ObjectTable::ObjectTable(std::shared_ptr<ONX_Model> model) {
    m_model = model;
}

/*add methods*/
ON_UUID ObjectTable::AddLine(const ON_3dPoint& start, const ON_3dPoint& end, const ON_3dmObjectAttributes* obj_attr) const {
    if (m_model == nullptr) {
        return ON_nil_uuid;
    }

    ON_LineCurve line(start, end);
    const ON_ModelComponent* mc = m_model->AddModelGeometryComponent(&line, obj_attr).ModelComponent();
    if (mc != nullptr) {
        return mc->Id();
    }

    return ON_nil_uuid;
}

ON_UUID ObjectTable::AddLine(const ON_Line& line, const ON_3dmObjectAttributes* obj_attr) const {
    return ObjectTable::AddLine(line.from, line.to, obj_attr);
}

ON_UUID ObjectTable::AddLine(const ON_LineCurve& line, const ON_3dmObjectAttributes* obj_attr) const {
    return ObjectTable::AddLine(line.m_line, obj_attr);
}

ON_UUID ObjectTable::AddPoint(double x, double y, double z, const ON_3dmObjectAttributes* obj_attr) const {
    if (m_model == nullptr) {
        return ON_nil_uuid;
    }

    ON_Point point(x, y, z);
    const ON_ModelComponent* mc = m_model->AddModelGeometryComponent(&point, obj_attr).ModelComponent();
    if (mc != nullptr) {
        return mc->Id();
    }

    return ON_nil_uuid;
}

ON_UUID ObjectTable::AddPoint(const ON_3dPoint& point, const ON_3dmObjectAttributes* obj_attr) const {
    return ObjectTable::AddPoint(point.x, point.y, point.z, obj_attr);
}

ON_UUID ObjectTable::AddPoint(const ON_Point& point, const ON_3dmObjectAttributes* obj_attr) const {
    return ObjectTable::AddPoint(point.point, obj_attr);
}

/*other methods*/
int ObjectTable::Count() const {
    return m_model->Manifest().ActiveComponentCount(ON_ModelComponent::Type::ModelGeometry);
}

bool ObjectTable::DeleteByUUID(ON_UUID on_uuid) {
    return !m_model->RemoveModelComponent(ON_ModelComponent::Type::ModelGeometry, on_uuid).IsEmpty();
}

/*ObjectTable Iterator*/
ObjectTable::Iterator::Iterator(ObjectTable* table)
    : m_table(table),
      m_iterator(*table->m_model.get(), ON_ModelComponent::Type::ModelGeometry) {
    m_current = m_iterator.FirstComponentReference();
}

std::shared_ptr<ON_Geometry> ObjectTable::Iterator::operator*() const {
    if (!m_current.IsEmpty()) {
        const ON_ModelGeometryComponent* geom = ON_ModelGeometryComponent::Cast(m_current.ModelComponent());
        if (geom) {
            const ON_Geometry* geometry = geom->Geometry(nullptr);
            if (geometry) {

                return std::shared_ptr<ON_Geometry>(const_cast<ON_Geometry*>(geometry), [](ON_Geometry*){});
            }
        }
    }
    return nullptr;
}

ObjectTable::Iterator& ObjectTable::Iterator::operator++() {
    m_current = m_iterator.NextComponentReference();
    return *this;
}

bool ObjectTable::Iterator::IsOver() const {
    return m_current.IsEmpty();
}

ObjectTable::Iterator ObjectTable::Begin() {
    return Iterator(this);
}
