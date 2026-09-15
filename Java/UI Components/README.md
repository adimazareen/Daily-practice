# Android UI Components Demo

A simple Android application demonstrating different Android UI components using XML and Java.

## 📱 Description

This application demonstrates the following Android UI components:

* TextView
* EditText
* RadioButton
* ToggleButton
* CheckBox
* RatingBar
* AutoCompleteTextView
* MaterialButton

The user can enter their name, select a gender, enable or disable notifications, accept terms and conditions, provide a rating, select a country, and submit the information.

The entered information is displayed using a Toast message.

## 🛠️ Technologies Used

* Java
* XML
* Android Studio
* Android SDK
* Material Design Components

## 📂 Project Structure

```text
UIComponentsDemo/
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
            │   └── com/example/uicomponents/
            │       └── MainActivity.java
            │
            └── res/
                ├── layout/
                │   └── activity_main.xml
                │
                ├── values/
                │   ├── strings.xml
                │   ├── colors.xml
                │   └── themes.xml
                │
                └── mipmap-*/
                    └── app icons
```

## 🎯 UI Components Covered

### 1. TextView

Used to display the heading:

```xml
<TextView />
```

### 2. EditText

Used to accept the user's name:

```xml
<EditText />
```

### 3. RadioButton

Radio buttons allow the user to select one option from a group.

```xml
<RadioGroup>
    <RadioButton />
    <RadioButton />
</RadioGroup>
```

### 4. ToggleButton

Used to turn notifications ON or OFF.

```xml
<ToggleButton />
```

### 5. CheckBox

Used to accept terms and conditions:

```xml
<CheckBox />
```

### 6. RatingBar

Allows the user to provide a rating from 1 to 5 stars:

```xml
<RatingBar />
```

### 7. AutoCompleteTextView

Provides country suggestions while the user types.

Example:

```text
India
USA
Canada
Australia
Germany
France
Japan
```

### 8. MaterialButton

Used as the Submit button:

```xml
<com.google.android.material.button.MaterialButton />
```

## ⚙️ Functionality

When the user presses the Submit button, the application collects:

* Name
* Gender
* Notification status
* Terms acceptance
* Rating
* Country

The collected information is displayed using a Toast message.

## 📚 Learning Objective

The objective of this practical is to understand and implement commonly used Android UI components and handle their values using Java.

## ▶️ How to Run

1. Open the project in Android Studio.
2. Allow Gradle to sync.
3. Start an Android emulator or connect an Android device.
4. Click **Run**.
5. Enter the required information.
6. Click **Submit**.

## 🖼️ Expected Output

```text
┌──────────────────────────────────┐
│   Learn UI Components with       │
│           Adima                  │
│                                  │
│   Enter your name                │
│                                  │
│   ○ Male      ○ Female           │
│                                  │
│   [ Notifications OFF ]          │
│                                  │
│   ☑ Accept Terms and Conditions  │
│                                  │
│   ☆ ☆ ☆ ☆ ☆                      │
│                                  │
│   Choose a country               │
│                                  │
│   [           Submit           ] │
│                                  │
└──────────────────────────────────┘
```

## 👩‍💻 Author

Adima
