#include "curve_view.h"

/*constructor*/
CurveView::CurveView(
    const ON_Curve* source,
    const ON_UUID on_uuid
) : m_line_curve(source), m_uuid(on_uuid) {}

/*other methods*/
ON_UUID CurveView::GetUUID() const {
    return m_uuid;
}

bool CurveView::IsClosed() const {
    return m_line_curve->IsClosed();
}

bool CurveView::IsLinear() const {
    return m_line_curve->IsLinear();
}

bool CurveView::IsValid(ON_TextLog* text_log) const {
    return m_line_curve->IsValid(text_log);
}
