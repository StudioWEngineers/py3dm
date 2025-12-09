"""
py3dm
-----

Python bindings for ``OpenNURBS`` using ``nanobind``.

__author__: "StudioWEngineers"

__email__: "studio.w.engineers@gmail.com"
"""
# standard library imports
from enum import Enum
from typing import Iterator, overload
from uuid import UUID

# third party library imports

# local library specific imports


__author__: str
__doc__: str  # type: ignore[no-redef]
__email__: str
__maintainer__: str
__version__: str


class CurveTable:
    def __iter__(self) -> Iterator[LineCurve]: ...

    def __len__(self) -> int: ...

    @overload
    def add(self, start: Point3d, end: Point3d, attributes: None | ObjectAttributes = None) -> UUID:
        """Returns the ``UUID`` of the line in case of successful addition, or an empty
        ``UUID`` otherwise. If the line is in the model, then the ``UUID`` is unique for
        all components in the model and is locked.
        """
        ...

    @overload
    def add(self, line: Line, obj_attr: None | ObjectAttributes = None) -> UUID:
        """Returns the ``UUID`` of the line in case of successful addition, or an empty
        ``UUID`` otherwise. If the line is in the model, then the ``UUID`` is unique for
        all components in the model and is locked.
        """
        ...

    @overload
    def add(self, line: LineCurve, obj_attr: None | ObjectAttributes = None) -> UUID:
        """Returns the ``UUID`` of the line in case of successful addition, or an empty
        ``UUID`` otherwise. If the line is in the model, then the ``UUID`` is unique for
        all components in the model and is locked.
        """
        ...

    def count(self) -> int:
        """Returns the number of objects of type ``ON::curve_object`` in the model.
        """
        ...

    def get_by_uuid(self, object_uuid: UUID) -> LineCurve | None:
        """Returns the object with the given ``object_uuid`` or ``None`` if
        ``object_uuid`` is not found.
        """
        ...


class Geometry(OpenNURBSObject):
    """Python wrapper for the openNURBS ``ON_Geometry`` class.

        ``ON_Geometry``: base class for all geometry classes that must provide runtime
        class id. It provides interface for common geometric operations like finding
        bounding boxes and transforming.
    """
    def __init__(self) -> None: ...

    def dimension(self) -> int:
        """Returns the dimension of the object.

        Notes
        -----
        The dimension is typically three. For parameter space trimming curves the
        dimension is two. In rare cases the dimension can be one or greater than three.
        """
        ...

    def is_deformable(self) -> bool:
        """Returns ``True`` if object can be accurately modified with "squishy"
        transformations like projections, shears, an non-uniform scaling.
        """
        ...

    def is_valid(self, text_log: TextLog | None = None) -> bool:
        """The base implementation returns ``False``.
        """
        ...


class Layer(ModelComponent):
    """Python wrapper for the openNURBS ``ON_Layer`` class.
    """
    def __init__(self) -> None: ...
    def __repr__(self) -> str: ...

    @property
    def color(self) -> tuple[int, int, int, int]: ...
    @color.setter
    def color(self, color: tuple[int, int, int, int]) -> None: ...

    @property
    def full_path(self) -> str: ...

    @property
    def iges_level(self) -> int: ...
    @iges_level.setter
    def iges_level(self, level: int) -> None: ...

    @property
    def is_expanded(self) -> bool: ...
    @is_expanded.setter
    def is_expanded(self, is_expanded: bool) -> None: ...

    @property
    def is_locked(self) -> bool: ...
    @is_locked.setter
    def is_locked(self, is_locked: bool) -> None: ...

    def is_valid(self, text_log: TextLog | None = None) -> bool: ...

    @property
    def is_visible(self) -> bool: ...
    @is_visible.setter
    def is_visible(self, is_visible: bool) -> None: ...

    @property
    def layer_uuid(self) -> UUID: ...
    @layer_uuid.setter
    def layer_uuid(self, layer_uuid: UUID) -> None: ...

    @property
    def line_type_index(self) -> int: ...
    @line_type_index.setter
    def line_type_index(self, index: int) -> None: ...

    def get_name(self) -> str:
        """Returns the value of the name attribute.

        Notes
        -----
        If the component is in a model, then the name is unique among all components in
        the model. Names are formatted as reference : parent::leaf. For example in
        ``A.3dm : Z``, ``A.3dm`` is the reference and ``Z`` is the leaf. For a layer full
        path ``X::Y::Z``, ``X::Y`` is the parent and ``Z`` is the leaf. For most models,
        only the leaf is present in the name. The reference portion appears when a model
        component originates in a reference file (a linked instance definition with
        reference component names or a worksession reference). Components with a tree
        hierarchy, like layers, can have a parent and leaf.
        """
        ...

    def set_name(self, name: str) -> bool:
        """Returns ``True`` if the name attribute was changed to ``name`` or is already
        equal to ``name``; returns ``False`` and no changes are made if the name attribute
        is locked and ``name !=`` locked value or ``name`` is not empty and
        ``ON_ModelComponent::IsValidComponentName(name)`` is ``False``.

        Notes
        -----

        Leading and trailing non-zero unicode code points with values lower than equal
        ``ON_wString::Space`` are ignored.

        If ``name`` is the empty string, the ``name_is_state`` state will still be
        ``True``.
        """
        ...

    @property
    def path_separator(self) -> str: ...

    @property
    def parent_uuid(self) -> UUID: ...
    @parent_uuid.setter
    def parent_uuid(self, parent_uuid: UUID) -> None: ...

    @property
    def persistent_locking(self) -> bool: ...
    @persistent_locking.setter
    def persistent_locking(self, persistent_locking: bool) -> None: ...

    @property
    def persistent_visibility(self) -> bool: ...
    @persistent_visibility.setter
    def persistent_visibility(self, persistent_visibility: bool) -> None: ...

    @property
    def plot_color(self) -> tuple[int, int, int, int]: ...
    @plot_color.setter
    def plot_color(self, plot_color: tuple[int, int, int, int]) -> None: ...

    @property
    def plot_weight(self) -> float: ...
    @plot_weight.setter
    def plot_weight(self, plot_weight: float) -> None: ...

    @property
    def render_material_index(self) -> int: ...
    @render_material_index.setter
    def render_material_index(self, index: int) -> None: ...


class LayerTable:
    """Helper class that manages all the `Layer` (``ON_Layer``) added to the model.
    """
    def __getitem__(self, index: int) -> Layer:...

    def __iter__(self) -> Iterator[Layer]: ...

    def __len__(self) -> int: ...

    def add(self, layer: Layer) -> UUID:
        """Adds the ``layer`` to the table.

        Returns
        -------
        layer_uuid: UUID
            If the ``layer`` has been successfully added, ``ON_nil_uuid`` otherwise.
        """
        ...

    def count(self) -> int:
        """Returns the number of active model components of type
        ``ON_ModelComponent::Type::Layer`` in the table.

        Notes
        -----
        The ``count()`` does not include system components.
        """
        ...

    def delete_by_name(self, layer_name: str) -> bool:
        """Deletes the `Layer` given its full name, e.g., ``Layer 01::Nested layer 02``.

        Returns
        -------
        success: bool
            ``True`` if successfull, ``False`` otherwise.
        """
        ...

    def delete_by_uuid(self, layer_uuid: UUID) -> bool:
        """Deletes the `Layer` given its uuid.

        Returns
        -------
        success: bool
            ``True`` if successfull, ``False`` otherwise.
        """
        ...

    def get_by_index(self, layer_index: int) -> Layer:
        """Returns the ``Layer`` if the given ``index`` is found in the table, ``None``
        otherwise.

        Raises
        ------
        IndexError
            if ``layer_index`` is < 0
        """
        ...

    def get_by_name(self, full_name: str) -> Layer:
        """Returns the ``Layer`` if the given ``full_name`` is found in the table,
        ``None`` otherwise.
        """
        ...

    def get_by_uuid(self, layer_uuid: UUID) -> Layer:
        """Returns the ``Layer`` if the given ``layer_uuid`` is found in the table,
        ``None`` otherwise.
        """
        ...

    def get_index(self, full_name: str) -> int:
        """Returns the layer ``index`` if the given ``full_name`` is found in the table,
        ``ON_UNSET_INT_INDEX`` otherwise.
        """
        ...

    def get_uuid(self, full_name: str) -> UUID:
        """Returns the layer ``uuid`` if the given ``full_name`` is found in the table,
        ``ON_nil_uuid`` otherwise.
        """
        ...

    def has(self, full_name: str) -> bool:
        """Returns ``True`` if the given ``full_name`` is found in the table, ``False``
        otherwise.
        """
        ...

    def max_index(self) -> int:
        """Returns the maximum index among all active model components of type
        ``ON_ModelComponent::Type::Layer`` in the table.
        """
        ...


class Line:
    """Python bindings for the openNURBS ``ON_Line`` class.
    """
    def __eq__(self, other: object) -> bool: ...

    def __getitem__(self, index: int) -> Point3d: ...

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, start: Point3d, end: Point3d) -> None: ...

    def __ne__(self, other: object) -> bool: ...

    def __setitem__(self, index: int, value: Point3d) -> None: ...

    def create(self, start: Point3d, end: Point3d) -> bool:
        """Create a line from two points.

        Parameters
        ----------
        start: ``Point3d``
            Point at the start of line segment

        end: ``Point3d``
            Point at end of line segment

        Returns
        -------
        ``True`` if ``start`` and ``end`` are distinct points.
        """
        ...

    def distance_to(self, test_point: Point3d, finite_chord: bool = False) -> float:
        """Returns the distance from the point on the line that is closest to the
        ``test_point``. If ``finite_chord`` is ``True``, the distance is reported to the
        line as a finite chord.
        """
        ...

    def is_valid(self) -> bool:
        """Returns ``True`` if start ``!=`` end and both start and end are valid points.
        """
        ...

    def length(self) -> float:
        """Returns the length of the line.
        """
        ...

    def point_at(self, parameter: float) -> Point3d:
        """Returns a point on the (infinite) line, calculated as:
        ``(1 - parameter) * line.start + parameter * line.end``.
        """
        ...


class LineCurve(Geometry):
    """Python bindings for the openNURBS ``ON_LineCurve`` class.
    """
    line: Line

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, line: Line) -> None: ...

    @overload
    def __init__(self, start: Point3d, end: Point3d) -> None: ...

    def dimension(self) -> int:
        """Returns ``2`` or ``3`` (``2`` so ``ON_LineCurve`` can be uses as a trimming
        curve).
        """
        ...

    def is_valid(self, text_log: TextLog | None = None) -> bool:
        """Returns ``True`` if start ``!=`` end and both start and end are valid points.
        """
        ...

    def reverse(self) -> bool:
        """Reverses the parameterization. Domain changes from ``[a, b]`` to ``[-b, -a]``.
        """
        ...

    def set_end_point(self, new_end: Point3d) -> bool:
        """Forces the curve to end at a specified point.

        Parameters
        ----------
        new_end: Point3d
            The new end point.

        Returns
        -------
        ``True`` if successful, ``False`` otherwise.

        Notes
        -----
        Some end points cannot be moved. Be sure to check return code.
        """
        ...

    def set_start_point(self, new_end: Point3d) -> bool:
        """Forces the curve to start at a specified point.

        Parameters
        ----------
        new_start: Point3d
            The new start point.

        Returns
        -------
        ``True`` if successful, ``False`` otherwise.

        Notes
        -----
        Some start points cannot be moved. Be sure to check return code.
        """
        ...

    def swap_coordinates(self, index_i: int, index_j: int) -> bool:
        """Swaps the coordinates of the given indices.

        Returns
        -------
        ``True`` if successful, ``False`` otherwise.
        """
        ...


class Model:
    """Python bindings for the openNURBS ``ONX_Model`` class, via helper class ``Model``.

    ``ONX_Model``: pedagogical example of all the things in an OpenNURBS 3dm archive. The
    openNURBS examples use ONX_Model to store the information read from 3dm archives.
    """
    def __init__(self) -> None: ...

    def new_revision(self) -> int:
        """Returns the updated revision count.

        Notes
        -----
        If the current revision is set to ``0``, ``ON_3dmRevisionHistory`` is set to
        empty, overriding the current settings. Refer to ``../tests/test_model.py`` to
        understand the proper setup order.
        """
        ...

    def read(self, path_to_file: str) -> bool:
        """Reads an openNURBS archive and loads the information in this model.
        Before trying to read the 3dm file, the current model is reset!

        Parameters
        ----------
        path_to_file: ``str``
            Path to 3dm file, including file name and extension.

        Returns
        -------
        bool
            ``True`` if the archive is read without errors, ``False`` otherwise.
        """
        ...

    def reset(self) -> None:
        """Resets the current model.
        """
        ...

    def write(self, path_to_file: str, version: int = 7) -> bool:
        """Writes the content of this model to an openNURBS archive.

        Parameters
        ----------
        path_to_file: ``str``
            Path to 3dm file, including file name and extension.

        version: ``int``, optional default to ``7``
            Rhinoceros major varsion.

        Returns
        -------
        bool
            ``True`` if the archive is written without errors, ``False`` otherwise.
        """
        ...

    @property
    def application_details(self) -> str: ...
    @application_details.setter
    def application_details(self, details: str) -> None: ...

    @property
    def application_name(self) -> str: ...
    @application_name.setter
    def application_name(self, name: str) -> None: ...

    @property
    def application_url(self) -> str: ...
    @application_url.setter
    def application_url(self, url: str) -> None: ...

    @property
    def created_by(self) -> str: ...
    @created_by.setter
    def created_by(self, author: str) -> None: ...

    @property
    def last_edited_by(self) -> str: ...
    @last_edited_by.setter
    def last_edited_by(self, author: str) -> None: ...

    @property
    def archive_version(self) -> int: ...

    @property
    def LayerTable(self) -> LayerTable: ...

    @property
    def CurveTable(self) -> CurveTable: ...

    @property
    def ObjectTable(self) -> ObjectTable: ...

    @property
    def PointTable(self) -> PointTable: ...

    @property
    def revision(self) -> int: ...


class ModelComponent(OpenNURBSObject):
    """Python bindings for the openNURBS ``ON_ModelComponent`` class.

    ``ON_ModelComponent``: base class for all components in a model and manages the index,
    uuid and other information common to all components in a model.
    """
    def __init__(self) -> None: ...

    @overload
    def get_index(self) -> int:
        """Value of the runtime model component index attribute.

        Notes
        -----
        If the component is in a model, then the index is unique for all components of
        identical type in the model and is locked. If the index has not been set,
        ``ON_UNSET_INT_INDEX`` is returned. The ``get_index()`` value can change when
        saved in an archive (.3dm file). Use the `get_uuid()` when you need to reference
        model components in an archive.
        """
        ...

    @overload
    def get_index(self, index: int) -> int:
        """Value of the runtime model component index attribute.

        Parameters
        ----------
        index: int
            Value to return if the index has not been set. ``ON_UNSET_INT_INDEX`` or
            indices of default components are often used for this parameter.

        Notes
        -----
        If the component is in a model, then the index is unique for all components of
        identical type in the model and is locked. If the index has not been set,
        ``ON_UNSET_INT_INDEX`` is returned. The ``get_index()`` value can change when
        saved in an archive (.3dm file). Use the `get_uuid()` when you need to reference
        model components in an archive.
        """
        ...

    def get_uuid(self) -> UUID:
        """Value of the ``ON_UUID`` attribute.

        Notes
        -----
        If the component is in a model, then the ``ON_UUID`` is unique for all components
        in the model and is locked.
        """
        ...

    def parent_uuid_is_not_null(self) -> bool: ...

    def parent_uuid_is_null(self) -> bool: ...

    @overload
    def set_uuid(self, new_uuid: UUID) -> bool:
        """Value of the runtime model component index attribute.

        Returns
        -------
        value: bool
            ``True`` if the ``ON_UUID`` value was changed to ``new_uuid`` or is already
            equal to component_id. ``False`` if the ``ON_UUID`` value is locked and
            ``new_uuid != locked value``.
        """
        ...

    @overload
    def set_uuid(self) -> UUID:
        """Sets the id to a new value created by ``ON_CreateUuid()``.

        Returns
        -------
        value: UUID
            ``ON_nil_uuid`` if the ``ON_UUID`` was locked, otherwise the value of the new
            ``ON_UUID``.
        """
        ...

    def uuid_is_not_null(self) -> bool: ...

    def uuid_is_null(self) -> bool: ...


class ObjectAttributes(OpenNURBSObject):
    """Python bindings for the openNURBS ``ON_3dmObjectAttributes`` class.

    ``ON_3dmObjectAttributes``: Top level OpenNURBS objects have geometry and attributes.
    The geometry is stored in some class derived from ``ON_Geometry`` and the attributes
    are stored in an ``ON_3dmObjectAttributes`` class. Examples of attributes are object
    name, object id, display attributes, group membership, layer membership, and so on.
    """
    color: tuple[int, int, int, int]

    layer_index: int

    line_type_index: int

    material_index: int

    plot_color: tuple[int, int, int, int]

    def __init__(self) -> None: ...

    def __eq__(self, other: object) -> bool: ...

    def __ne__(self, other: object) -> bool: ...

    @property
    def color_source(self) -> ObjectColorSource: ...
    @color_source.setter
    def color_source(self, color_source: ObjectColorSource) -> None: ...

    @property
    def is_visible(self) -> bool: ...
    @is_visible.setter
    def is_visible(self, is_visible: bool) -> None: ...

    @property
    def mode(self) -> ObjectMode: ...
    @mode.setter
    def mode(self, mode: ObjectMode) -> None: ...

    @property
    def plot_color_source(self) -> PlotColorSource: ...
    @plot_color_source.setter
    def plot_color_source(self, plot_color_source: PlotColorSource) -> None: ...

    def default(self) -> None:
        """Initializes all attributes to the default values.
        """
        ...

    def get_name(self) -> str:
        """From ``ON_3dmObjectAttributes``:

        The ``m_name member`` is public to avoid breaking the SDK. Use `set_name` and
        `get_name` for proper validation. OpenNURBS object have optional text names. More
        than one object in a model can have the same name and some objects may have no
        name.
        """
        ...

    def set_name(self, name: str, fix_invalid_name: bool = False) -> bool:
        """From ``ON_3dmObjectAttributes``:

        The ``m_name member`` is public to avoid breaking the SDK. Use `set_name` and
        `get_name` for proper validation. OpenNURBS object have optional text names. More
        than one object in a model can have the same name and some objects may have no
        name.
        """
        ...


class ObjectColorSource(Enum):
    """Python bindings for the openNURBS ``object_color_source`` enumerator.
    """
    from_layer = 0
    from_object = 1
    from_material = 2
    from_parent = 3


class ObjectMode(Enum):
    """Python bindings for the openNURBS ``object_mode`` enumerator.
    """
    normal = 0
    hidden = 1
    locked = 2
    idef = 3
    mode_count = 4


class ObjectTable:
    def __getitem__(self, index: int) -> Layer: ...

    def __iter__(self) -> Iterator[Layer]: ...

    def __len__(self) -> int: ...

    @overload
    def add_line(self, start: Point3d, end: Point3d, obj_attr: None | ObjectAttributes = None) -> UUID:
        """Returns the ``UUID`` of the line in case of successful addition, or an empty
        ``UUID`` otherwise. If the line is in the model, then the ``UUID`` is unique for
        all components in the model and is locked.
        """
        ...

    @overload
    def add_line(self, line: Line, obj_attr: None | ObjectAttributes = None) -> UUID:
        """Returns the ``UUID`` of the line in case of successful addition, or an empty
        ``UUID`` otherwise. If the line is in the model, then the ``UUID`` is unique for
        all components in the model and is locked.
        """
        ...

    @overload
    def add_line(self, line: LineCurve, obj_attr: None | ObjectAttributes = None) -> UUID:
        """Returns the ``UUID`` of the line in case of successful addition, or an empty
        ``UUID`` otherwise. If the line is in the model, then the ``UUID`` is unique for
        all components in the model and is locked.
        """
        ...

    @overload
    def add_point(self, x: float, y: float, z: float, obj_attr: None | ObjectAttributes = None) -> UUID:
        """Returns the ``UUID`` of the point in case of successful addition, or an empty
        ``UUID`` otherwise. If the point is in the model, then the ``UUID`` is unique for
        all components in the model and is locked.
        """
        ...

    @overload
    def add_point(self, point: Point3d, obj_attr: None | ObjectAttributes = None) -> UUID:
        """Returns the ``UUID`` of the point in case of successful addition, or an empty
        ``UUID`` otherwise. If the point is in the model, then the ``UUID`` is unique for
        all components in the model and is locked.
        """
        ...

    @overload
    def add_point(self, point: PointGeometry, obj_attr: None | ObjectAttributes = None) -> UUID:
        """Returns the ``UUID`` of the point in case of successful addition, or an empty
        ``UUID`` otherwise. If the point is in the model, then the ``UUID`` is unique for
        all components in the model and is locked.
        """
        ...

    def count(self) -> int:
        """Returns the number of active model components of type
        ``ON_ModelComponent::Type::ModelGeometry`` in this table.

        Notes
        -----
        The ``count()`` does not include deleted components (for which ``is_deleted() =
        True``) and does not include system components.
        """
        ...

    def delete_by_uuid(self, object_uuid: UUID) -> bool:
        """Returns ``True`` if the object with the given ``object_uuid`` has been removed
        from the table.
        """
        ...

    def get_by_uuid(self, object_uuid: UUID) -> None | PointGeometry | LineCurve:
        """Returns the object with the given ``object_uuid`` or ``None`` if
        ``object_uuid`` is not found.
        """
        ...


class OpenNURBSObject:
    """Python bindings for the openNURBS ``ON_Object`` class.

    ``ON_Object``: pure virtual base class for all classes that must provide runtime class
    id or support object level 3DM serialization. Returns
    """
    def get_user_string(self, key: str) -> str:
        """Get the user string from the object.

        Parameters
        ----------
        key: ``str``
            the key used to retrieve the user string.

        Returns
        -------
        value: ``str``
            the ``str`` to be returned if the ``key`` has been found. Empty ``str`` is
            returned otherwise.
        """
        ...

    def is_corrupt(self, repair: bool, silent_error: bool, text_log: TextLog) -> bool:
        """Check for corrupt data values that are likely to cause crashes.

        Parameters
        ----------
        repair: ``bool``
            If ``True``, ``const_cast<>`` will be used to change the corrupt data so that
            crashes are less likely.

        silent_error: ``bool``
            If ``True``, ON_ERROR will not be called when corruption is detected.

        text_log: ``TextLog``
            If text_log is not null, then a description of corruption is printed using
            text_log.

        Notes
        -----
        Ideally, ``is_corrupt`` would be a virtual function on ``ON_Object``, but doing
        that at this point would break the public SDK.
        """
        ...

    def is_valid(self, text_log: TextLog | None = None) -> bool:
        """Tests an object to see if its data members are correctly initialized.

        Parameters
        ----------
        text_log: `TextLog`, optional
            If the object is not valid and ``text_log`` is not ``None``, then a brief
            english description of the reason the object is not valid is appended to the
            log. The information appended to ``text_log`` is suitable for low-level
            debugging purposes by programmers and is not intended to be useful as a high
            level user interface tool.

        Returns
        -------
        ``True`` if the object is valid or ``False`` if the object is invalid,
        uninitialized, etc.
        """
        ...

    def remove_user_string(self, key: str) -> bool:
        """Remove a user string in the form of a ``key``-``value`` string pair from the
        object.

        Parameters
        ----------
        key: ``str``
            key component of the string pair.

        Returns
        -------
        ``True`` if successful.
        """
        ...

    def set_user_string(self, key: str, value: str) -> bool:
        """Attach a user string in the form of a ``key``-``value`` string pair to the
        object. This information will persist through copy construction, operator ``=``,
        and file IO.

        Parameters
        ----------
        key: ``str``
            key component of the string pair.

        value: ``str``
            value component of the string pair.

        Returns
        -------
        ``True`` if successful.
        """
        ...

    def user_string_count(self) -> int:
        """Returns the number of user strings on the object.
        """
        ...


class PlotColorSource(Enum):
    """Python bindings for the openNURBS ``plot_color_source`` enumerator.
    """
    from_layer = 0
    from_object = 1
    from_material = 2
    from_parent = 3


class PointGeometry(Geometry):
    """Python wrapper for the openNURBS ``ON_Point`` class.
    """
    point: Point3d

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, x: float, y: float, z: float) -> None: ...

    @overload
    def __init__(self, point3d: Point3d) -> None: ...

    def is_valid(self, text_log: TextLog | None = None) -> bool:
        """Returns ``False`` if any coordinate is infinite, a nan, or ``ON_UNSET_VALUE``.
        """
        ...


class PointTable:
    def __iter__(self) -> Iterator[PointGeometry]: ...

    def __len__(self) -> int: ...

    @overload
    def add(self, x: float, y: float, z: float, attributes: None | ObjectAttributes = None) -> UUID:
        """Returns the ``UUID`` of the point in case of successful addition, or an empty
        ``UUID`` otherwise. If the point is in the model, then the ``UUID`` is unique for
        all components in the model and is locked.
        """
        ...

    @overload
    def add(self, point: PointGeometry, obj_attr: None | ObjectAttributes = None) -> UUID:
        """Returns the ``UUID`` of the point in case of successful addition, or an empty
        ``UUID`` otherwise. If the point is in the model, then the ``UUID`` is unique for
        all components in the model and is locked.
        """
        ...

    @overload
    def add(self, point: Point3d, obj_attr: None | ObjectAttributes = None) -> UUID:
        """Returns the ``UUID`` of the point in case of successful addition, or an empty
        ``UUID`` otherwise. If the point is in the model, then the ``UUID`` is unique for
        all components in the model and is locked.
        """
        ...

    def count(self) -> int:
        """Returns the number of objects of type ``ON::point_object`` in the model.
        """
        ...

    def get_by_uuid(self, object_uuid: UUID) -> PointGeometry | None:
        """Returns the object with the given ``object_uuid`` or ``None`` if
        ``object_uuid`` is not found.
        """
        ...


class Point3d:
    """Python wrapper for the openNURBS ``ON_3dPoint`` class.
    """
    def __add__(self, other: Point3d) -> Point3d: ...

    def __eq__(self, other: object) -> bool: ...

    def __init__(self, x: float, y: float, z: float) -> None: ...

    def __mul__(self, value: float) -> Point3d: ...

    def __ne__(self, other: object) -> bool: ...

    def __truediv__(self, value: float) -> Point3d: ...

    @property
    def x(self) -> float: ...
    @x.setter
    def x(self, value: float) -> None: ...

    @property
    def y(self) -> float: ...
    @y.setter
    def y(self, value: float) -> None: ...

    @property
    def z(self) -> float: ...
    @z.setter
    def z(self, value: float) -> None: ...

    def distance_to(self, point: Point3d) -> float:
        """Returns the distance between the two points.
        """
        ...

    def is_coincident(self, point: Point3d) -> bool:
        """In openNURBS points within ``ON_ZERO_TOLERANCE`` are generally considered to be
        the same.

        Returns
        -------
        ``True`` if for each coordinate pair ``|a - b| <= ON_ZERO_TOLERANCE`` or
        ``|a - b| <= (abs(a) + abs(b)) * ON_RELATIVE_TOLERANCE``.
        """
        ...


class TextLog:
    """Python bindings for openNURBS ``ON_TextLog`` class.
    """
    def __init__(self) -> None: ...

    def decrease_level_of_detail(self) -> LevelOfDetail:
        """Decrease the level of detail.

        Returns
        -------
        LevelOfDetail
            Level of detail to restore when this scope of decreased detail is finished.
        """
        ...

    def get_level_of_detail(self) -> LevelOfDetail:
        """Returns the level of detail.

        Returns
        -------
        LevelOfDetail
            Level of detail to print.
        """
        ...

    def increase_level_of_detail(self) -> LevelOfDetail:
        """Increase the level of detail.

        Returns
        -------
        LevelOfDetail
            Level of detail to restore when this scope of increased detail is finished.
        """
        ...

    def is_null(self) -> bool:
        """Returns ``True`` if this `TextLog` is ``ON_TextLog::Null``.
        """
        ...

    def set_level_of_detail(self, level: LevelOfDetail) -> None:
        """Sets the level of detail.
        """
        ...

    @staticmethod
    def null() -> TextLog:
        """``ON_TextLog::Null`` is a silent `TextLog` and can be used when no output is
        desired but an ``ON_TextLog`` parameter is required.
        """
        ...

    class LevelOfDetail(Enum):
        """``ON_TextLog::LevelOfDetail`` determines how much detail is printed. Functions
        that have an ``ON_TextLog`` parameter, like the ``dump`` functions, may use the
        level of detail to tailor their output.
        """
        Minimum = 0

        Medium = 1

        Maximum = 2
