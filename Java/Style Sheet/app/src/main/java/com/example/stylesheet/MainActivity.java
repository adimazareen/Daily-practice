package com.example.stylesheet;

import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);

        setContentView(R.layout.activity_main);

        EditText editText = findViewById(R.id.editText);

        Button button = findViewById(R.id.button);

        button.setOnClickListener(v -> {

            String input =
                    editText.getText().toString();

            editText.setText(
                    "You entered: " + input
            );
        });
    }
}
