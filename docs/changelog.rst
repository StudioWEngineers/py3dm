.. _changelog:

Changelog
#########

*py3dm* uses a `semantic versioning <http://semver.org>`__ policy for its API.

Version 0.2.0 (T.B.A.)
-----------------------------

- Added bindings for ``ON_3dVector``.
- Added bindings for ``ON_3dPoint::operator+=``.


Version 0.1.1 (June 22, 2026)
-----------------------------

Dummy release due to an error in uploading to PyPI.

Version 0.1.0 (June 22, 2026)
-----------------------------

Initial release of the py3dm codebase:

- Added bindings for ``ON_ModelComponent`` and derived ``ON_Layer`` bindings from it.
- Added tests for PyPy.
- Added workflow for build and publish wheels (ubuntu, macos and windows)
- ``LayerTable.add()`` now returns the ``layer_uuid`` instead of the assigned index.
- ix ``LayerTable`` return type for get methods (refer to #11)
- tables member variables are now snake_case (refer to #11)
- Added bindings for ``ON_Mesh`` (refer to PR `#20 <https://github.com/StudioWEngineers/py3dm/pull/20>`__)
- ``CurveTable`` has been renamed ``LineCurveTable`` narrowing down its scope (commit `5172f1e <https://github.com/StudioWEngineers/py3dm/commit/5172f1e9b984073dbd1fbfc48e07e74faf5eb13b>`__)