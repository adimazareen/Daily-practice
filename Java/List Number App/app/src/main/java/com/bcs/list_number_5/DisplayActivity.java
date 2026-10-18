package com.bcs.list_number_5;

import android.os.Bundle;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

import java.util.Arrays;
import java.util.List;

public class DisplayActivity extends AppCompatActivity {

    TextView tvPassed, tvListCount;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_display);

        tvPassed = findViewById(R.id.tvPassed);
        tvListCount = findViewById(R.id.tvListCount);

        // Receive the number from MainActivity
        int passedNumber = getIntent()
                .getIntExtra("inputNumber", 0);

        tvPassed.setText("Passed number: " + passedNumber);

        // Create a sample list
        List<String> items = Arrays.asList(
                "Apple",
                "Banana",
                "Cherry",
                "Dates",
                "Elderberry"
        );

        // Count the items in the list
        int count = items.size();

        tvListCount.setText(
                "Number of items in the list: " + count
        );
    }
}
