"""Monthly analytics and CSV export for the Smart Expense Tracker SQLite database."""
import argparse
import csv
import sqlite3
from pathlib import Path
from datetime import date

DEFAULT_DB = Path("expenses.db")
FIELDS = ["id", "type", "amount", "category", "description", "transaction_date"]


def get_month_summary(db_path=DEFAULT_DB, year=None, month=None):
    today = date.today()
    year = today.year if year is None else int(year)
    month = today.month if month is None else int(month)
    if not 1 <= month <= 12 or not 1 <= year <= 9999:
        raise ValueError("Provide a valid year and month (1-12).")
    if not Path(db_path).exists():
        return {"year": year, "month": month, "income": 0.0,
                "expenses": 0.0, "savings": 0.0, "transaction_count": 0}
    with sqlite3.connect(str(db_path)) as conn:
        conn.row_factory = sqlite3.Row
        # Works with the SQLite schema used by the Java application.
        rows = conn.execute(
            """SELECT type, COALESCE(SUM(amount), 0) AS total, COUNT(*) AS count
               FROM transactions WHERE substr(transaction_date, 1, 7) = ?
               GROUP BY type""",
            (f"{year:04d}-{month:02d}",),
        ).fetchall()
    income = expenses = 0.0
    count = 0
    for row in rows:
        count += row["count"]
        if row["type"] == "income":
            income = float(row["total"])
        elif row["type"] == "expense":
            expenses = float(row["total"])
    income, expenses = round(income, 2), round(expenses, 2)
    return {"year": year, "month": month, "income": income,
            "expenses": expenses, "savings": round(income - expenses, 2),
            "transaction_count": count}


def export_transactions(db_path=DEFAULT_DB, output_path="transactions.csv"):
    if not Path(db_path).exists():
        raise FileNotFoundError(f"Database not found: {db_path}. Run the Java app first.")
    with sqlite3.connect(str(db_path)) as conn:
        conn.row_factory = sqlite3.Row
        rows = conn.execute(
            "SELECT id, type, amount, category, description, transaction_date "
            "FROM transactions ORDER BY transaction_date DESC, id DESC"
        ).fetchall()
    output = Path(output_path)
    with output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows([dict(row) for row in rows])
    return output


def main():
    parser = argparse.ArgumentParser(description="Smart Expense Tracker Python analytics")
    parser.add_argument("--db", default=str(DEFAULT_DB), help="SQLite database path")
    parser.add_argument("--year", type=int, help="Summary year")
    parser.add_argument("--month", type=int, help="Summary month (1-12)")
    parser.add_argument("--export", metavar="FILE", help="Export transactions to CSV")
    args = parser.parse_args()

    summary = get_month_summary(args.db, args.year, args.month)
    print(f"Summary: {summary['year']}-{summary['month']:02d}")
    print(f"Income:       ₹{summary['income']:.2f}")
    print(f"Expenses:     ₹{summary['expenses']:.2f}")
    print(f"Net savings:  ₹{summary['savings']:.2f}")
    print(f"Transactions: {summary['transaction_count']}")
    if args.export:
        print(f"CSV exported to {export_transactions(args.db, args.export)}")


if __name__ == "__main__":
    main()
