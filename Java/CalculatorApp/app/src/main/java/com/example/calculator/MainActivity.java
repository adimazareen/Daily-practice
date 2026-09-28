package com.example.calculator;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    EditText editText;

    String input = "";
    String operator = "";

    double num1;
    double num2;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        editText = findViewById(R.id.editText);
    }

    public void onDigitClick(View view) {
        Button button = (Button) view;
        input += button.getText().toString();
        editText.setText(input);
    }

    public void onOperatorClick(View view) {
        Button button = (Button) view;
        if (!input.isEmpty()) {
            num1 = Double.parseDouble(input);
            operator = button.getText().toString();
            input = "";
        }
    }

    public void onEqualClick(View view) {
        if (!input.isEmpty() && !operator.isEmpty()) {
            num2 = Double.parseDouble(input);
            double result = 0;
            switch (operator) {
                case "+":
                    result = num1 + num2;
                    break;

                case "-":
                    result = num1 - num2;
                    break;

                case "×":
                    result = num1 * num2;
                    break;

                case "÷":
                    if (num2 != 0) {
                        result = num1 / num2;
                    } else {
                        editText.setText("Cannot divide by zero");
                        input = "";
                        operator = "";
                        return;
                    }
                    break;

                case "%":
                    result = num1 % num2;
                    break;
            }

            editText.setText(String.valueOf(result));
            input = "";
            operator = "";
        }
    }

    public void onClearClick(View view) {

        input = "";
        operator = "";

        num1 = 0;
        num2 = 0;

        editText.setText("");
    }

    public void onBackspaceClick(View view) {

        if (!input.isEmpty()) {

            input = input.substring(
                    0,
                    input.length() - 1
            );
            editText.setText(input);
        }
    }
}
