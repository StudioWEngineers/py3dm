.. _why:

Why another binding library for openNURBS?
==========================================

The official Python bindings for openNURBS are provided by McNeel in the
`rhino3dm <https://github.com/mcneel/rhino3dm>`_ package. This is an open-source, large
project which provides bindings for most, if not all, openNURBS classes, and also supports
multiple programming languages. These capabilities come with a trade-off: increased complexity
of both the source code and the accompanying documentation.

At the time of writing (November 2025), the Python bindings's documentation and type hints
provided with rhino3dm do not fully reflect the actual implementation of the source code.
As a result, using the package is challenging, and understanding its behavior is time-consuming.
Several pull requests have been submitted and merged to improve the state of the type hints,
but substantial gaps remain; see the rhino3dm `changelog <https://github.com/mcneel/rhino3dm/blob/dev/CHANGELOG.md>`_
for ongoing updates.

Another notable limitation, which stems from the library's general architecture, is that
objects retrieved from or added to an openNURBS model cannot be further modified. For example, see issue
`#695 <https://github.com/mcneel/rhino3dm/issues/695>`_ and the discussion in
`#649 <https://github.com/mcneel/rhino3dm/pull/649#issuecomment-2457124992>`_.
This behavior likely arises because rhino3dm does not provide direct Python bindings for openNURBS classes.
Instead, it introduces an intermediate C++ layer that acts as a wrapper between the Python API and
the underlying C++ implementation of openNURBS.
This design choice allows rhino3dm to maintain a single core C++ codebase for multiple programming languages
while handling memory management, type conversions, and platform-specific differences in a controlled manner.
While this architecture has clear advantages in terms of cross-language support and code reuse,
it also introduces limitations for developers. In particular, the immutability of
retrieved objects and the abstraction introduced by the intermediate layer obscure the
original API semantics, complicate debugging, and restrict openNURBS object modifications.
In our view, these represent significant constraints on the usability of the library.

So what is different?
---------------------

py3dm is a lightweight Python library that provides direct bindings to openNURBS classes.
Its primary goal is to offer straightforward access to the core functionality of openNURBS,
without the additional abstraction layers present in larger projects like rhino3dm.
While py3dm does not aim for the same level of coverage or completeness as rhino3dm,
it emphasizes transparency, minimal overhead, and direct interaction with the underlying C++ objects.

Where possible, direct bindings are exposed to Python, allowing users to manipulate
openNURBS objects natively. To improve usability, a small number of helper classes have
been defined to facilitate common operations on 3dm models and their components, without
obscuring the underlying API.

py3dm provides comprehensive type hints for all classes and methods, enabling better
integration with IDEs and static type checkers like mypy or Pylance. In addition, extensive
test suites are included to ensure correctness and coverage of the bindings, helping users verify that
the library behaves consistently with the original openNURBS implementation.

Overall, py3dm is designed for developers who need direct, efficient access to openNURBS
functionality in Python, while avoiding the additional complexity introduced by wrapper
layers or multi-language support in larger binding libraries.

Exclusive pointers
^^^^^^^^^^^^^^^^^^

In order to modify a generic openNURBS object, an exclusive pointer to the target object is
required. As example, from the ON_ModelGeometryComponent class:

.. code-block:: cpp

    /*
    Description:
        Get a pointer to geometry that can be used to modify the geometry.
        The returned pointer is not shared at the time it is returned
        and will not be shared until a copy of this ON_ModelGeometryComponent
        is created.
    Returns:
        If this ON_ModelGeometryComponent is the only reference to the geometry,
        then a pointer to the geometry is returned.
        Otherwise, nullptr is returned.
    See Also:
        ON_ModelGeometryComponent::Attributes()
        ON_ModelGeometryComponent::Geometry()
        ON_ModelGeometryComponent::ExclusiveAttributes()
        ON_ModelGeometryComponent::ExclusiveGeometry();
        ON_ModelComponentRef::ExclusiveModelComponent();
        ONX_Model::ComponentFromRuntimeSerialNumber()
    */
    class ON_Geometry* ExclusiveGeometry() const;


py3dm does not make use of such API when retrieving objects from openNURBS because it would
make impossible an operation like this:

.. code-block:: py

    from py3dm import Model, Point3d

    model = Model()
    model.ObjectTable.add_point(Point3d(0, 0, 0))

    for obj in model.ObjectTable:
        obj.x = 1.0 # this is not possible because ExclusiveGeometry() return nullptr
