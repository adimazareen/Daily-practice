package com.example.relativelayout;

import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    EditText usernameInput;
    EditText passwordInput;
    Button loginButton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        setContentView(R.layout.activity_main);

        // Linking views from XML
        usernameInput = findViewById(R.id.usernameInput);
        passwordInput = findViewById(R.id.passwordInput);
        loginButton = findViewById(R.id.loginButton);

        // Setting up Login button click listener
        loginButton.setOnClickListener(v -> {

            String username = usernameInput
                    .getText()
                    .toString()
                    .trim();

            String password = passwordInput
                    .getText()
                    .toString()
                    .trim();

            if (username.isEmpty() || password.isEmpty()) {

                Toast.makeText(
                        MainActivity.this,
                        "Please enter both fields",
                        Toast.LENGTH_SHORT
                ).show();

            } else {

                Toast.makeText(
                        MainActivity.this,
                        "Welcome, " + username + "!",
                        Toast.LENGTH_SHORT
                ).show();
            }
        });
    }
}
