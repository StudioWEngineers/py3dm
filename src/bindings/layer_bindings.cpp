// System includes
#include <sstream>

// External includes

// Project includes
#include "casters/color_caster.h"
#include "casters/on_wstring_caster.h"
#include "casters/uuid_caster.h"
#include "layer_bindings.h"


namespace LayerUtilities {
    bool SetName(ON_Layer& layer, const ON_wString& name) {
        return layer.SetName(name);
    }

    ON_wString ToString(const ON_Layer& layer) {
        char p_uuid_str[37];
        char uuid_str[37];
        ON_UuidToString(layer.ParentId(), p_uuid_str);
        ON_UuidToString(layer.Id(), uuid_str);

        ON_Color color = layer.Color();
        std::wostringstream color_stream;
        color_stream << "(" << color.Red() << ", " << color.Green() << ", " << color.Blue() << ", " << 255 - color.Alpha() << ")";

        ON_Color p_color = layer.PlotColor();
        std::wostringstream p_color_stream;
        p_color_stream << "(" << p_color.Red() << ", " << p_color.Green() << ", " << p_color.Blue() << ", " << 255 - p_color.Alpha() << ")";

        std::wostringstream output;
        output << "Layer with properties:\n"
               << "\tcolor = " << color_stream.str() << "\n"
               << "\tiges_level = " << layer.IgesLevel() << "\n"
               << "\tindex = " << layer.Index() << "\n"
               << "\tis_expanded = " << std::boolalpha << layer.m_bExpanded << "\n"
               << "\tis_locked = " << layer.IsLocked() << "\n"
               << "\tis_visible = " << layer.IsVisible() << "\n"
               << "\tlayer_uuid = " << uuid_str << "\n"
               << "\tline_type_index = " << layer.LinetypeIndex() << "\n"
               << "\tname = '" << layer.NameAsPointer() << "'\n"
               << "\tparent_uuid = " << p_uuid_str << "\n"
               << "\tpath separator = " << ON_ModelComponent::NamePathSeparator.Array() << "\n"
               << "\tpersistent_locking = " << layer.PersistentLocking() << "\n"
               << "\tpersistent_visibility = " << layer.PersistentVisibility() << "\n"
               << "\tplot_color = " << p_color_stream.str() << "\n"
               << "\tplot_weight = " << layer.PlotWeight() << "\n"
               << "\trender_material_index = " << layer.RenderMaterialIndex() << "\n";
        return ON_wString(output.str().c_str());
    }
} // namespace LayerUtilities

void LayerBindings(nb::module_& m) {
    nb::class_<ON_Layer>(m, "Layer")
        /*magic methods*/
        .def(nb::init<>())

        .def("__repr__", [](const ON_Layer& self) {return LayerUtilities::ToString(self);})

        /*read-write properties*/
        .def_prop_rw("color", &ON_Layer::Color, &ON_Layer::SetColor)

        .def_prop_rw("iges_level", &ON_Layer::IgesLevel, &ON_Layer::SetIgesLevel)

        .def_prop_rw(
            "is_expanded",
            [](const ON_Layer& self) {
                return self.m_bExpanded;
            },
            [](ON_Layer& self, bool is_expanded) {
                self.m_bExpanded = is_expanded;
            }
        )

        .def_prop_rw("is_locked", &ON_Layer::IsLocked, &ON_Layer::SetLocked)

        .def_prop_rw(
            "is_visible",
            [](const ON_Layer& self) {
                return self.IsVisible();
            },
            [](ON_Layer& self, bool is_visible) {
                self.SetVisible(is_visible);
            }
        )

        .def_prop_rw(
            "layer_uuid",
            [](const ON_Layer& self) {
                return self.Id();
            },
            [](ON_Layer& self, ON_UUID on_uuid) {
                self.SetId(on_uuid);
            }
        )

        .def_prop_rw("line_type_index", &ON_Layer::LinetypeIndex, &ON_Layer::SetLinetypeIndex)

        .def_prop_rw("parent_uuid", &ON_Layer::ParentLayerId, &ON_Layer::SetParentLayerId)

        .def_prop_rw("persistent_locking", &ON_Layer::PersistentLocking, &ON_Layer::SetPersistentLocking)

        .def_prop_rw("persistent_visibility", &ON_Layer::PersistentVisibility, &ON_Layer::SetPersistentVisibility)

        .def_prop_rw("plot_color", &ON_Layer::PlotColor, &ON_Layer::SetPlotColor)

        .def_prop_rw("plot_weight", &ON_Layer::PlotWeight, &ON_Layer::SetPlotWeight)

        .def_prop_rw("render_material_index", &ON_Layer::RenderMaterialIndex, &ON_Layer::SetRenderMaterialIndex)

        .def_prop_rw(
            "index",
            [](const ON_Layer& self) {
                return self.Index();
            },
            [](ON_Layer& self, int index) {
                self.SetIndex(index);
            }
        )

        /*read-only properties*/
        .def_prop_ro("parent_uuid_is_not_null", &ON_Layer::ParentIdIsNotNil)

        .def_prop_ro("parent_uuid_is_null", &ON_Layer::ParentIdIsNil)

        .def_ro_static("path_separator", &ON_ModelComponent::NamePathSeparator)

        /*other methods*/
        .def("is_valid", &ON_Layer::IsValid, nb::arg("text_log") = nullptr)

        .def("get_name", &ON_Layer::Name)

        .def("set_name", &LayerUtilities::SetName)

        .def("unset_persistent_locking", &ON_Layer::UnsetPersistentLocking)

        .def("unset_persistent_visibility", &ON_Layer::UnsetPersistentVisibility)
    ;
}
