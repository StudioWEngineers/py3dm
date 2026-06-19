// System includes

// External includes

// Project includes
#include "../layer_table.h"
#include "casters/on_wstring_caster.h"
#include "casters/uuid_caster.h"


void LayerTableBindings(nb::module_& m) {
    nb::class_<LayerTable::Iterator>(m, "__LayerTableIterator")
        .def("__iter__", [](LayerTable::Iterator &it) -> LayerTable::Iterator& {
            return it;
        })
        .def("__next__", [](LayerTable::Iterator &it) -> LayerView* {
            while (!it.IsOver()) {
                LayerView* layer = *it;
                ++it;

                if (layer != nullptr) {
                    return layer;
                }
            }
            throw nb::stop_iteration();
            }, nb::rv_policy::reference_internal)
    ;

    nb::class_<LayerTable>(m, "LayerTable")
        /*magic methods*/
        .def("__getitem__", nb::overload_cast<int>(&LayerTable::Get, nb::const_), nb::rv_policy::reference_internal)
        .def("__iter__", [](LayerTable& self) {return self.Begin();}, nb::keep_alive<0, 1>())
        .def("__len__", &LayerTable::Count)

        /*deleters*/
        .def("delete", nb::overload_cast<const ON_wString>(&LayerTable::Delete, nb::const_))
        .def("delete", nb::overload_cast<const ON_UUID>(&LayerTable::Delete, nb::const_))

        /*getters*/
        .def("get", nb::overload_cast<int>(&LayerTable::Get, nb::const_), nb::rv_policy::reference_internal)
        .def("get", nb::overload_cast<ON_wString>(&LayerTable::Get, nb::const_), nb::rv_policy::reference_internal)
        .def("get", nb::overload_cast<const ON_UUID>(&LayerTable::Get, nb::const_), nb::rv_policy::reference_internal)
        .def("get_exclusive", &LayerTable::GetExclusive, nb::rv_policy::reference_internal)

        /*other methods*/
        .def("add", &LayerTable::Add)
        .def("count", &LayerTable::Count)
        .def("get_index", &LayerTable::GetIndex)
        .def("get_uuid", &LayerTable::GetUUID)
        .def("has", &LayerTable::Has)
        .def("max_index", &LayerTable::MaxIndex)
    ;
}
