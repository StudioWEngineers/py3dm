// System includes

// External includes

// Project includes
#include "casters/uuid_caster.h"
#include "model_component_bindings.h"


void ModelComponentBindings(nb::module_& m) {
    nb::class_<ON_ModelComponent, ON_Object>(m, "ModelComponent")
        /*magic methods*/
        .def(nb::init<>())

        /*other methods*/
        .def("get_index", nb::overload_cast<>(&ON_ModelComponent::Index, nb::const_))
        .def("get_index", nb::overload_cast<int>(&ON_ModelComponent::Index, nb::const_))
        .def("get_uuid", &ON_ModelComponent::Id)
        .def("parent_uuid_is_not_null", &ON_ModelComponent::ParentIdIsNotNil)
        .def("parent_uuid_is_null", &ON_ModelComponent::ParentIdIsNil)
        .def("set_uuid", nb::overload_cast<const ON_UUID&>(&ON_ModelComponent::SetId))
        .def("set_uuid", nb::overload_cast<>(&ON_ModelComponent::SetId))
        .def("uuid_is_not_null", &ON_ModelComponent::IdIsNotNil)
        .def("uuid_is_null", &ON_ModelComponent::IdIsNil)
    ;
}
