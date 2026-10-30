package com.example.expensetracker;

import com.example.expensetracker.dto.CreateTransactionRequest;
import com.example.expensetracker.dto.MonthlySummary;
import com.example.expensetracker.dto.TransactionResponse;
import com.example.expensetracker.service.TransactionService;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.Test;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.datasource.DriverManagerDataSource;

import java.math.BigDecimal;
import java.nio.file.Files;
import java.nio.file.Path;
import java.time.LocalDate;

import static org.junit.jupiter.api.Assertions.*;

class TransactionServiceTest {
    private JdbcTemplate jdbc;
    private TransactionService service;
    private Path databaseFile;

    @BeforeEach
    void setUp() throws Exception {
        databaseFile = Files.createTempFile("expense-tracker-test-", ".db");
        DriverManagerDataSource dataSource = new DriverManagerDataSource();
        dataSource.setDriverClassName("org.sqlite.JDBC");
        dataSource.setUrl("jdbc:sqlite:" + databaseFile.toAbsolutePath());
        jdbc = new JdbcTemplate(dataSource);
        jdbc.execute("""
                CREATE TABLE transactions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    type VARCHAR(10) NOT NULL CHECK (type IN ('income', 'expense')),
                    amount NUMERIC(12, 2) NOT NULL CHECK (amount > 0),
                    category VARCHAR(100) NOT NULL,
                    description VARCHAR(500) NOT NULL DEFAULT '',
                    transaction_date VARCHAR(10) NOT NULL
                )
                """);
        service = new TransactionService(jdbc);
    }

    @AfterEach
    void cleanUp() throws Exception {
        if (databaseFile != null) Files.deleteIfExists(databaseFile);
    }

    @Test
    void createsAndListsTransaction() {
        var request = new CreateTransactionRequest("expense", new BigDecimal("125.50"),
                "Food", "Lunch", LocalDate.parse("2026-10-25"));
        TransactionResponse created = service.create(request);
        assertEquals("expense", created.type());
        assertEquals(0, new BigDecimal("125.50").compareTo(created.amount()));
        assertEquals(1, service.findAll().size());
    }

    @Test
    void calculatesMonthlySummary() {
        service.create(new CreateTransactionRequest("income", new BigDecimal("1000"),
                "Salary", "", LocalDate.parse("2026-10-01")));
        service.create(new CreateTransactionRequest("expense", new BigDecimal("250"),
                "Food", "", LocalDate.parse("2026-10-02")));
        MonthlySummary summary = service.summary(2026, 10);
        assertEquals(0, new BigDecimal("1000").compareTo(summary.income()));
        assertEquals(0, new BigDecimal("250").compareTo(summary.expenses()));
        assertEquals(0, new BigDecimal("750").compareTo(summary.savings()));
        assertEquals(2, summary.transactionCount());
    }

    @Test
    void rejectsInvalidType() {
        var request = new CreateTransactionRequest("transfer", new BigDecimal("5"),
                "Other", "", LocalDate.now());
        assertThrows(IllegalArgumentException.class, () -> service.create(request));
    }

    @Test
    void deletingMissingTransactionThrows() {
        assertThrows(TransactionService.TransactionNotFoundException.class,
                () -> service.delete(999));
    }
}
