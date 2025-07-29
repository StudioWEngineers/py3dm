#pragma once

// System includes

// External includes
#include <nanobind/nanobind.h>
#include <nanobind/stl/string.h>
#include <nanobind/stl/wstring.h>
#include <nanobind/stl/tuple.h>

// Project includes
#include "../opennurbs_includes.h"

#define PY3DM_VERSION_MAJOR 0
#define PY3DM_VERSION_MINOR 2
#define PY3DM_VERSION_PATCH 0
#define PY3DM_VERSION_DEV   1 // A value > 0 indicates a development release

namespace nb = nanobind;
