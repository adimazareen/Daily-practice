# Android Spinner Application

A simple Android application demonstrating how to display a list of cities using a `Spinner` component.

## 📱 Description

This project demonstrates how to create and populate a Spinner in Android using Java and XML.

The application displays a dropdown list containing the following cities:

- Mumbai
- Pune
- Delhi
- Hyderabad
- Bangalore

When the user selects a city, a Toast message displays the selected city.

The city names are stored in `strings.xml` using a string array. An `ArrayAdapter` connects the array to the Spinner.

## 🛠️ Technologies Used

- Java
- XML
- Android Studio
- Spinner
- ArrayAdapter
- String Array Resources
- Toast
- ConstraintLayout
- AppCompatActivity

## 📂 Project Structure

```text
SpinnerApp/
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
            │   └── com/bcs/spinner_6/
            │       └── MainActivity.java
            │
            └── res/
                ├── layout/
                │   └── activity_main.xml
                │
                └── values/
                    ├── strings.xml
                    ├── colors.xml
                    └── themes.xml
```

## 🎯 Concepts Covered

### 1. Spinner

A `Spinner` displays a dropdown list from which the user can select one item.

```xml
<Spinner
    android:id="@+id/spinnerCities"
    android:layout_width="match_parent"
    android:layout_height="wrap_content" />
```

### 2. String Array

The city names are stored as a string array in `strings.xml`.

```xml
<string-array name="city_names">
    <item>Mumbai</item>
    <item>Pune</item>
    <item>Delhi</item>
    <item>Hyderabad</item>
    <item>Bangalore</item>
</string-array>
```

### 3. ArrayAdapter

`ArrayAdapter` connects the city array to the Spinner.

```java
ArrayAdapter<CharSequence> adapter =
        ArrayAdapter.createFromResource(
                this,
                R.array.city_names,
                android.R.layout.simple_spinner_item
        );

adapter.setDropDownViewResource(
        android.R.layout.simple_spinner_dropdown_item
);

spinnerCities.setAdapter(adapter);
```

### 4. Item Selection Listener

`OnItemSelectedListener` detects when a city is selected.

```java
spinnerCities.setOnItemSelectedListener(
    new AdapterView.OnItemSelectedListener() {

        @Override
        public void onItemSelected(
                AdapterView<?> parent,
                View view,
                int position,
                long id) {

            String selectedCity =
                    parent.getItemAtPosition(position).toString();

            Toast.makeText(
                    MainActivity.this,
                    "Selected: " + selectedCity,
                    Toast.LENGTH_SHORT
            ).show();
        }

        @Override
        public void onNothingSelected(AdapterView<?> parent) {
        }
    }
);
```

### 5. Toast Message

A Toast displays the selected city.

Example:

```text
Selected: Bangalore
```

## 🖼️ Expected Output

### Spinner Dropdown

```text
┌──────────────────────────────────┐
│                                  │
│  Mumbai                          │
│  Pune                            │
│  Delhi                           │
│  Hyderabad                       │
│  Bangalore                       │
│                                  │
└──────────────────────────────────┘
```

### Selected City

When the user selects Bangalore, the Spinner displays the selected city.

```text
Selected: Bangalore
```

## ▶️ How to Run

1. Open the project in Android Studio.
2. Allow Gradle to sync.
3. Start an Android emulator or connect an Android device.
4. Click **Run**.
5. Tap the Spinner dropdown.
6. Select a city from the list.
7. Verify that the selected city appears in the Spinner and a Toast message is displayed.

**Note:** Android may trigger the selection listener for the initial Spinner selection when the screen opens, so a Toast can appear before the user makes a new selection.

## 📚 Learning Objective

The objective of this practical is to understand how to create a Spinner, define string array resources, populate a dropdown using `ArrayAdapter`, handle item selection events, and display Toast messages in Android.

## 👩‍💻 Author

Adima Zareen
