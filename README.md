# py3dm
[![Continuous Integration](https://img.shields.io/github/actions/workflow/status/StudioWEngineers/py3dm/workflow_ci.yml?label=tests)](https://github.com/StudioWEngineers/py3dm/actions/workflows/workflow_ci.yml) 
[![PyPI Publish](https://img.shields.io/github/actions/workflow/status/StudioWEngineers/py3dm/build_and_publish.yml?label=publish)](https://github.com/StudioWEngineers/py3dm/actions/workflows/build_and_publish.yml)
[![Documentation](https://img.shields.io/readthedocs/py3dm/latest)](https://py3dm.readthedocs.io/en/latest/)
[![](https://img.shields.io/pypi/v/py3dm.svg?color=brightgreen)](https://pypi.org/pypi/py3dm/)
![](https://img.shields.io/pypi/l/py3dm.svg?color=brightgreen)
[![](https://img.shields.io/badge/Changelog-Link-brightgreen)](https://py3dm.readthedocs.io/en/latest/changelog.html)


The Studio W Python bindings for *OpenNURBS* using *nanobind*.

> [!IMPORTANT]  
> **OpenNURBS and Rhinoceros are registered trademarks of Robert McNeel & Associates.**
>
> *py3dm* is an independent, open-source project not affiliated with, endorsed by, or vetted by Robert McNeel & Associates. It provides Python bindings that utilize the publicly available OpenNURBS APIs. *py3dm* is distributed under the BSD 3-Clause License. Users should refer to the OpenNURBS [Terms of Use](https://www.rhino3d.com/features/developer/opennurbs/) for further details.
>

## Dependencies

- [OpenNURBS](https://github.com/mcneel/opennurbs/) commit `d38986464ebfa2dad4e572cf1c0915896d75109b` (`v8.24.25281.15001`) 
- [google-draco](https://github.com/google/draco) `3abbc66fdf5597b1560c44ce7840aac76900b3f7` (`1.3.0-291-g3abbc66`) 
- [nanobind](https://github.com/wjakob/nanobind) commit `d145ec5a41cf2d47eed7a8d7e366c92d2b0ac5b4` (`v2.9.2-30-gd145ec5`) 

## Documentation

Reference documentation is available in [HTML](https://py3dm.readthedocs.io/en/latest/) format.

## License and attribution

All material in this repository is licensed under a three-clause [BSD
license](LICENSE).

Please use the following BibTeX template to cite *py3dm*:

```bibtex
@misc{py3dm,
   author = {Studio W Engineers},
   title = {py3dm: Python bindings for openNURBS using nanobind},
   year = {2025},
   url = {https://github.com/StudioWEngineers/py3dm},
}
```
