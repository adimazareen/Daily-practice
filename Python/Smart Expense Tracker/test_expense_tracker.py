
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import expense_tracker as app


class ExpenseTrackerTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.db_path = Path(self.temp_dir.name) / "test.db"
        self.db_patch = patch.object(app, "DB_PATH", self.db_path)
        self.db_patch.start()

    def tearDown(self):
        self.db_patch.stop()
        self.temp_dir.cleanup()

    def test_add_and_summarize(self):
        app.add_transaction("income", 5000, "other")
        app.add_transaction("expense", 500, "food")

        summary = app.get_summary()

        self.assertEqual(summary["income"], 5000)
        self.assertEqual(summary["expenses"], 500)
        self.assertEqual(summary["savings"], 4500)

    def test_reject_invalid_amount(self):
        with self.assertRaises(ValueError):
            app.add_transaction("expense", -100, "food")

    def test_reject_invalid_category(self):
        with self.assertRaises(ValueError):
            app.add_transaction("expense", 100, "invalid-category")


if __name__ == "__main__":
    unittest.main()
