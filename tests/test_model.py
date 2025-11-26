"""
ModelTestSuite
--------------

Test suites for the `Model` class.
"""
# standard library imports
from tempfile import TemporaryDirectory
from unittest import TestCase

# third party library imports
from py3dm import Layer, Model, Point3d

# local library specific imports


class NewModelTestSuite(TestCase):
    """Tests for the `Model` class.
    """
    def setUp(self) -> None:
        self.model = Model()

    def test_application_details(self) -> None:
        """Tests for the `application_details` property.
        """
        with self.subTest(msg="Before assignment"):
            self.assertEqual(self.model.application_details, "")

        self.model.application_details = "custom string"

        with self.subTest(msg="After assignment"):
            self.assertEqual(self.model.application_details, "custom string")

    def test_application_name(self) -> None:
        """Tests for the `application_name` property.
        """
        with self.subTest(msg="Before assignment"):
            self.assertEqual(self.model.application_name, "")

        self.model.application_name = "custom string"

        with self.subTest(msg="After assignment"):
            self.assertEqual(self.model.application_name, "custom string")

    def test_application_url(self) -> None:
        """Tests for the `application_url` property.
        """
        with self.subTest(msg="Before assignment"):
            self.assertEqual(self.model.application_url, "")

        self.model.application_url = "custom string"

        with self.subTest(msg="After assignment"):
            self.assertEqual(self.model.application_url, "custom string")

    def test_archive_version(self) -> None:
        """Test for the `archive_version` property.
        """
        self.assertEqual(self.model.archive_version, 0)

    def test_created_by(self) -> None:
        """Tests for the `created_by` property.
        """
        with self.subTest(msg="Before assignment"):
            self.assertEqual(self.model.created_by, "")

        self.model.created_by = "StudioWEngineers"

        with self.subTest(msg="After assignment"):
            self.assertEqual(self.model.created_by, "StudioWEngineers")

    def test_last_edited_by(self) -> None:
        """Tests for the `last_edited_by` property.
        """
        with self.subTest(msg="Before assignment"):
            self.assertEqual(self.model.last_edited_by, "")

        self.model.last_edited_by = "StudioWEngineers"

        with self.subTest(msg="After assignment"):
            self.assertEqual(self.model.last_edited_by, "StudioWEngineers")

    def test_revision(self) -> None:
        """Tests for the `revision` property.
        """
        with self.subTest(msg="Before assignment"):
            self.assertEqual(self.model.revision, 0)

        with self.subTest(msg="Assignment"):
            self.assertEqual(self.model.new_revision(), 1)

        with self.subTest(msg="After assignment"):
            self.assertEqual(self.model.revision, 1)


class WriteAndReadModelTestSuite(TestCase):
    """Tests for the `Model` class. A new model is created from scratch, then written and
    lastly read to ensure the correctness of the workflow.
    """
    def setUp(self) -> None:
        # create a model with custom info
        model = Model()
        model.new_revision()
        model.application_details = "WriteAndReadModelTestSuite"
        model.application_name = "Rhinoceros 7"
        model.application_url = "custom URL"
        model.created_by = "StudioWEngineers"
        model.last_edited_by = "StudioWEngineers"

        # create the model for tests
        self.model = Model()

        with TemporaryDirectory() as temp_dir:
            model.write(temp_dir + "/WriteAndReadModelTestSuite.3dm", 7)
            self.model.read(temp_dir + "/WriteAndReadModelTestSuite.3dm")

    def test_application_details(self) -> None:
        """Test for the `application_details` property.
        """
        self.assertEqual(self.model.application_details, "WriteAndReadModelTestSuite")

    def test_application_name(self) -> None:
        """Test for the `application_name` property.
        """
        self.assertEqual(self.model.application_name, "Rhinoceros 7")

    def test_application_url(self) -> None:
        """Test for the `application_url` property.
        """
        self.assertEqual(self.model.application_url, "custom URL")

    def test_archive_version(self) -> None:
        """Test for the `archive_version` property.
        """
        self.assertEqual(self.model.archive_version, 70)

    def test_created_by(self) -> None:
        """Test for the `created_by` property.
        """
        self.assertEqual(self.model.created_by, "StudioWEngineers")

    def test_last_edited_by(self) -> None:
        """Test for the `last_edited_by` property.
        """
        self.assertEqual(self.model.last_edited_by, "StudioWEngineers")

    def test_revision(self) -> None:
        """Test for the `revision` property.
        """
        self.assertEqual(self.model.revision, 1)


class ResetModelTestSuite(TestCase):
    """Tests for the `Model` class, `reset` method.
    """
    def setUp(self) -> None:
        # create a model with custom info, one layer and one geometrical object
        self.model = Model()
        self.model.new_revision()
        self.model.created_by = "StudioWEngineers"
        self.model.last_edited_by = "StudioWEngineers"

        self.model.LayerTable.add(Layer())
        self.model.CurveTable.add(Point3d(0, 1, 2), Point3d(0, 1, 0))

        self.model.reset()

    def test_created_by(self) -> None:
        """Check the `created_by` property after `reset`.
        """
        self.assertEqual(self.model.created_by, "")

    def test_last_edited_by(self) -> None:
        """Check the `last_edited_by` property after `reset`.
        """
        self.assertEqual(self.model.last_edited_by, "")

    def test_number_of_layers(self) -> None:
        """Check the number of `Layer`s in the model after `reset`.
        """
        self.assertEqual(len(list(self.model.LayerTable)), 0)

    def test_number_of_objects(self) -> None:
        """Check the number of objects in the model after `reset`.
        """
        self.assertEqual(len(list(self.model.ObjectTable)), 0)

    def test_revision(self) -> None:
        """Check the `revision` property after `reset`.
        """
        self.assertEqual(self.model.revision, 0)
