# Android Basic Calculator App

A simple Android application demonstrating how to create a basic calculator using `Button`, `EditText`, `GridLayout`, and Java click event handling.

## 📱 Description

This application demonstrates a basic calculator Activity where the user can perform arithmetic operations.

The calculator provides buttons for:

- Numbers 0–9
- Addition (+)
- Subtraction (-)
- Multiplication (×)
- Division (÷)
- Modulus (%)
- Clear (C)
- Backspace (⌫)
- Equal (=)

The calculator uses a `GridLayout` with four columns to arrange the buttons.

The application takes two numbers and performs the selected arithmetic operation when the `=` button is pressed.

## 🛠️ Technologies Used

- Java
- XML
- Android Studio
- LinearLayout
- GridLayout
- EditText
- Button
- TextView
- Event Handling
- Arithmetic Operations

## 📂 Project Structure

```text
CalculatorApp/
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
            │   └── com/example/calculator/
            │       └── MainActivity.java
            │
            └── res/
                ├── layout/
                │   └── activity_main.xml
                │
                ├── values/
                │   ├── strings.xml
                │   ├── colors.xml
                │   ├── styles.xml
                │   └── themes.xml
                │
                └── mipmap-*/
                    └── app icons
```

## 🎯 Concepts Covered

### 1. EditText

`EditText` is used to display the entered numbers and the calculation result.

```xml
<EditText
    android:id="@+id/editText"
    android:layout_width="match_parent"
    android:layout_height="wrap_content" />
```

### 2. GridLayout

`GridLayout` is used to arrange the calculator buttons in four columns.

```xml
<GridLayout
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:columnCount="4">
```

### 3. Button Click Events

Each button calls a specific Java method using the `android:onClick` attribute.

```xml
<Button
    android:text="7"
    android:onClick="onDigitClick" />
```

### 4. Digit Input

The `onDigitClick()` method adds the selected number to the current input.

```java
public void onDigitClick(View view) {

    Button button = (Button) view;

    input += button.getText().toString();

    editText.setText(input);
}
```

### 5. Arithmetic Operators

The calculator supports the following operations:

```text
+
-
×
÷
%
```

The selected operator is stored until the user enters the second number and presses `=`.

### 6. Equal Button

The `onEqualClick()` method performs the selected arithmetic operation.

```java
switch (operator) {

    case "+":
        result = num1 + num2;
        break;

    case "-":
        result = num1 - num2;
        break;

    case "×":
        result = num1 * num2;
        break;

    case "÷":
        result = num1 / num2;
        break;

    case "%":
        result = num1 % num2;
        break;
}
```

### 7. Clear Button

The `C` button clears the entered input and selected operator.

```java
public void onClearClick(View view) {

    input = "";
    operator = "";

    editText.setText("");
}
```

### 8. Backspace Button

The `⌫` button removes the last entered digit.

```java
public void onBackspaceClick(View view) {

    if (!input.isEmpty()) {

        input = input.substring(
                0,
                input.length() - 1
        );

        editText.setText(input);
    }
}
```

## 🖼️ Expected Output

```text
┌──────────────────────────────────┐
│                                  │
│                                  │
│       Calculator Display         │
│                                  │
│       Enter text here            │
│                                  │
│   ┌─────┬─────┬─────┬─────┐      │
│   │  7  │  8  │  9  │  ÷  │      │
│   ├─────┼─────┼─────┼─────┤      │
│   │  4  │  5  │  6  │  ×  │      │
│   ├─────┼─────┼─────┼─────┤      │
│   │  1  │  2  │  3  │  -  │      │
│   ├─────┼─────┼─────┼─────┤      │
│   │  C  │  0  │  =  │  +  │      │
│   ├─────┼─────┼─────┼─────┤      │
│   │  %  │  ⌫ │     │     │      │
│   └─────┴─────┴─────┴─────┘      │
│                                  │
│       Adima Zareen's Calculator  │
│                                  │
└──────────────────────────────────┘
```

## ▶️ How to Run

1. Open the project in Android Studio.
2. Allow Gradle to sync.
3. Start an Android emulator or connect an Android device.
4. Click **Run**.
5. Enter the first number using the calculator buttons.
6. Select an arithmetic operator.
7. Enter the second number.
8. Press `=` to display the result.
9. Use `C` to clear the calculator.
10. Use `⌫` to remove the last entered digit.

## 📚 Learning Objective

The objective of this practical is to understand how to create a basic calculator Activity in Android and handle button click events to perform arithmetic operations.

## 👩‍💻 Author

**Adima Zareen**
