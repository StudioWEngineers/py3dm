// System includes

// External includes

// Project includes
#include "layer_view_bindings.h"

#include "casters/color_caster.h"
#include "casters/on_wstring_caster.h"
#include "casters/uuid_caster.h"

#include "../views/layer_view.h"


void LayerViewBindings(nb::module_& m) {
    nb::class_<LayerView>(m, "LayerView")
        /*read-only static member variables*/
        .def_ro_static("path_separator", &ON_ModelComponent::NamePathSeparator)

        /*read-only properties*/
        .def_prop_ro("color", &LayerView::Color)
        .def_prop_ro("iges_level", &LayerView::IgesLevel)
        .def_prop_ro("is_expanded", &LayerView::IsExpanded)
        .def_prop_ro("is_locked", &LayerView::IsLocked)
        .def_prop_ro("is_visible", &LayerView::IsVisible)
        .def_prop_ro("layer_uuid", &LayerView::GetUUID)
        .def_prop_ro("line_type_index", &LayerView::LineTypeIndex)
        .def_prop_ro("name", &LayerView::Name)
        .def_prop_ro("parent_uuid", &LayerView::GetParentUUID)
        .def_prop_ro("parent_uuid_is_not_null", &LayerView::ParentIdIsNotNil)
        .def_prop_ro("parent_uuid_is_null", &LayerView::ParentIdIsNil)
        .def_prop_ro("plot_color", &LayerView::PlotColor)
        .def_prop_ro("plot_weight", &LayerView::PlotWeight)
        .def_prop_ro("render_material_index", &LayerView::RenderMaterialIndex)

        /*other methods*/
        .def("index", nb::overload_cast<>(&LayerView::Index, nb::const_))
        .def("index", nb::overload_cast<int>(&LayerView::Index, nb::const_))
        .def("is_valid", &LayerView::IsValid, nb::arg("text_log") = nullptr)
    ;
}
