# Smart Expense Tracker

A full-stack personal finance application with a web dashboard, Java Spring Boot REST API, SQLite storage, Python analytics, CSV export, and automated tests.

## Features
- Create, view, and delete income and expense transactions
- Categorize transactions and add descriptions and dates
- Monthly income, expense, and net-savings summaries
- Browser dashboard with transaction history
- CSV export from the web interface
- Python CLI analytics and CSV report utility
- SQLite by default; PostgreSQL configuration included
- Input validation and automated tests

## Architecture
- **Web:** HTML, CSS, vanilla JavaScript, served by Spring Boot
- **API:** Java 17+ and Spring Boot 3
- **Database:** SQLite by default; PostgreSQL via the `postgres` Spring profile
- **Analytics:** Python 3.10+ standard library

The browser calls the Java API. Java stores the data in `expenses.db` in the Java backend's working directory. The Python analytics script uses the same database path by default when run from `java-backend/`. Python analytics is an optional companion utility, not a separate web server.

## Requirements
- Java 17 or newer
- Maven 3.9+ (or use the Maven wrapper if you add one)
- Python 3.10+ for the analytics utility

## Run the web application (SQLite)
From the repository root:

```bash
cd java-backend
mvn spring-boot:run
```

Then open http://localhost:8080.

The SQLite database is created automatically as `java-backend/expenses.db`.

## Run tests
From `java-backend/`:

```bash
mvn test
```

From the repository root:

```bash
python -m unittest discover -s python -v
```

## Python analytics utility
Run from `java-backend/` so it finds the same SQLite database:

```bash
python ../python/analytics.py
```

Export a CSV report:

```bash
python ../python/analytics.py --export transactions.csv
```

Or select a month:

```bash
python ../python/analytics.py --year 2026 --month 10
```

## API endpoints
Base URL: `http://localhost:8080/api`

| Method | Endpoint | Description |
|---|---|---|
| GET | `/transactions` | List transactions |
| POST | `/transactions` | Create transaction |
| DELETE | `/transactions/{id}` | Delete transaction |
| GET | `/summary?year=2026&month=10` | Monthly summary |
| GET | `/transactions/export.csv` | Download CSV export |

Example POST body:

```json
{
  "type": "expense",
  "amount": 249.50,
  "category": "Food",
  "description": "Lunch",
  "transactionDate": "2026-10-25"
}
```

## PostgreSQL profile
Create a PostgreSQL database and set environment variables before launching:

```bash
export DB_URL=jdbc:postgresql://localhost:5432/expense_tracker
export DB_USERNAME=postgres
export DB_PASSWORD=your_password
mvn spring-boot:run -Dspring-boot.run.profiles=postgres
```

On Windows PowerShell, use `$env:DB_URL=...`, `$env:DB_USERNAME=...`, and `$env:DB_PASSWORD=...`.

Never commit real passwords. The PostgreSQL profile uses `schema-postgres.sql`; the default profile uses `schema-sqlite.sql`.

## Project structure
```text
Smart-Expense-Tracker/
├── README.md
├── .gitignore
├── LICENSE
├── requirements.txt
├── python/
│   ├── analytics.py
│   └── test_analytics.py
└── java-backend/
    ├── pom.xml
    ├── .gitignore
    └── src/
        ├── main/
        │   ├── java/com/example/expensetracker/
        │   │   ├── ExpenseTrackerApplication.java
        │   │   ├── config/WebConfig.java
        │   │   ├── controller/TransactionController.java
        │   │   ├── dto/CreateTransactionRequest.java
        │   │   ├── dto/MonthlySummary.java
        │   │   ├── dto/TransactionResponse.java
        │   │   ├── exception/ApiExceptionHandler.java
        │   │   ├── model/Transaction.java
        │   │   └── service/TransactionService.java
        │   └── resources/
        │       ├── application.properties
        │       ├── application-postgres.properties
        │       ├── schema-sqlite.sql
        │       ├── schema-postgres.sql
        │       └── static/
        │           ├── index.html
        │           ├── styles.css
        │           └── app.js
        └── test/java/com/example/expensetracker/
            └── TransactionServiceTest.java
```

## Roadmap
- [x] Web dashboard
- [x] Java REST API
- [x] SQLite storage
- [x] Monthly summary and CSV export
- [x] Python analytics and tests
- [x] PostgreSQL profile and schema
- [ ] Authentication and multiple user accounts
- [ ] Budget limits and spending alerts
- [ ] CI workflow and deployment

## Security notes
This is a learning project and does not include authentication, authorization, or production deployment hardening. Do not expose it publicly with real financial data until those protections are implemented.

## License
MIT. See [LICENSE](LICENSE).
