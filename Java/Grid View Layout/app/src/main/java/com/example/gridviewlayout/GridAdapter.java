package com.example.gridviewlayout;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.ImageView;
import android.widget.TextView;

public class GridAdapter extends BaseAdapter {

    private Context context;
    private String[] fruitNames;
    private int[] fruitImages;
    private LayoutInflater inflater;

    public GridAdapter(
            Context context,
            String[] fruitNames,
            int[] fruitImages) {

        this.context = context;
        this.fruitNames = fruitNames;
        this.fruitImages = fruitImages;

        inflater = LayoutInflater.from(context);
    }

    @Override
    public int getCount() {
        return fruitNames.length;
    }

    @Override
    public Object getItem(int position) {
        return fruitNames[position];
    }

    @Override
    public long getItemId(int position) {
        return position;
    }

    @Override
    public View getView(
            int position,
            View convertView,
            ViewGroup parent) {

        if (convertView == null) {
            convertView = inflater.inflate(
                    R.layout.grid_item,
                    parent,
                    false
            );
        }

        ImageView imageView =
                convertView.findViewById(R.id.imageView);

        TextView textView =
                convertView.findViewById(R.id.textView);

        imageView.setImageResource(
                fruitImages[position]
        );

        textView.setText(
                fruitNames[position]
        );

        return convertView;
    }
}
