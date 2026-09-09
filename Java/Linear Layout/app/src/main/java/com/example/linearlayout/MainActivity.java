package com.example.linearlayout;

import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    EditText txtTo, txtSub, txtMsg;
    Button btnSend;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        setContentView(R.layout.activity_main);

        // Connect XML views with Java
        txtTo = findViewById(R.id.txtTo);
        txtSub = findViewById(R.id.txtSub);
        txtMsg = findViewById(R.id.txtMsg);
        btnSend = findViewById(R.id.btnSend);

        // Send button click event
        btnSend.setOnClickListener(v -> {

            String to = txtTo.getText().toString();
            String subject = txtSub.getText().toString();
            String message = txtMsg.getText().toString();

            if (to.isEmpty() || subject.isEmpty() || message.isEmpty()) {

                Toast.makeText(
                        MainActivity.this,
                        "Please fill all fields",
                        Toast.LENGTH_SHORT
                ).show();

            } else {

                Toast.makeText(
                        MainActivity.this,
                        "Message sent to " + to,
                        Toast.LENGTH_LONG
                ).show();
            }
        });
    }
}
