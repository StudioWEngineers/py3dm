#include "mesh_view.h"

/*constructor*/
MeshView::MeshView(
    const ON_Mesh* source,
    const ON_UUID on_uuid
) : m_mesh(source), m_uuid(on_uuid) {}

/*query methods*/
bool MeshView::IsCorrupt() const {
    return m_mesh->IsCorrupt(false, true, nullptr);
}

bool MeshView::IsEmpty() const {
    return m_mesh->IsEmpty();
}

bool MeshView::IsNotEmpty() const {
    return m_mesh->IsNotEmpty();
}

bool MeshView::IsValid() const {
    return m_mesh->IsValid(nullptr);
}

/*count methods*/
int MeshView::FaceCount() const {
    return m_mesh->FaceCount();
}

int MeshView::HiddenVertexCount() const {
    return m_mesh->HiddenVertexCount();
}

int MeshView::InvalidFaceCount() const {
    return m_mesh->InvalidFaceCount();
}

int MeshView::QuadCount() const {
    return m_mesh->QuadCount();
}

int MeshView::TriangleCount() const {
    return m_mesh->TriangleCount();
}

int MeshView::VertexCount() const {
    return m_mesh->VertexCount();
}

/*has methods*/
bool MeshView::HasFaceNormals() const {
    return m_mesh->HasFaceNormals();
}

bool MeshView::HasNgons() const {
    return m_mesh->HasNgons();
}

bool MeshView::HasPrincipalCurvatures() const {
    return m_mesh->HasPrincipalCurvatures();
}

bool MeshView::HasSurfaceParameters() const {
    return m_mesh->HasSurfaceParameters();
}

bool MeshView::HasVertexColors() const {
    return m_mesh->HasVertexColors();
}

bool MeshView::HasVertexNormals() const {
    return m_mesh->HasVertexNormals();
}

/*other methods*/
ON_UUID MeshView::GetUUID() const {
    return m_uuid;
}
