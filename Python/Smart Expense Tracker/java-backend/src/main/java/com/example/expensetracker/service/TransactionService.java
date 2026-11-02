package com.example.expensetracker.service;

import com.example.expensetracker.dto.CreateTransactionRequest;
import com.example.expensetracker.dto.MonthlySummary;
import com.example.expensetracker.dto.TransactionResponse;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.core.RowMapper;
import org.springframework.stereotype.Service;

import java.math.BigDecimal;
import java.sql.Date;
import java.time.LocalDate;
import java.util.List;
import java.util.Locale;

@Service
public class TransactionService {
    private final JdbcTemplate jdbc;

    private final RowMapper<TransactionResponse> mapper = (rs, rowNum) ->
            new TransactionResponse(
                    rs.getLong("id"),
                    rs.getString("type"),
                    rs.getBigDecimal("amount"),
                    rs.getString("category"),
                    rs.getString("description"),
                    LocalDate.parse(rs.getString("transaction_date"))
            );

    public TransactionService(JdbcTemplate jdbc) {
        this.jdbc = jdbc;
    }

    public List<TransactionResponse> findAll() {
        return jdbc.query("""
                SELECT id, type, amount, category, description, transaction_date
                FROM transactions
                ORDER BY transaction_date DESC, id DESC
                """, mapper);
    }

    public TransactionResponse create(CreateTransactionRequest request) {
        String type = request.type().trim().toLowerCase(Locale.ROOT);
        if (!type.equals("income") && !type.equals("expense")) {
            throw new IllegalArgumentException("Type must be income or expense.");
        }
        if (request.amount() == null || request.amount().compareTo(BigDecimal.ZERO) <= 0) {
            throw new IllegalArgumentException("Amount must be greater than zero.");
        }
        String category = request.category() == null ? "" : request.category().trim();
        if (category.isEmpty()) {
            throw new IllegalArgumentException("Category cannot be empty.");
        }
        String description = request.description() == null ? "" : request.description().trim();
        LocalDate transactionDate = request.transactionDate();
        if (transactionDate == null) {
            throw new IllegalArgumentException("Transaction date is required.");
        }

        jdbc.update("""
                INSERT INTO transactions
                    (type, amount, category, description, transaction_date)
                VALUES (?, ?, ?, ?, ?)
                """,
                type, request.amount(), category, description, transactionDate.toString());

        Long id = jdbc.queryForObject("SELECT MAX(id) FROM transactions", Long.class);
        return jdbc.queryForObject("""
                SELECT id, type, amount, category, description, transaction_date
                FROM transactions WHERE id = ?
                """, mapper, id);
    }

    public void delete(long id) {
        int changed = jdbc.update("DELETE FROM transactions WHERE id = ?", id);
        if (changed == 0) {
            throw new TransactionNotFoundException(id);
        }
    }

    public MonthlySummary summary(int year, int month) {
        if (year < 1 || year > 9999 || month < 1 || month > 12) {
            throw new IllegalArgumentException("Enter a valid year and month.");
        }
        String prefix = String.format("%04d-%02d", year, month);
        List<MonthlySummaryRow> rows = jdbc.query("""
                SELECT type, COALESCE(SUM(amount), 0) AS total, COUNT(*) AS count
                FROM transactions
                WHERE SUBSTRING(transaction_date, 1, 7) = ?
                GROUP BY type
                """,
                (rs, rowNum) -> new MonthlySummaryRow(
                        rs.getString("type"), rs.getBigDecimal("total"), rs.getInt("count")),
                prefix);

        BigDecimal income = BigDecimal.ZERO;
        BigDecimal expenses = BigDecimal.ZERO;
        int count = 0;
        for (MonthlySummaryRow row : rows) {
            count += row.count();
            if ("income".equals(row.type())) income = row.total();
            if ("expense".equals(row.type())) expenses = row.total();
        }
        income = income == null ? BigDecimal.ZERO : income;
        expenses = expenses == null ? BigDecimal.ZERO : expenses;
        return new MonthlySummary(year, month, income, expenses,
                income.subtract(expenses), count);
    }

    public List<TransactionResponse> forCsv() {
        return findAll();
    }

    private record MonthlySummaryRow(String type, BigDecimal total, int count) {}

    public static class TransactionNotFoundException extends RuntimeException {
        public TransactionNotFoundException(long id) {
            super("Transaction " + id + " was not found.");
        }
    }
}
