.. _tables:

Tables
======

Objects can be added, deleted and retrieved from a ``Model`` using tables.

All tables implement an iterator, add and getter methods and they allow working on small
subsets of objects (Curves, Points, ...). All the tables that refer to geometrical objects
are an interface to the same container via ``ON_ModelComponent::Type::ModelGeometry``.

.. _layer_table:

LayerTable
----------

The ``LayerTable`` class provides interface to objects of type
``ON_ModelComponent::Type::Layer``.

Despite these objects are supposed to be accessed (and actually are) by ``ON_UUID`` (or
``index``) like any other objects in `Model`, this table provides abstractions to enable
access to Layers via full name, i.e., using the format ``parent::leaf``.

It is highlighted that deleting the last Layer in the table and adding a new one does
not guarantee nor preserve the order of the Layers in the table in case of deletions and
additions.

.. _curve_table:

CurveTable
----------

The ``CurveTable`` class provides methods to add .

.. _point_table:

PointTable
----------

The ``PointTable`` class provides methods to access and modify existing ``ON_Point`` s as
well as add new ones.

