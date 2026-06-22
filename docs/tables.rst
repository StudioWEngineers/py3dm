.. _tables:

Tables
======

Objects can be added, deleted, and retrieved from a ``Model`` through tables.

The primary purpose of tables is to provide convenient access to specific
subsets of objects (such as Layers, LineCurves, Meshes, Points, ...). This is
particularly useful when working with existing models, as it eliminates the
need to inspect the type of every retrieved object.

Separate tables do not correspond to separate storage mechanisms in openNURBS.
They exist solely as a convenience layer that provides a cleaner and more
intuitive API.

All tables implement the following common API:

* iterator support
* ``add`` method
* ``count`` method
* ``delete`` method
* ``get`` method
* ``get_exclusive`` method

The difference between the ``get`` and ``get_exclusive`` methods is that the
former returns a read-only view of the underlying object, whereas the latter
returns a modifiable object.
Refer also to chapter :ref:`access_existing_model`.

.. _layer_table:

LayerTable
----------

The ``LayerTable`` class provides an interface to objects of type
``ON_ModelComponent::Type::Layer``.

Although these objects are typically accessed by ``ON_UUID`` (or ``index``),
like other model objects, this table provides additional abstractions that
allow layers to be accessed by their full name using the format
``parent::leaf``.

Note that deleting the last layer and then adding a new one does not guarantee
that layer ordering will be preserved.

.. _line_curve_table:

LineCurveTable
--------------

The ``LineCurveTable`` class provides methods to manage ``ON_LineCurve``
objects.

.. _mesh_table:

MeshTable
---------

The ``MeshTable`` class provides methods to manage ``ON_Mesh`` objects.

.. _point_table:

PointTable
----------

The ``PointTable`` class provides methods to manage ``ON_Point`` objects.
