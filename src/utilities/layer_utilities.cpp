// System includes
#include <codecvt>
#include <locale>
#include <sstream>

// External includes

// Project includes
#include "layer_utilities.h"


namespace LayerUtilities {

bool SetName(ON_Layer& layer, const ON_wString& name) {
    return layer.SetName(name);
}

std::string ToString(const ON_Layer& layer) {
    std::wstring_convert<std::codecvt_utf8<wchar_t>> convert;
    std::string name_str = convert.to_bytes(layer.NameAsPointer());
    std::string path_separator = convert.to_bytes(ON_ModelComponent::NamePathSeparator);

    char p_uuid_str[37];
    char uuid_str[37];
    ON_UuidToString(layer.ParentId(), p_uuid_str);
    ON_UuidToString(layer.Id(), uuid_str);

    ON_Color color = layer.Color();
    std::ostringstream color_stream;
    color_stream << "(" << color.Red() << ", " << color.Green() << ", " << color.Blue() << ", " << 255 - color.Alpha() << ")";

    ON_Color p_color = layer.PlotColor();
    std::ostringstream p_color_stream;
    p_color_stream << "(" << p_color.Red() << ", " << p_color.Green() << ", " << p_color.Blue() << ", " << 255 - p_color.Alpha() << ")";

    std::ostringstream output;
    output << "Layer with properties:\n"
           << "\tcolor = " << color_stream.str() << "\n"
           << "\tiges_level = " << layer.IgesLevel() << "\n"
           << "\tindex = " << layer.Index() << "\n"
           << "\tis_expanded = " << std::boolalpha << layer.m_bExpanded << "\n"
           << "\tis_locked = " << layer.IsLocked() << "\n"
           << "\tis_visible = " << layer.IsVisible() << "\n"
           << "\tlayer_uuid = " << std::string(uuid_str) << "\n"
           << "\tline_type_index = " << layer.LinetypeIndex() << "\n"
           << "\tname = '" << name_str << "'\n"
           << "\tparent_uuid = " << std::string(p_uuid_str) << "\n"
           << "\tpath separator = " << path_separator << "\n"
           << "\tpersistent_locking = " << layer.PersistentLocking() << "\n"
           << "\tpersistent_visibility = " << layer.PersistentVisibility() << "\n"
           << "\tplot_color = " << p_color_stream.str() << "\n"
           << "\tplot_weight = " << layer.PlotWeight() << "\n"
           << "\trender_material_index = " << layer.RenderMaterialIndex() << "\n";
    return output.str();
}

} // namespace LayerUtilities
