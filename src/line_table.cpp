#include "line_table.h"
#include<iostream>

/*constructors*/
LineTable::LineTable(std::shared_ptr<ONX_Model> model) {
    m_model = model;
}

/*add methods*/
ON_UUID LineTable::Add(const ON_3dPoint& from, const ON_3dPoint& to, const ON_3dmObjectAttributes* obj_attr) const {
    if (m_model == nullptr) {
        return ON_nil_uuid;
    }

    ON_LineCurve line(from, to);
    const ON_ModelComponent* mc = m_model->AddModelGeometryComponent(&line, obj_attr).ModelComponent();

    return (mc != nullptr) ? mc->Id() : ON_nil_uuid;
}

ON_UUID LineTable::Add(const ON_Line& line, const ON_3dmObjectAttributes* obj_attr) const {
    return LineTable::Add(line.from, line.to, obj_attr);
}

ON_UUID LineTable::Add(const ON_LineCurve& line, const ON_3dmObjectAttributes* obj_attr) const {
    return LineTable::Add(line.m_line, obj_attr);
}

/*getters*/
ON_Object* LineTable::GetbyUUID(const ON_UUID on_uuid) {
    const ON_ModelComponent* mc = m_model->ComponentFromId(ON_ModelComponent::Type::ModelGeometry, on_uuid).ModelComponent();
    const ON_ModelGeometryComponent* mgc = ON_ModelGeometryComponent::Cast(mc);

    if (const ON_LineCurve* lc = ON_LineCurve::Cast(mgc->Geometry(nullptr))) {
        return const_cast<ON_LineCurve*>(lc);
    }

    return nullptr;
}

/*LineTable Iterator*/
LineTable::Iterator::Iterator(LineTable* table)
    : m_table(table),
      m_iterator(*table->m_model.get(), ON_ModelComponent::Type::ModelGeometry) {
    m_current = m_iterator.FirstComponentReference();
}

ON_Object* LineTable::Iterator::operator*() const {
    return m_table->GetbyUUID(m_current.ModelComponentId());
}

LineTable::Iterator& LineTable::Iterator::operator++() {
    m_current = m_iterator.NextComponentReference();
    return *this;
}

bool LineTable::Iterator::IsOver() const {
    return m_current.IsEmpty();
}

LineTable::Iterator LineTable::Begin() {
    return Iterator(this);
}
