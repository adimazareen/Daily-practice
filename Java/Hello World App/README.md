# Android ConstraintLayout App

A simple Android application demonstrating how to design user interfaces using ConstraintLayout in Android Studio.

## 📱 Description

This application demonstrates how to arrange and position UI components using `ConstraintLayout` in Android development.

`ConstraintLayout` allows developers to create flexible and responsive layouts by defining relationships between UI components and the parent layout.

The application demonstrates:

- Creating a user interface using ConstraintLayout
- Positioning views using constraints
- Aligning components horizontally and vertically
- Setting layout width and height
- Using margins and spacing
- Designing responsive Android layouts using XML

## 🛠️ Technologies Used

- Java
- XML
- Android Studio
- ConstraintLayout
- TextView
- Button
- EditText
- Android SDK
- AppCompat

## 📂 Project Structure

```text
ConstraintLayoutApp/
│
├── README.md
├── .gitignore
├── build.gradle
├── settings.gradle
│
└── app/
    ├── build.gradle
    │
    └── src/
        └── main/
            ├── AndroidManifest.xml
            │
            ├── java/
            │   └── com/example/constraintlayoutapp/
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

### 1. ConstraintLayout

`ConstraintLayout` is used as the root layout to arrange UI components.

```xml
<androidx.constraintlayout.widget.ConstraintLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:layout_width="match_parent"
    android:layout_height="match_parent">

</androidx.constraintlayout.widget.ConstraintLayout>
```

### 2. Layout Width and Height

The `layout_width` and `layout_height` attributes define the dimensions of a view.

```xml
android:layout_width="wrap_content"
android:layout_height="wrap_content"
```

Common values include:

- `match_parent` — Occupies the available size of the parent.
- `wrap_content` — Sizes the view according to its content.
- `0dp` — In ConstraintLayout, matches the available space between the defined constraints when used for a constrained dimension.

### 3. Constraints

Constraints define the position of a view relative to its parent or another view.

```xml
app:layout_constraintTop_toTopOf="parent"
app:layout_constraintBottom_toBottomOf="parent"
app:layout_constraintStart_toStartOf="parent"
app:layout_constraintEnd_toEndOf="parent"
```

These constraints can center a view horizontally and vertically inside the parent when the view has suitable dimensions.

### 4. TextView

A `TextView` displays text on the screen.

```xml
<TextView
    android:id="@+id/txtMessage"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:text="Hello Android!"
    android:textSize="20sp"
    app:layout_constraintTop_toTopOf="parent"
    app:layout_constraintBottom_toBottomOf="parent"
    app:layout_constraintStart_toStartOf="parent"
    app:layout_constraintEnd_toEndOf="parent" />
```

### 5. Button

A `Button` allows the user to perform an action.

```xml
<Button
    android:id="@+id/btnSubmit"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:text="Submit"
    app:layout_constraintTop_toBottomOf="@id/txtMessage"
    app:layout_constraintStart_toStartOf="parent"
    app:layout_constraintEnd_toEndOf="parent" />
```

The button is positioned below the TextView using a constraint.

### 6. Margins and Spacing

Margins add space around a view to improve the layout.

```xml
android:layout_marginTop="16dp"
android:layout_marginStart="16dp"
```

The `dp` unit is used for layout dimensions and spacing, while `sp` is generally used for text sizes.

### 7. Positioning Views Relative to Other Views

A view can be positioned relative to another view using its ID.

```xml
app:layout_constraintTop_toBottomOf="@id/txtMessage"
```

This places the top of the current view below the bottom of `txtMessage`.

### 8. Responsive UI Design

ConstraintLayout helps create flexible layouts that adapt to different screen sizes and orientations.

Using appropriate constraints instead of fixed screen coordinates helps maintain a consistent layout across devices.

## 🖼️ Expected Output

The application displays a simple user interface with a centered text message and a button positioned below it.

```text
┌──────────────────────────────────┐
│                                  │
│                                  │
│                                  │
│                                  │
│          Hello Android!          │
│                                  │
│             [Submit]             │
│                                  │
│                                  │
│                                  │
└──────────────────────────────────┘
```

## ▶️ How to Run

1. Open the project in Android Studio.
2. Allow Gradle to sync successfully.
3. Open `activity_main.xml` to view the layout design.
4. Start an Android emulator or connect an Android device.
5. Click **Run** to launch the application.
6. Observe how the views are positioned using ConstraintLayout constraints.

## 📚 Learning Objective

The objective of this practical is to understand the basic working of ConstraintLayout and learn how to position, align, and arrange Android UI components using XML constraints.

## 👩‍💻 Author

**Adima Zareen**
