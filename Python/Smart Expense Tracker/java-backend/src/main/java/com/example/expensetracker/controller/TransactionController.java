package com.example.expensetracker.controller;

import com.example.expensetracker.dto.CreateTransactionRequest;
import com.example.expensetracker.dto.MonthlySummary;
import com.example.expensetracker.dto.TransactionResponse;
import com.example.expensetracker.service.TransactionService;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.validation.Valid;
import org.springframework.format.annotation.DateTimeFormat;
import org.springframework.web.bind.annotation.*;

import java.io.IOException;
import java.io.PrintWriter;
import java.time.LocalDate;
import java.util.List;

@RestController
@RequestMapping("/api")
public class TransactionController {
    private final TransactionService service;

    public TransactionController(TransactionService service) {
        this.service = service;
    }

    @GetMapping("/transactions")
    public List<TransactionResponse> allTransactions() {
        return service.findAll();
    }

    @PostMapping("/transactions")
    @ResponseStatus(org.springframework.http.HttpStatus.CREATED)
    public TransactionResponse create(@Valid @RequestBody CreateTransactionRequest request) {
        return service.create(request);
    }

    @DeleteMapping("/transactions/{id}")
    @ResponseStatus(org.springframework.http.HttpStatus.NO_CONTENT)
    public void delete(@PathVariable long id) {
        service.delete(id);
    }

    @GetMapping("/summary")
    public MonthlySummary summary(
            @RequestParam(required = false) Integer year,
            @RequestParam(required = false) Integer month) {
        LocalDate today = LocalDate.now();
        return service.summary(year == null ? today.getYear() : year,
                month == null ? today.getMonthValue() : month);
    }

    @GetMapping("/transactions/export.csv")
    public void exportCsv(HttpServletResponse response) throws IOException {
        response.setContentType("text/csv; charset=UTF-8");
        response.setHeader("Content-Disposition", "attachment; filename=transactions.csv");
        try (PrintWriter writer = response.getWriter()) {
            writer.println("id,type,amount,category,description,transaction_date");
            for (TransactionResponse t : service.forCsv()) {
                writer.printf("%d,%s,%s,%s,%s,%s%n",
                        t.id(), csv(t.type()), t.amount().toPlainString(),
                        csv(t.category()), csv(t.description()), t.transactionDate());
            }
        }
    }

    private String csv(String value) {
        String safe = value == null ? "" : value;
        return "\"" + safe.replace("\"", "\"\"") + "\"";
    }
}
