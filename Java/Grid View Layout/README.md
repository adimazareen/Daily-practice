# GridView Layout Android App

A simple Android application demonstrating how to create a `GridView` layout and display multiple items in a two-column grid using a custom `BaseAdapter`.

## 📱 Description

This application demonstrates a fruit grid where each item contains an image and the corresponding fruit name.

The application displays the following fruits:

* Apple
* Banana
* Cherry
* Grapes
* Mango
* Orange

A custom XML layout is used for each GridView item, and `GridAdapter.java` is used to connect the fruit data with the GridView.

## 🛠️ Technologies Used

* Java
* XML
* Android Studio
* GridView
* BaseAdapter
* ImageView
* TextView
* LinearLayout
* LayoutInflater

## 📂 Project Structure

```text
GridViewLayoutDemo/
│
├── README.md
├── .gitignore
│
└── app/
    ├── build.gradle
    │
    └── src/
        └── main/
            ├── AndroidManifest.xml
            │
            ├── java/
            │   └── com/example/gridviewlayout/
            │       ├── MainActivity.java
            │       └── GridAdapter.java
            │
            └── res/
                ├── drawable/
                │   ├── apple.png
                │   ├── banana.png
                │   ├── cherry.png
                │   ├── grapes.png
                │   ├── mango.png
                │   └── orange.png
                │
                ├── layout/
                │   ├── activity_main.xml
                │   └── grid_item.xml
                │
                ├── values/
                │   ├── strings.xml
                │   ├── colors.xml
                │   └── themes.xml
                │
                └── mipmap-*/
                    └── app icons
```

## 🎯 Concepts Covered

### 1. GridView

`GridView` is used to display items in a two-dimensional grid.

```xml
<GridView
    android:id="@+id/gridView"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:numColumns="2" />
```

The `numColumns="2"` attribute arranges the fruits into two columns.

### 2. BaseAdapter

A custom `BaseAdapter` is used to connect the fruit names and images with the GridView.

```java
GridAdapter adapter =
        new GridAdapter(
                this,
                fruitNames,
                fruitImages
        );
```

### 3. Custom Grid Item

A separate XML file called `grid_item.xml` is used to define the appearance of each GridView item.

```text
res/layout/grid_item.xml
```

Each item contains:

* `ImageView` for displaying the fruit image
* `TextView` for displaying the fruit name

### 4. Setting the Adapter

The adapter is attached to the GridView using:

```java
gridView.setAdapter(adapter);
```

### 5. Sample Data

The application uses an array containing the fruit names:

```java
String[] fruitNames = {
    "Apple",
    "Banana",
    "Cherry",
    "Grapes",
    "Mango",
    "Orange"
};
```

The corresponding images are stored in the `drawable` folder:

```java
int[] fruitImages = {
    R.drawable.apple,
    R.drawable.banana,
    R.drawable.cherry,
    R.drawable.grapes,
    R.drawable.mango,
    R.drawable.orange
};
```

### 6. Custom GridAdapter

The `GridAdapter.java` class extends `BaseAdapter` and provides the appropriate image and name for each GridView position.

```java
public class GridAdapter extends BaseAdapter {

    @Override
    public int getCount() {
        return fruitNames.length;
    }

    @Override
    public View getView(
            int position,
            View convertView,
            ViewGroup parent) {

        // Set fruit image
        // Set fruit name

        return convertView;
    }
}
```

## 🖼️ Expected Output

```text
┌──────────────────────────────────┐
│                                  │
│           Fruits Grid            │
│                                  │
│       🍎              🍌        │
│      Apple          Banana       │
│                                  │
│       🍒              🍇        │
│      Cherry          Grapes      │
│                                  │
│       🥭              🍊        │
│      Mango           Orange      │
│                                  │
└──────────────────────────────────┘
```

The actual application displays fruit images instead of the emoji representations shown above.

## ▶️ How to Run

1. Open the project in Android Studio.
2. Allow Gradle to sync.
3. Make sure all six fruit images are placed inside the `drawable` folder.
4. Start an Android emulator or connect an Android device.
5. Click **Run**.
6. The **Fruits Grid** will be displayed with two columns.

## 📚 Learning Objective

The objective of this practical is to understand how `GridView` works and how a custom `BaseAdapter` can be used to display images and text in a grid-based Android layout.

## 👩‍💻 Author

Adima
