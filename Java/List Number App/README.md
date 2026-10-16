# Android List Display Application

A simple Android application demonstrating how to pass a number between activities using an `Intent` and display the size of a sample list.

## 📱 Description

This project demonstrates how to create a two-screen Android application using Java and XML.

**Screen 1 — MainActivity**
- Accepts a number from the user.
- Validates the input.
- Passes the number to the next activity using an explicit `Intent`.

**Screen 2 — DisplayActivity**
- Receives the number from the previous screen.
- Displays the passed number.
- Creates a sample list of five fruits.
- Displays the total number of items in the list.

Sample list:
- Apple
- Banana
- Cherry
- Dates
- Elderberry

## 🛠️ Technologies Used

- Java
- XML
- Android Studio
- ConstraintLayout
- EditText
- Button
- TextView
- Intent
- Arrays and List
- Toast
- AppCompatActivity

## 📂 Project Structure

```text
ListNumberApp/
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
            │   └── com/bcs/list_number_5/
            │       ├── MainActivity.java
            │       └── DisplayActivity.java
            │
            └── res/
                ├── layout/
                │   ├── activity_main.xml
                │   └── activity_display.xml
                │
                ├── values/
                │   ├── strings.xml
                │   ├── colors.xml
                │   └── themes.xml
                │
                └── mipmap-*/
                    └── App icons
```

## 🎯 Concepts Covered

### 1. EditText

Accepts a number from the user.

```xml
<EditText
    android:id="@+id/etNumber"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:hint="Enter a number"
    android:inputType="number" />
```

### 2. Intent

Passes the entered number from `MainActivity` to `DisplayActivity`.

```java
Intent intent = new Intent(
    MainActivity.this,
    DisplayActivity.class
);

intent.putExtra("inputNumber", number);
startActivity(intent);
```

### 3. Receiving Data

The second activity retrieves the number using `getIntExtra()`.

```java
int passedNumber =
        getIntent().getIntExtra("inputNumber", 0);

tvPassed.setText("Passed number: " + passedNumber);
```

### 4. Creating a List

A sample list is created using `Arrays.asList()`.

```java
List<String> items = Arrays.asList(
    "Apple",
    "Banana",
    "Cherry",
    "Dates",
    "Elderberry"
);
```

### 5. Counting List Items

The `size()` method returns the number of elements in the list.

```java
int count = items.size();

tvListCount.setText(
    "Number of items in the list: " + count
);
```

## 🖼️ Expected Output

### Screen 1 — Input

```text
┌──────────────────────────────────┐
│                                  │
│             [ 3 ]                │
│                                  │
│            [ Next ]              │
│                                  │
└──────────────────────────────────┘
```

### Screen 2 — Result

```text
┌──────────────────────────────────┐
│                                  │
│          Passed number: 3        │
│                                  │
│    Number of items in the list: 5│
│                                  │
└──────────────────────────────────┘
```

If the input is empty or is outside the supported integer range, the application displays an error Toast.

## ▶️ How to Run

1. Open the project in Android Studio.
2. Allow Gradle to sync.
3. Start an Android emulator or connect an Android device.
4. Click **Run**.
5. Enter a number on the first screen.
6. Click **Next**.
7. Verify that the next screen displays the entered number and the list count of `5`.

## 📚 Learning Objective

The objective of this practical is to understand multiple Android activities, user input validation, explicit Intents, passing data between screens, creating a Java list, and counting list elements using `size()`.

## 👩‍💻 Author

Adima Zareen
