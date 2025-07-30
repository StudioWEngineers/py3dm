cmake_minimum_required(VERSION 3.30)
project(py3dm)

set (CMAKE_CXX_STANDARD 17)
set(CMAKE_POSITION_INDEPENDENT_CODE ON)

set(DEV_MODULE Development.Module)
find_package(Python 3.8 COMPONENTS Interpreter ${DEV_MODULE} REQUIRED)
add_subdirectory(lib/nanobind)

# Source files
file(GLOB_RECURSE bindings_SRC "src/*.h" "src/*.cpp")
file(GLOB zlib_SRC "lib/opennurbs/zlib/*.h" "lib/opennurbs/zlib/*.c")
file(GLOB opennurbs_SRC "lib/opennurbs/*.h" "lib/opennurbs/*.cpp")

# Remove unused OpenNURBS files
list(REMOVE_ITEM opennurbs_SRC
    "${CMAKE_CURRENT_SOURCE_DIR}/lib/opennurbs/opennurbs_gl.cpp"
    "${CMAKE_CURRENT_SOURCE_DIR}/lib/opennurbs/opennurbs_precompiledheader.cpp"
    "${CMAKE_CURRENT_SOURCE_DIR}/lib/opennurbs/opennurbs_unicode_cp932.cpp"
    "${CMAKE_CURRENT_SOURCE_DIR}/lib/opennurbs/opennurbs_unicode_cp949.cpp"
)

# Compiler flags / definitions
add_definitions(
    -D_GNU_SOURCE
    -DON_COMPILING_OPENNURBS
    -DOPENNURBS_FREETYPE_INC_
    -DMY_ZCALLOC
    -DZ_PREFIX
    -DOPENNURBS_ZLIB_LIB_DIR
    -DUNICODE
    -DON_INCLUDE_DRACO
)
#if(UNIX AND NOT APPLE)
#   add_definitions(
#        -DON_RUNTIME_LINUX -> this seems to be required in font.cpp and other cpp
#   )
#endif()

# Static libraries
add_library(zlib_static STATIC ${zlib_SRC})
add_library(opennurbs_static STATIC ${opennurbs_SRC})
add_subdirectory(lib/draco)

# Main Python extension module
nanobind_build_library(nanobind)
if(UNIX AND NOT APPLE)
    nanobind_add_module(_py3dm NB_STATIC ${bindings_SRC} ${zlib_SRC})
else()
    nanobind_add_module(_py3dm NB_STATIC ${bindings_SRC})
endif()
target_link_libraries(_py3dm PRIVATE nanobind-static)

target_include_directories(_py3dm PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}/lib/opennurbs
    ${CMAKE_CURRENT_SOURCE_DIR}/lib/draco/src
    ${CMAKE_BINARY_DIR}
)

# Link additional libraries
target_link_libraries(_py3dm PRIVATE
    zlib_static
    opennurbs_static
    draco::draco
)

# Link shlwapi on Windows
if(WIN32)
    target_link_libraries(_py3dm PRIVATE shlwapi)
endif()

# Link libuuid on Linux
if(UNIX AND NOT APPLE)
    find_library(UUID_LIB uuid REQUIRED)
    target_link_libraries(_py3dm PRIVATE ${UUID_LIB})
endif()

# Python package installation
install(FILES
    ${CMAKE_SOURCE_DIR}/src/__init__.py
    ${CMAKE_SOURCE_DIR}/src/__init__.pyi
    ${CMAKE_SOURCE_DIR}/src/py.typed
    DESTINATION py3dm
)

install(TARGETS _py3dm
    LIBRARY DESTINATION py3dm
    RUNTIME DESTINATION py3dm
    ARCHIVE DESTINATION py3dm
)
