# ListView Layout Android App

A simple Android application demonstrating the use of `ListView` and `ArrayAdapter` to display a list of items.

## 📱 Description

This project demonstrates how to create and populate a `ListView` in Android.

The application displays a list of names:

* Adima
* Khadija
* Samaira
* Mehvish
* Umama
* Sumera
* Aram
* Rana
* Sofiya
* Rutuja

A custom XML layout is used for displaying each individual item in the ListView.

## 🛠️ Technologies Used

* Java
* XML
* Android Studio
* ListView
* ArrayAdapter
* TextView
* RelativeLayout

## 📂 Project Structure

```text
ListViewLayoutDemo/
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
            │   └── com/example/listviewlayout/
            │       └── MainActivity.java
            │
            └── res/
                ├── layout/
                │   ├── activity_main.xml
                │   └── list_item.xml
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

### 1. ListView

`ListView` is used to display a vertically scrolling list of items.

```xml
<ListView
    android:id="@+id/listView" />
```

### 2. ArrayAdapter

`ArrayAdapter` connects the array of data with the ListView.

```java
ArrayAdapter<String> adapter =
        new ArrayAdapter<>(
                this,
                R.layout.list_item,
                sampleItems
        );
```

### 3. Custom List Item

A separate XML file called `list_item.xml` is used to define the appearance of each item.

```text
res/layout/list_item.xml
```

### 4. Setting the Adapter

The adapter is attached to the ListView using:

```java
listView.setAdapter(adapter);
```

### 5. Sample Data

The application uses an array of names:

```java
String[] sampleItems = {
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
```

## 🖼️ Expected Output

```text
┌──────────────────────────────────┐
│  Adima                           │
├──────────────────────────────────┤
│  Khadija                         │
├──────────────────────────────────┤
│  Samaira                         │
├──────────────────────────────────┤
│  Mehvish                         │
├──────────────────────────────────┤
│  Umama                           │
├──────────────────────────────────┤
│  Sumera                          │
├──────────────────────────────────┤
│  Aram                            │
├──────────────────────────────────┤
│  Rana                            │
├──────────────────────────────────┤
│  Sofiya                          │
├──────────────────────────────────┤
│  Rutuja                          │
└──────────────────────────────────┘
```

## ▶️ How to Run

1. Open the project in Android Studio.
2. Allow Gradle to sync.
3. Start an Android emulator or connect an Android device.
4. Click **Run**.
5. The list of names will be displayed on the screen.

## 📚 Learning Objective

The objective of this practical is to understand how `ListView` works and how an `ArrayAdapter` can be used to display an array of data in a scrolling list.

## 👩‍💻 Author

Adima
