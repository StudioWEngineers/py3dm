Introduction
============

Welcome to py3dm v|release| documentation!

*py3dm* is a small binding library that exposes openNURBS classes to Python. It is
reminiscent of `rhino3dm <https://github.com/mcneel/rhino3dm>`__ and uses very similar
syntax.

.. only:: not latex

   Documentation formats
   ---------------------

   You are reading the HTML version of the documentation. An alternative `PDF
   version <https://py3dm.readthedocs.io/_/downloads/en/latest/pdf/>`__ is
   also available.

   Dependencies
   ------------

.. only:: latex

   .. rubric:: Dependencies

*py3dm* depends on

- `nanobind <https://github.com/wjakob/nanobind>`__.
- `openNURBS <https://github.com/mcneel/opennurbs>`__.
- `google draco <https://github.com/google/draco>`__.

.. only:: not latex

   How to cite this project?
   -------------------------

.. only:: latex

   .. rubric:: How to cite this project?

Please use the following BibTeX template to cite *py3dm* in scientific
discourse:

.. code-block:: bibtex

    @misc{py3dm,
       author = {StudioWEngineers},
       year = {2025},
       note = {https://github.com/StudioWEngineers/py3dm},
       title = {py3dm: Python bindings for openNURBS using nanobind}
    }

.. only:: not latex

   Table of contents
   -----------------

.. toctree::
   :maxdepth: 1

   changelog
   why
   faq

.. toctree::
   :caption: API Reference
   :maxdepth: 1

   api
