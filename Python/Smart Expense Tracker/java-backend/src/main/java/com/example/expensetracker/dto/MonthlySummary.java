package com.example.expensetracker.dto;

import java.math.BigDecimal;

public record MonthlySummary(
        int year,
        int month,
        BigDecimal income,
        BigDecimal expenses,
        BigDecimal savings,
        int transactionCount
) {}
