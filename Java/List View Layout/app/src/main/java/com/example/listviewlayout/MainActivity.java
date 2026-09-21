package com.example.listviewlayout;

import android.os.Bundle;
import android.widget.ArrayAdapter;
import android.widget.ListView;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    private ListView listView;

    private String[] sampleItems = {
            "Adima",
            "Khadija",
            "Samaira",
            "Mehvish",
            "Umama",
            "Sumera",
            "Aram",
            "Rana",
            "Sofiya",
            "Rutuja"
    };

    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);

        setContentView(R.layout.activity_main);

        // Initialize ListView
        listView = findViewById(R.id.listView);

        // Set up ArrayAdapter
        ArrayAdapter<String> adapter =
                new ArrayAdapter<>(
                        this,
                        R.layout.list_item,
                        sampleItems
                );

        // Set adapter to ListView
        listView.setAdapter(adapter);
    }
}
