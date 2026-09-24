package com.example.gridviewlayout;

import android.os.Bundle;
import android.widget.GridView;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    private GridView gridView;

    private String[] fruitNames = {
            "Apple",
            "Banana",
            "Cherry",
            "Grapes",
            "Mango",
            "Orange"
    };

    private int[] fruitImages = {
            R.drawable.apple,
            R.drawable.banana,
            R.drawable.cherry,
            R.drawable.grapes,
            R.drawable.mango,
            R.drawable.orange
    };

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        setContentView(R.layout.activity_main);

        gridView = findViewById(R.id.gridView);

        GridAdapter adapter =
                new GridAdapter(
                        this,
                        fruitNames,
                        fruitImages
                );

        gridView.setAdapter(adapter);
    }
}
