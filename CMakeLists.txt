cmake_minimum_required(VERSION 3.30)
project(py3dm)

set (CMAKE_CXX_STANDARD 17)
set(CMAKE_POSITION_INDEPENDENT_CODE ON)

set(DEV_MODULE Development.Module)
find_package(Python 3.8 COMPONENTS Interpreter ${DEV_MODULE} REQUIRED)
add_subdirectory(lib/nanobind)

# Source files
file(GLOB_RECURSE bindings_source "src/*.h" "src/*.cpp")
file(GLOB zlib_source "lib/opennurbs/zlib/*.h" "lib/opennurbs/zlib/*.c")
file(GLOB opennurbs_source "lib/opennurbs/*.h" "lib/opennurbs/*.cpp")

# Remove unused OpenNURBS files
list(REMOVE_ITEM opennurbs_source
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
)
#if(UNIX AND NOT APPLE)
#   add_definitions(
#        -DON_RUNTIME_LINUX -> this seems to be required in font.cpp and other cpp
#   )
#endif()

# Static libraries
add_library(opennurbs_static STATIC ${opennurbs_source})

# Main Python extension module
nanobind_build_library(nanobind)
nanobind_add_module(_py3dm NB_STATIC ${bindings_source} ${zlib_source})

option(INCLUDE_DRACO "Enable google draco mesh compression support" OFF)
if(INCLUDE_DRACO)
    add_definitions(-DON_INCLUDE_DRACO)
    add_subdirectory(lib/draco)
    target_include_directories(_py3dm PRIVATE
        ${CMAKE_CURRENT_SOURCE_DIR}/lib/draco/src
    )
    target_link_libraries(_py3dm PRIVATE
        draco::draco
    )
endif()

target_include_directories(_py3dm PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}/lib/opennurbs
    ${CMAKE_BINARY_DIR}
)

# Link additional libraries
target_link_libraries(_py3dm PRIVATE
    opennurbs_static
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
install(DIRECTORY ${CMAKE_SOURCE_DIR}/py3dm DESTINATION .)
install(TARGETS _py3dm
    LIBRARY DESTINATION py3dm
    RUNTIME DESTINATION py3dm
    ARCHIVE DESTINATION py3dm
)
