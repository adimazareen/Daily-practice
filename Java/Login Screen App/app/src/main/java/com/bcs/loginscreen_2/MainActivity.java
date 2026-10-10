package com.bcs.loginscreen_2;

import android.content.Intent;
import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    EditText etUsername, etPassword;
    Button btnLogin;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        setContentView(R.layout.activity_login);

        etUsername = findViewById(R.id.etUsername);
        etPassword = findViewById(R.id.etPassword);
        btnLogin = findViewById(R.id.btnLogin);

        btnLogin.setOnClickListener(v -> {

            String user = etUsername.getText()
                    .toString().trim();

            String pass = etPassword.getText()
                    .toString();

            if (user.equals("admin") && pass.equals("1234")) {

                Toast.makeText(
                        MainActivity.this,
                        "Login Successful",
                        Toast.LENGTH_SHORT
                ).show();

                Intent i = new Intent(
                        MainActivity.this,
                        HomeActivity.class
                );

                i.putExtra("username", user);
                startActivity(i);

            } else {

                Toast.makeText(
                        MainActivity.this,
                        "Login Failed",
                        Toast.LENGTH_SHORT
                ).show();
            }
        });
    }
}
