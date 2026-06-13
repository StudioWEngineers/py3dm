#include "line_curve_view.h"

/*constructor*/
LineCurveView::LineCurveView(
    const ON_LineCurve* source,
    const ON_UUID on_uuid
) : m_line_curve(source), m_uuid(on_uuid) {}

/*operators*/
bool LineCurveView::operator==(const ON_Line& other) const {
    return m_line_curve->m_line == other;
}

bool LineCurveView::operator!=(const ON_Line& other) const {
    return m_line_curve->m_line != other;
}

/*other methods*/
double LineCurveView::DistanceTo(const ON_3dPoint& point, bool finite_chord) const {
    return m_line_curve->m_line.DistanceTo(point, finite_chord);
}

ON_UUID LineCurveView::GetUUID() const {
    return m_uuid;
}

bool LineCurveView::IsValid(ON_TextLog* text_log) const {
    return m_line_curve->IsValid(text_log);
}

double LineCurveView::Length () const {
    return m_line_curve->m_line.Length();
}
