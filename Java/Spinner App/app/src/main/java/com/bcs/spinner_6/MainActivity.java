package com.bcs.spinner_6;

import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Spinner;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    Spinner spinnerCities;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        spinnerCities = findViewById(R.id.spinnerCities);

        // Create an adapter using the city array in strings.xml
        ArrayAdapter<CharSequence> adapter =
                ArrayAdapter.createFromResource(
                        this,
                        R.array.city_names,
                        android.R.layout.simple_spinner_item
                );

        // Set the dropdown item layout
        adapter.setDropDownViewResource(
                android.R.layout.simple_spinner_dropdown_item
        );

        // Attach the adapter to the Spinner
        spinnerCities.setAdapter(adapter);

        // Handle city selection
        spinnerCities.setOnItemSelectedListener(
                new AdapterView.OnItemSelectedListener() {

                    @Override
                    public void onItemSelected(
                            AdapterView<?> parent,
                            View view,
                            int position,
                            long id) {

                        String selectedCity =
                                parent.getItemAtPosition(position)
                                        .toString();

                        Toast.makeText(
                                MainActivity.this,
                                "Selected: " + selectedCity,
                                Toast.LENGTH_SHORT
                        ).show();
                    }

                    @Override
                    public void onNothingSelected(
                            AdapterView<?> parent) {
                    }
                }
        );
    }
}
