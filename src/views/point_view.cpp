#include "point_view.h"

/*constructor*/
PointView::PointView(
    const ON_Point* source,
    const ON_UUID on_uuid
) : m_point(source), m_uuid(on_uuid) {}

/*operators*/
bool PointView::operator==(const ON_Point& other) const {
    return m_point->point == other;
}

bool PointView::operator==(const ON_3dPoint& other) const {
    return m_point->point == other;
}

bool PointView::operator!=(const ON_Point& other) const {
    return m_point->point != other;
}

bool PointView::operator!=(const ON_3dPoint& other) const {
    return m_point->point != other;
}

/*other methods*/
double PointView::DistanceTo(const ON_3dPoint& point) const {
    return m_point->point.DistanceTo(point);
}

ON_UUID PointView::GetUUID() const {
    return m_uuid;
}

bool PointView::IsCoincident(const ON_3dPoint& point) const {
    return m_point->point.IsCoincident(point);
}

bool PointView::IsValid(ON_TextLog* text_log) const {
    return m_point->IsValid(text_log);
}

double PointView::X () const {
    return m_point->point.x;
}

double PointView::Y () const {
    return m_point->point.y;
}

double PointView::Z () const {
    return m_point->point.z;
}
