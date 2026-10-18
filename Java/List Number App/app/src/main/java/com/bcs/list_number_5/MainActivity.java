package com.bcs.list_number_5;

import android.content.Intent;
import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    EditText etNumber;
    Button btnNext;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        etNumber = findViewById(R.id.etNumber);
        btnNext = findViewById(R.id.btnNext);

        btnNext.setOnClickListener(v -> {

            String input = etNumber.getText()
                    .toString()
                    .trim();

            if (input.isEmpty()) {
                Toast.makeText(
                        MainActivity.this,
                        "Please enter a number",
                        Toast.LENGTH_SHORT
                ).show();
                return;
            }

            try {
                int number = Integer.parseInt(input);

                Intent intent = new Intent(
                        MainActivity.this,
                        DisplayActivity.class
                );

                intent.putExtra("inputNumber", number);
                startActivity(intent);

            } catch (NumberFormatException e) {
                Toast.makeText(
                        MainActivity.this,
                        "Please enter a valid integer",
                        Toast.LENGTH_SHORT
                ).show();
            }
        });
    }
}
