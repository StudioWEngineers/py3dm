# standard library imports
from unittest import TestCase

# third party library imports
from py3dm import TextLog

# local library specific imports


class TextLogTestSuite(TestCase):
    def setUp(self) -> None:
        self.text_log = TextLog()

    def test_decrease_level_of_detail(self) -> None:
        with self.subTest(msg="Test return value"):
            self.assertEqual(
                self.text_log.decrease_level_of_detail(),
                TextLog.LevelOfDetail.Medium
            )

        with self.subTest(msg="Test updated value"):
            self.assertEqual(
                self.text_log.get_level_of_detail(),
                TextLog.LevelOfDetail.Minimum
            )

    def test_get_level_of_detail(self) -> None:
        self.assertEqual(
            self.text_log.get_level_of_detail(),
            TextLog.LevelOfDetail.Medium
        )

    def test_increase_level_of_detail(self) -> None:
        with self.subTest(msg="Test return value"):
            self.assertEqual(
                self.text_log.increase_level_of_detail(),
                TextLog.LevelOfDetail.Medium
            )

        with self.subTest(msg="Test updated value"):
            self.assertEqual(
                self.text_log.get_level_of_detail(),
                TextLog.LevelOfDetail.Maximum
            )

    def test_is_null(self) -> None:
        with self.subTest(msg="Test not null TextLog"):
            self.assertFalse(self.text_log.is_null())

        with self.subTest(msg="Test null TextLog"):
            self.assertTrue(TextLog.null().is_null())

    def test_level_of_detail_is_at_least(self) -> None:
        self.assertTrue(
            self.text_log.level_of_detail_is_at_least(
                TextLog.LevelOfDetail.Medium
            )
        )

    def test_null(self) -> None:
        self.assertIsInstance(self.text_log.null(), TextLog)

    def test_set_level_of_detail(self) -> None:
        self.text_log.set_level_of_detail(TextLog.LevelOfDetail.Minimum)
        self.assertEqual(
            self.text_log.get_level_of_detail(),
            TextLog.LevelOfDetail.Minimum
        )
