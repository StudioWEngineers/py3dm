Introduction
============

This is the py3dm 0.2.0-dev1 documentation.

*py3dm* is a small binding library that exposes openNURBS classes to Python.
It is reminiscent of `rhino3dm <https://github.com/mcneel/rhino3dm>`__ and uses very
similar syntax.

.. important::

    **OpenNURBS and Rhinoceros are registered trademarks of Robert McNeel & Associates.**

    *py3dm* is an independent, open-source project not affiliated with, endorsed by, or
    vetted by Robert McNeel & Associates. It provides Python bindings that utilize the
    publicly available OpenNURBS APIs. Users should refer to the OpenNURBS
    `Terms of Use <https://www.rhino3d.com/features/developer/opennurbs/>`__ for further
    details.

How to cite this project?
-------------------------

Please use the following BibTeX template to cite *py3dm*:

.. code-block:: bibtex

    @misc{py3dm,
        author = {StudioWEngineers},
        title = {py3dm: Python bindings for openNURBS using nanobind},
        year = {2025},
        url = {https://github.com/StudioWEngineers/py3dm}
    }

Disclaimer
----------

*py3dm* is an open-source set of bindings that benefits from the collaboration
of many contributors. While efforts have been made to ensure the implementation is
correct, it remains the user's responsibility to verify and accept the results.

Please refer to the `license <https://github.com/StudioWEngineers/py3dm/blob/main/LICENSE>`__
for the terms and conditions of use.

.. toctree::
    :maxdepth: 1
    :hidden:

    changelog
    why
    faq

.. toctree::
    :caption: Basics
    :hidden:

    installation
    tables

.. toctree::
    :caption: API Reference
    :maxdepth: 1
    :hidden:

    autoapi/py3dm/index