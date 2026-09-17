package com.example.uicomponents;

import android.os.Bundle;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.AutoCompleteTextView;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.EditText;
import android.widget.RadioButton;
import android.widget.RadioGroup;
import android.widget.RatingBar;
import android.widget.Toast;
import android.widget.ToggleButton;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    EditText editText;
    RadioGroup radioGroup;
    ToggleButton toggleButton;
    CheckBox checkBox;
    RatingBar ratingBar;
    AutoCompleteTextView autoCompleteTextView;
    Button submitButton;

    String[] countries = {
            "India",
            "USA",
            "Canada",
            "Australia",
            "Germany",
            "France",
            "Japan"
    };

    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);

        setContentView(R.layout.activity_main);

        // Initialize UI components
        editText = findViewById(R.id.editText);
        radioGroup = findViewById(R.id.radioGroup);
        toggleButton = findViewById(R.id.toggleButton);
        checkBox = findViewById(R.id.checkBox);
        ratingBar = findViewById(R.id.ratingBar);
        autoCompleteTextView =
                findViewById(R.id.autoCompleteTextView);
        submitButton = findViewById(R.id.submitButton);

        // Set up AutoCompleteTextView
        ArrayAdapter<String> adapter =
                new ArrayAdapter<>(
                        this,
                        android.R.layout.simple_dropdown_item_1line,
                        countries
                );

        autoCompleteTextView.setAdapter(adapter);

        // Submit button action
        submitButton.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View v) {

                // Get user input values
                String name =
                        editText.getText().toString().trim();

                int selectedRadioId =
                        radioGroup.getCheckedRadioButtonId();

                RadioButton selectedRadioButton = null;

                if (selectedRadioId != -1) {
                    selectedRadioButton =
                            findViewById(selectedRadioId);
                }

                String gender =
                        selectedRadioButton != null
                                ? selectedRadioButton.getText().toString()
                                : "Not selected";

                boolean notifications =
                        toggleButton.isChecked();

                boolean termsAccepted =
                        checkBox.isChecked();

                float rating =
                        ratingBar.getRating();

                String country =
                        autoCompleteTextView
                                .getText()
                                .toString()
                                .trim();

                // Display the results
                String message =
                        "Name: " + name + "\n" +
                        "Gender: " + gender + "\n" +
                        "Notifications: " +
                        (notifications ? "ON" : "OFF") + "\n" +
                        "Terms Accepted: " +
                        (termsAccepted ? "Yes" : "No") + "\n" +
                        "Rating: " + rating + "\n" +
                        "Country: " + country;

                Toast.makeText(
                        MainActivity.this,
                        message,
                        Toast.LENGTH_LONG
                ).show();
            }
        });
    }
}
