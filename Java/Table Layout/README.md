# TableLayout Android App

A simple Android application demonstrating the use of `TableLayout` and `TableRow` to display data in a tabular format.

## 📱 Description

This project demonstrates how to create a table-based user interface using Android's `TableLayout`.

The application displays a list of students with their:

* ID
* Name

The table contains a header row and four data rows.

## 🛠️ Technologies Used

* Java
* XML
* Android Studio
* TableLayout
* TableRow
* TextView
* RelativeLayout

## 📂 Project Structure

```text
TableLayoutDemo/
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
            │   └── com/example/tablelayout/
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

## 🎯 Concepts Covered

### TableLayout

`TableLayout` is used to arrange UI elements in rows and columns.

```xml
<TableLayout>
```

### TableRow

Each row of the table is created using:

```xml
<TableRow>
```

Each `TableRow` contains multiple `TextView` elements representing individual cells.

### Stretch Columns

The following property makes column 2 stretch to occupy available space:

```xml
android:stretchColumns="1"
```

The index starts from `0`, so:

* Column 0 = ID
* Column 1 = Name

### Table Header

The first `TableRow` is used as the table header:

```text
ID | Name
```

The header uses bold text and a darker background.

### Data Rows

The application displays four data rows:

```text
4  | Adima
29 | Bushra
34 | Sofiya
57 | Samaira
```

### RelativeLayout

The `TableLayout` is placed inside a `RelativeLayout` and centered using:

```xml
android:layout_centerInParent="true"
```

## 🖼️ Expected Output

```text
┌─────────────────────────┐
│       ID    |   Name    │
├─────────────────────────┤
│        4    |   Adima   │
│       29    |   Bushra  │
│       34    |   Sofiya  │
│       57    |   Samaira │
└─────────────────────────┘
```

## ▶️ How to Run

1. Open the project in Android Studio.
2. Allow Gradle to sync.
3. Start an Android emulator or connect an Android device.
4. Click the **Run** button.
5. The table will be displayed on the screen.

## 📚 Learning Objective

The objective of this practical is to understand how `TableLayout` and `TableRow` can be used to arrange information in rows and columns in an Android application.

## 👩‍💻 Author

Adima
