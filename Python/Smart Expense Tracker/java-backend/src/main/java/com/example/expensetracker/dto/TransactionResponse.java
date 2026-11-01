package com.example.expensetracker.dto;

import java.math.BigDecimal;
import java.time.LocalDate;

public record TransactionResponse(
        long id,
        String type,
        BigDecimal amount,
        String category,
        String description,
        LocalDate transactionDate
) {}
