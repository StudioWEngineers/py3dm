#include "curve_table.h"


/*constructors*/
CurveTable::CurveTable(std::shared_ptr<ONX_Model> model) {
    m_model = model;
}

/*add methods*/
ON_UUID CurveTable::Add(const ON_3dPoint& from, const ON_3dPoint& to, const ON_3dmObjectAttributes* obj_attr) const {
    if (m_model == nullptr) {
        return ON_nil_uuid;
    }

    ON_LineCurve line(from, to);
    const ON_ModelComponent* mc = m_model->AddModelGeometryComponent(&line, obj_attr).ModelComponent();

    return (mc != nullptr) ? mc->Id() : ON_nil_uuid;
}

ON_UUID CurveTable::Add(const ON_Line& line, const ON_3dmObjectAttributes* obj_attr) const {
    return CurveTable::Add(line.from, line.to, obj_attr);
}

ON_UUID CurveTable::Add(const ON_LineCurve& line, const ON_3dmObjectAttributes* obj_attr) const {
    return CurveTable::Add(line.m_line, obj_attr);
}

/*getters*/
ON_Object* CurveTable::GetbyUUID(const ON_UUID on_uuid) {
    const ON_ModelComponent* mc = m_model->ComponentFromId(ON_ModelComponent::Type::ModelGeometry, on_uuid).ModelComponent();

    if (!IsCurve(mc)) {
        return nullptr;
    }

    const ON_ModelGeometryComponent* mgc = ON_ModelGeometryComponent::Cast(mc);
    return const_cast<ON_LineCurve*>(ON_LineCurve::Cast(mgc->Geometry(nullptr)));
}


/*other methods*/
int CurveTable::Count() {
    int count = 0;
    ONX_ModelComponentIterator mci(*m_model.get(), ON_ModelComponent::Type::ModelGeometry);
    ON_ModelComponentReference mcr = mci.FirstComponentReference();

    while (!mcr.IsEmpty()) {
        if (CurveTable::IsCurve(mcr.ModelComponent())) {
            ++count;
        }
        mcr = mci.NextComponentReference();
    }

    return count;
}

bool CurveTable::IsCurve(const ON_ModelComponent* mc) {
    const ON_ModelGeometryComponent* mgc = ON_ModelGeometryComponent::Cast(mc);
    if (mgc == nullptr) {
        return false;
    }

    const ON_Geometry* geom = mgc->Geometry(nullptr);
    return (geom && geom->ObjectType() == ON::curve_object);
}

/*CurveTable Iterator*/
CurveTable::Iterator::Iterator(CurveTable* table)
    : m_table(table),
      m_iterator(*table->m_model.get(), ON_ModelComponent::Type::ModelGeometry) {
    m_current = m_iterator.FirstComponentReference();
}

ON_Object* CurveTable::Iterator::operator*() const {
    return m_table->GetbyUUID(m_current.ModelComponentId());
}

CurveTable::Iterator& CurveTable::Iterator::operator++() {
    m_current = m_iterator.NextComponentReference();
    return *this;
}

bool CurveTable::Iterator::IsOver() const {
    return m_current.IsEmpty();
}

CurveTable::Iterator CurveTable::Begin() {
    return Iterator(this);
}
