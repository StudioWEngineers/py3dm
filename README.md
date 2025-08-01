# py3dm
[![Tests](https://github.com/StudioWEngineers/py3dm/actions/workflows/workflow_ci.yml/badge.svg)](https://github.com/StudioWEngineers/py3dm/actions/workflows/workflow_ci.yml)
[![PyPI](https://github.com/StudioWEngineers/py3dm/actions/workflows/build_and_publish.yml/badge.svg)](https://github.com/StudioWEngineers/py3dm/actions/workflows/build_and_publish.yml)
[![Documentation Status](https://readthedocs.org/projects/py3dm/badge/?version=latest)](https://py3dm.readthedocs.io/en/latest/?badge=latest)
[![GitHub Release](https://img.shields.io/github/v/release/StudioWEngineers/py3dm)](https://github.com/StudioWEngineers/py3dm/releases)


Python bindings for **OpenNURBS** using **nanobind**.

## Dependencies

- openNURBS commit `76f86d7e68341f3c80be8fcf50f3312c112072bd` (PR #107 - version: `v8.18.25098.11001`) [OpenNURBS](https://github.com/mcneel/opennurbs/pull/107)
- draco commit `4e12ab27d0fe690cf98e96dc33c2bd52e1485163` [google-draco](https://github.com/google/draco)
- nanobind `2.7.0` [nanobind](https://github.com/wjakob/nanobind)

## Documentation

Please see the following links for reference documentation (currently a BIG WIP) in 
[HTML](https://py3dm.readthedocs.io/en/latest/) and
[PDF](https://py3dm.readthedocs.io/_/downloads/en/latest/pdf/) formats.

## License and attribution

All material in this repository is licensed under a three-clause [BSD
license](LICENSE).

Please use the following BibTeX template to cite py3dm in scientific
discourse:

```bibtex
@misc{py3dm,
   author = {Studio W Engineers},
   year = {2025},
   note = {https://github.com/StudioWEngineers/py3dm},
   title = {py3dm: Python bindings for openNURBS using nanobind}
}
```
