package com.bcs.loginscreen_2;

import android.os.Bundle;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

public class HomeActivity extends AppCompatActivity {

    TextView txtWelcome;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        setContentView(R.layout.activity_home);

        txtWelcome = findViewById(R.id.txtWelcome);

        String username =
                getIntent().getStringExtra("username");

        txtWelcome.setText("Welcome, " + username + "!");
    }
}
