#include "casters/color_caster.h"
#include "casters/on_wstring_caster.h"
#include "object_attributes_bindings.h"


void ObjectAttributesBindings(nb::module_& m) {
    nb::class_<ON_3dmObjectAttributes, ON_Object>(m, "ObjectAttributes")
        /*magic methods*/
        .def(nb::init<>())
        .def("__eq__", [] (const ON_3dmObjectAttributes& self, const ON_3dmObjectAttributes& other) {
            return self == other;
            }
        )
        .def("__ne__", [] (const ON_3dmObjectAttributes& self, const ON_3dmObjectAttributes& other) {
            return self != other;
            }
        )

        /*read-write properties*/
        .def_prop_rw("color_source", &ON_3dmObjectAttributes::ColorSource, &ON_3dmObjectAttributes::SetColorSource)
        .def_prop_rw("is_visible", &ON_3dmObjectAttributes::IsVisible, &ON_3dmObjectAttributes::SetVisible)
        .def_prop_rw("mode", &ON_3dmObjectAttributes::Mode, &ON_3dmObjectAttributes::SetMode)
        .def_prop_rw("plot_color_source", &ON_3dmObjectAttributes::PlotColorSource, &ON_3dmObjectAttributes::SetPlotColorSource)

        /*read-write member variables*/
        .def_rw("color", &ON_3dmObjectAttributes::m_color)
        .def_rw("layer_index", &ON_3dmObjectAttributes::m_layer_index)
        .def_rw("line_type_index", &ON_3dmObjectAttributes::m_linetype_index)
        .def_rw("material_index", &ON_3dmObjectAttributes::m_material_index)
        .def_rw("plot_color", &ON_3dmObjectAttributes::m_plot_color)

        /*other methods*/
        .def("default", &ON_3dmObjectAttributes::Default)
        .def("get_name", &ON_3dmObjectAttributes::Name)
        .def("set_name", &ON_3dmObjectAttributes::SetName, nb::arg("name"), nb::arg("fix_invalid_name") = false)
    ;
}
