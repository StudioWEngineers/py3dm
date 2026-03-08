.. _modify_existing_model:

Modify existing models
======================

*py3dm* can be used to read, write, and modify ``.3dm`` files.

Due to the current lightweight implementation of the library, special care is
required when modifying objects that have already been added to a ``Model``.

Retrieve geometrical objects
----------------------------
There are two ways to retrieve objects from an existing ``Model``, which mirror
the underlying openNURBS C++ API:

- ``get_by_uuid``
- ``get_by_uuid_exclusive``

Both methods take only the object's ``ON_UUID`` as input. On the C++ side:

- ``get_by_uuid`` returns a ``const`` pointer to the geometry, which prevents
  modification in C++.
- ``get_by_uuid_exclusive`` returns a raw pointer to the geometry if, and only
  if, the retrieved ``ON_ModelGeometryComponent`` is the sole reference to that
  geometry. Otherwise, ``nullptr`` is returned.

Therefore, when retrieving an object with the explicit intent to modify it,
``get_by_uuid_exclusive`` should be used.

Modify geometrical objects
--------------------------

While the distinction between const and non-const access is enforced on the
C++ side, this constness is not preserved when the geometry is exposed to
Python.

As example, an ``ON_Point`` returned from a const getter is currently bound
as a regular mutable Python ``Point`` object. At the moment there is no simple
mechanism in *nanobind* to indicate that such a returned object should behave
purely as a read-only view. As a consequence, the following code runs
successfully, even though the original C++ API was designed to prevent
modification in this case:

.. code-block:: python

    import py3dm

    model = py3dm.Model()
    pt_uuid = model.point_table.add(0, 0, 0)
    pt = model.point_table.get_by_uuid(pt_uuid)
    pt.point.x = 1

    assert pt.point.x == 1  # pass

This behavior reflects the current implementation: const access in C++ does not
translate to a read-only object in Python.

A possible future improvement would be to introduce lightweight view types
around the original openNURBS classes and expose those views as read-only
objects on the Python side. This is not implemented yet.
