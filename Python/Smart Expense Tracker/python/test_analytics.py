import sqlite3
import tempfile
import unittest
from pathlib import Path

from analytics import get_month_summary, export_transactions


class AnalyticsTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.db = Path(self.temp.name) / "test.db"
        with sqlite3.connect(self.db) as conn:
            conn.execute("""CREATE TABLE transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                type TEXT NOT NULL,
                amount NUMERIC NOT NULL,
                category TEXT NOT NULL,
                description TEXT NOT NULL DEFAULT '',
                transaction_date TEXT NOT NULL
            )""")
            conn.executemany(
                """INSERT INTO transactions
                   (type, amount, category, description, transaction_date)
                   VALUES (?, ?, ?, ?, ?)""",
                [
                    ("income", 30000, "Salary", "", "2026-10-01"),
                    ("expense", 5000, "Rent", "", "2026-10-02"),
                    ("expense", 1000, "Food", "", "2026-09-15"),
                ],
            )

    def tearDown(self):
        self.temp.cleanup()

    def test_month_summary(self):
        result = get_month_summary(self.db, 2026, 10)
        self.assertEqual(result["income"], 30000)
        self.assertEqual(result["expenses"], 5000)
        self.assertEqual(result["savings"], 25000)
        self.assertEqual(result["transaction_count"], 2)

    def test_empty_database_path_returns_zero_summary(self):
        result = get_month_summary(Path(self.temp.name) / "missing.db", 2026, 10)
        self.assertEqual(result["income"], 0)
        self.assertEqual(result["transaction_count"], 0)

    def test_invalid_month_rejected(self):
        with self.assertRaises(ValueError):
            get_month_summary(self.db, 2026, 13)

    def test_csv_export(self):
        output = Path(self.temp.name) / "report.csv"
        export_transactions(self.db, output)
        self.assertTrue(output.exists())
        self.assertIn("transaction_date", output.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
