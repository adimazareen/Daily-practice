package com.bcs.login_url_4;

import android.content.ActivityNotFoundException;
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    EditText etUsername, etPassword;
    Button btnLogin;

    private static final String TARGET_URL =
            "https://www.wikipedia.org";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        setContentView(R.layout.activity_login);

        etUsername = findViewById(R.id.etUsername);
        etPassword = findViewById(R.id.etPassword);
        btnLogin = findViewById(R.id.btnLogin);

        btnLogin.setOnClickListener(view -> {

            String user =
                    etUsername.getText().toString().trim();

            String pass =
                    etPassword.getText().toString().trim();

            if (user.equals("admin") && pass.equals("1234")) {
                openBrowser(TARGET_URL);
            } else {
                Toast.makeText(
                        MainActivity.this,
                        "Login failed",
                        Toast.LENGTH_SHORT
                ).show();
            }
        });
    }

    private void openBrowser(String url) {
        try {
            Intent intent = new Intent(
                    Intent.ACTION_VIEW,
                    Uri.parse(url)
            );

            intent.addCategory(Intent.CATEGORY_BROWSABLE);

            startActivity(intent);

        } catch (ActivityNotFoundException e) {
            Toast.makeText(
                    this,
                    "No browser found to open the link.",
                    Toast.LENGTH_LONG
            ).show();
        }
    }
}
