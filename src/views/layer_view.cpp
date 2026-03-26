#include "layer_view.h"

/*constructor*/
LayerView::LayerView(const ON_Layer* source) : m_layer(source) {}

/*other methods*/
ON_Color LayerView::Color() const {
    return m_layer->Color();
}

ON_UUID LayerView::GetParentUUID() const {
    return m_layer->ParentId();
}

ON_UUID LayerView::GetUUID() const {
    return m_layer->Id();
}

int LayerView::IgesLevel() const {
    return m_layer->IgesLevel();
}

int LayerView::Index() const {
    return m_layer->Index();
}

int LayerView::Index(int return_value) const {
    return m_layer->Index(return_value);
}

bool LayerView::IsExpanded() const {
    return m_layer->m_bExpanded;
}

bool LayerView::IsLocked() const {
    return m_layer->IsLocked();
}

bool LayerView::IsValid(ON_TextLog* text_log) const {
    return m_layer->IsValid(text_log);
}

bool LayerView::IsVisible() const {
    return m_layer->IsVisible();
}

int LayerView::LineTypeIndex() const {
    return m_layer->m_linetype_index;
}

ON_wString LayerView::Name() const {
    return m_layer->Name();
}

bool LayerView::ParentIdIsNil() const {
    return m_layer->ParentIdIsNil();
}

bool LayerView::ParentIdIsNotNil() const {
    return m_layer->ParentIdIsNotNil();
}

ON_Color LayerView::PlotColor() const {
    return m_layer->PlotColor();
}

double LayerView::PlotWeight() const {
    return m_layer->PlotWeight();
}

int LayerView::RenderMaterialIndex() const {
    return m_layer->RenderMaterialIndex();
}
