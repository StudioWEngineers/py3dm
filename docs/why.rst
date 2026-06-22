.. _why:

Why another binding library?
============================

The official Python bindings for openNURBS are provided by McNeel in the
`rhino3dm <https://github.com/mcneel/rhino3dm>`_ package, an
open-source, large project which provides bindings for most, if not all,
openNURBS classes. It also supports multiple programming languages. These
capabilities come with a trade-off: increased complexity of both the source
code and the accompanying documentation.

However, at the time of writing (November 2025), the documentation and type
hints do not always accurately reflect the implementation, making the API
difficult to discover and use effectively. While several improvements have been
merged, significant gaps remain; as example refer to this forum
`thread <https://discourse.mcneel.com/t/file3dm-boundingbox-accuracy/219801>`_.

A more fundamental limitation is that objects retrieved from or added to a
model cannot be modified in place. Among many others, see discussions in
`#695 <https://github.com/mcneel/rhino3dm/issues/695>`_ and in
`#649 <https://github.com/mcneel/rhino3dm/pull/649#issuecomment-2457124992>`_.

So what is different?
---------------------

*py3dm* is a lightweight Python library that provides direct bindings to
openNURBS classes. Its primary goal is to offer access to the core
functionalities of openNURBS, without the additional abstraction layers present
in rhino3dm. While *py3dm* does not aim for the same level of coverage or
completeness as rhino3dm, it emphasizes transparency, minimal overhead, and
direct interaction with the underlying C++ objects.

Where possible, direct bindings are exposed to Python, allowing users to
manipulate openNURBS objects natively. To improve usability, a small number of
helper classes (:ref:`tables`) have been defined to facilitate common
operations on 3dm models and their components, without obscuring the underlying
API.

*py3dm* provides comprehensive type hints for all classes and methods, enabling
better integration with IDEs and static type checkers like mypy or Pylance. In
addition, test suites are included to ensure correctness and coverage of the
bindings.

Very little of openNURBS is wrapped so far, but this library is being developed
in a way that should make it as easy as possible to wrap more functionality as
necessary. If you find that a function that you would like to use is not yet
wrapped, please create a discussion or feel free to wrap it on your own and
submit a pull request.
