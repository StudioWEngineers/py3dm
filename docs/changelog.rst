.. _changelog:

Changelog
#########

*py3dm* uses a `semantic versioning <http://semver.org>`__ policy for its API.

Version 0.2.0 (T.B.A.)
----------------------

- Added bindings for ``ON_ModelComponent`` and derived ``ON_Layer`` bindings from it.
- Added tests for PyPy.
- Added workflow for build and publish wheels (ubuntu, macos and windows)
- ``LayerTable.add()`` now returns the ``layer_uuid`` instead of the assigned index.
- fix ``LayerTable`` return type for get methods (refer to #11)
- tables member variables are now snake_case (refer to #11)

Version 0.1.0 (July 29, 2025)
-----------------------------

- Initial release of the py3dm codebase.