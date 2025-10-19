// System includes

// External includes

// Project includes
#include "bindings.h"
#include "enumerators_bindings.h"
#include "geometry_bindings.h"
#include "layer_bindings.h"
#include "layer_table_bindings.h"
#include "line_bindings.h"
#include "line_curve_bindings.h"
#include "model_bindings.h"
#include "model_component_bindings.h"
#include "object_attributes_bindings.h"
#include "object_bindings.h"
#include "object_table_bindings.h"
#include "point_geometry_bindings.h"
#include "point3d_bindings.h"
#include "text_log_bindings.h"


NB_MODULE(_py3dm, m) {
    m.attr("__author__") = "StudioWEngineers";
    m.attr("__email__") = "studio.w.engineers@gmail.com";
    m.attr("__maintainer__") = "StudioWEngineers";
    m.doc() = "Python bindings for openNURBS using nanobind.";

    ON::Begin();
    EnumeratorsBindings(m);
    ObjectBindings(m);

    ObjectAttributesBindings(m);
    ModelComponentBindings(m);
    Point3dBindings(m);
    LineBindings(m);

    GeometryBindings(m);
    LayerBindings(m);
    LayerTableBindings(m);
    LineCurveBindings(m);
    ModelBindings(m);
    PointGeometryBindings(m);
    TextLogBindings(m);

    ObjectTableBindings(m);
}
