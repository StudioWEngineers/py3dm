.. _access_existing_model:

Access existing models
======================

On the C++ side, openNURBS provides openNURBS provides two categories of accessors from an existing ``ONX_Model``,
depending on whether the user needs to modify the retrieved object or not:

* ``const`` getters:

  - ``const ON_ModelComponent* ON_ModelComponentReference::ModelComponent()``
  - ``const ON_3dmObjectAttributes* ON_ModelGeometryComponent::Attributes()``
  - ``const ON_Geometry* ON_ModelGeometryComponent::Geometry()``

* non-``const`` getters:

  - ``ON_ModelComponent* ON_ModelComponentReference::ExclusiveModelComponent()``
  - ``ON_3dmObjectAttributes* ON_ModelGeometryComponent::ExclusiveAttributes()``
  - ``ON_Geometry* ON_ModelGeometryComponent::ExclusiveGeometry()``

Neither nanobind nor Python has a notion of ``const``-ness. As a result,
objects retrieved from ``ONX_Model`` through ``const`` accessors could still be
modified if exposed directly to Python.

To prevent this, ``get`` methods return a read-only *view* of the original
object. These views allow inspection of the underlying object while preventing
modifications. View objects are lightweight wrappers around the underlying
openNURBS classes.

Objects returned by table ``get_exclusive`` methods are modifiable because they
are obtained through the corresponding non-``const`` openNURBS accessors. This
distinction mirrors the ownership model used internally by openNURBS, where
mutable access is granted only when the object is not shared.
