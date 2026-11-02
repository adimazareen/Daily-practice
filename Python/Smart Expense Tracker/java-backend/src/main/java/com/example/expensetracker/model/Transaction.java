package com.example.expensetracker.model;

import java.math.BigDecimal;
import java.time.LocalDate;

public record Transaction(
        long id,
        String type,
        BigDecimal amount,
        String category,
        String description,
        LocalDate transactionDate
) {}
