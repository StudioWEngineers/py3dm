.. _installation:

Installation
============

*py3dm* can be installed either via *pip* (from PyPI or a wheel) or built locally from
source.

Prerequisites:

- Python 3.12 or newer
- pip (Python package manager)

Installing via pip
------------------

The simplest way to install *py3dm* is using pip:

.. code-block:: bash

    pip install py3dm

This command downloads the latest release from PyPI and installs all required dependencies
automatically.

Local build from source
-----------------------

For access to the latest development version or modifications to the source, a local build
can be performed.

Additional prerequisites for local build:

- CMake 3.30 or newer
- A C++17 compatible compiler (refer to `OpenNURBS supported compilers <https://developer.rhino3d.com/guides/opennurbs/getting-started/>`__ )
- Git

Steps:

1. Clone the repository and initialize submodules

.. code-block:: bash

    git clone https://github.com/StudioWEngineers/py3dm.git
    git submodule update --init --recursive
    cd py3dm

2. Install the Python package in editable mode

.. code-block:: bash

    pip install -e .

This installation method compiles C++ extensions automatically and links the package in
editable mode, so modifications to Python or C++ source files are reflected after
reinstallation.

Verification
------------

Installation can be verified by importing the package and printing its version:

.. code-block:: python

    import py3dm
    print(py3dm.__version__)
