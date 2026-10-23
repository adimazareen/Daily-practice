
import csv
import sqlite3
from datetime import date
from pathlib import Path

DB_PATH = Path(__file__).parent / "expenses.db"

CATEGORIES = {
    "food", "travel", "education",
    "shopping", "bills", "health", "other"
}


def connect():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    connection.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            kind TEXT NOT NULL CHECK(kind IN ('income', 'expense')),
            amount REAL NOT NULL CHECK(amount > 0),
            category TEXT NOT NULL,
            note TEXT NOT NULL DEFAULT '',
            transaction_date TEXT NOT NULL
        )
    """)
    return connection


def add_transaction(kind, amount, category, note="",
                    transaction_date=None):
    kind = kind.lower()
    category = category.lower()
    transaction_date = transaction_date or date.today().isoformat()

    if kind not in {"income", "expense"}:
        raise ValueError("Kind must be income or expense.")
    if amount <= 0:
        raise ValueError("Amount must be greater than zero.")
    if category not in CATEGORIES:
        raise ValueError(f"Choose a category from {sorted(CATEGORIES)}.")
    date.fromisoformat(transaction_date)

    with connect() as db:
        cursor = db.execute("""
            INSERT INTO transactions
                (kind, amount, category, note, transaction_date)
            VALUES (?, ?, ?, ?, ?)
        """, (kind, amount, category, note, transaction_date))
        return cursor.lastrowid


def list_transactions():
    with connect() as db:
        return db.execute("""
            SELECT * FROM transactions
            ORDER BY transaction_date DESC, id DESC
        """).fetchall()


def get_summary(month=None):
    month = month or date.today().strftime("%Y-%m")

    with connect() as db:
        rows = db.execute("""
            SELECT kind, COALESCE(SUM(amount), 0) AS total
            FROM transactions
            WHERE transaction_date LIKE ?
            GROUP BY kind
        """, (f"{month}-%",)).fetchall()

    totals = {row["kind"]: row["total"] for row in rows}
    income = totals.get("income", 0.0)
    expenses = totals.get("expense", 0.0)

    return {
        "month": month,
        "income": income,
        "expenses": expenses,
        "savings": income - expenses,
    }


def export_csv(filename="expense_report.csv"):
    rows = list_transactions()
    fields = [
        "id", "kind", "amount", "category",
        "note", "transaction_date"
    ]

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(dict(row) for row in rows)

    return filename


def main():
    while True:
        print("\n=== SMART EXPENSE TRACKER ===")
        print("1. Add income")
        print("2. Add expense")
        print("3. View transactions")
        print("4. Monthly summary")
        print("5. Export CSV")
        print("0. Exit")

        choice = input("Choose an option: ").strip()

        try:
            if choice in {"1", "2"}:
                kind = "income" if choice == "1" else "expense"
                amount = float(input("Amount: ₹"))
                category = input(
                    f"Category {sorted(CATEGORIES)}: "
                ).strip().lower()
                note = input("Note (optional): ").strip()

                transaction_id = add_transaction(
                    kind, amount, category, note
                )
                print(f"Saved transaction #{transaction_id}.")

            elif choice == "3":
                for item in list_transactions():
                    print(
                        f"#{item['id']} | {item['transaction_date']} | "
                        f"{item['kind']} | ₹{item['amount']:.2f} | "
                        f"{item['category']} | {item['note']}"
                    )

            elif choice == "4":
                month = input("Month YYYY-MM (blank for current): ").strip()
                summary = get_summary(month or None)
                print(f"\nSummary for {summary['month']}")
                print(f"Income:  ₹{summary['income']:.2f}")
                print(f"Expenses: ₹{summary['expenses']:.2f}")
                print(f"Savings: ₹{summary['savings']:.2f}")

            elif choice == "5":
                filename = export_csv()
                print(f"Report saved to {filename}")

            elif choice == "0":
                print("Goodbye!")
                break

            else:
                print("Invalid option. Please choose again.")

        except (ValueError, sqlite3.Error, OSError) as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
