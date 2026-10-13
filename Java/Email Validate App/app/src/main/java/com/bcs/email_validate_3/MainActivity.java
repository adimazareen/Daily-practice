package com.bcs.email_validate_3;

import android.os.Bundle;
import android.text.Editable;
import android.text.TextWatcher;
import android.util.Patterns;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    EditText etEmail, etPassword;
    Button btnLogin;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        setContentView(R.layout.activity_login);

        etEmail = findViewById(R.id.etEmail);
        etPassword = findViewById(R.id.etPassword);
        btnLogin = findViewById(R.id.btnLogin);

        // Disable Login until the email format is valid.
        btnLogin.setEnabled(false);

        etEmail.addTextChangedListener(new TextWatcher() {

            @Override
            public void beforeTextChanged(
                    CharSequence s,
                    int start,
                    int count,
                    int after) {
            }

            @Override
            public void onTextChanged(
                    CharSequence email,
                    int start,
                    int before,
                    int count) {

                boolean isValid =
                        Patterns.EMAIL_ADDRESS
                                .matcher(email)
                                .matches();

                btnLogin.setEnabled(isValid);
            }

            @Override
            public void afterTextChanged(Editable s) {
            }
        });

        btnLogin.setOnClickListener(view -> {

            String email =
                    etEmail.getText().toString().trim();

            String pass =
                    etPassword.getText().toString();

            if (Patterns.EMAIL_ADDRESS.matcher(email).matches()
                    && email.equals("admin@gmail.com")
                    && pass.equals("1234")) {

                Toast.makeText(
                        MainActivity.this,
                        "Login Successful",
                        Toast.LENGTH_SHORT
                ).show();

            } else {

                Toast.makeText(
                        MainActivity.this,
                        "Invalid Credentials",
                        Toast.LENGTH_SHORT
                ).show();
            }
        });
    }
}
