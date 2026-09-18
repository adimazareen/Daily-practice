package com.example.buttonclick;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    private EditText etEmail;
    private EditText etPassword;
    private Button btnLogin;
    private TextView tvMessage;

    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);

        setContentView(R.layout.activity_main);

        // Initialize UI Components
        etEmail = findViewById(R.id.etEmail);
        etPassword = findViewById(R.id.etPassword);
        btnLogin = findViewById(R.id.btnLogin);
        tvMessage = findViewById(R.id.tvMessage);

        // Handle Login Button Click
        btnLogin.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View v) {

                String email =
                        etEmail.getText().toString().trim();

                String password =
                        etPassword.getText().toString().trim();

                // Validate input
                if (email.isEmpty() || password.isEmpty()) {

                    Toast.makeText(
                            MainActivity.this,
                            "Email and Password cannot be empty!",
                            Toast.LENGTH_SHORT
                    ).show();

                } else {

                    // Display success message
                    tvMessage.setText("Welcome Sami sir!");

                    tvMessage.setVisibility(View.VISIBLE);

                    Toast.makeText(
                            MainActivity.this,
                            "Login Successful!",
                            Toast.LENGTH_SHORT
                    ).show();
                }
            }
        });
    }
}
