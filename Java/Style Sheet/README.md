```markdown
# Android Style Sheet App

A simple Android application demonstrating how to design Android application components using reusable styles, themes, colors, and a custom drawable background.

## 📱 Description

This application demonstrates how styles can be created in Android and applied to different UI components.

The application contains:

- An `EditText` for entering text
- A styled `Button` for submitting the text
- A custom button background
- Custom colors
- Reusable styles
- A custom application theme

When the user enters text and clicks the **SUBMIT** button, the entered text is displayed in the EditText.

## 🛠️ Technologies Used

- Java
- XML
- Android Studio
- LinearLayout
- EditText
- Button
- TextView
- Styles
- Themes
- Colors
- Drawable
- Material Components
- Event Handling

## 📂 Project Structure

```text
StyleSheetDemo/
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
            │   └── com/example/stylesheet/
            │       └── MainActivity.java
            │
            └── res/
                ├── drawable/
                │   └── button_background.xml
                │
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

### 1. Styles

Styles are used to define common properties of UI components in one place.

```xml
<style name="MyButtonStyle"
    parent="Widget.MaterialComponents.Button">

    <item name="android:textColor">
        @color/white
    </item>

    <item name="android:textSize">
        18sp
    </item>

</style>
```

### 2. Applying a Style

The custom style is applied to the Button using the **`style`** attribute.

```xml
<Button
    android:id="@+id/button"
    style="@style/MyButtonStyle"
    android:text="SUBMIT" />
```

The EditText also uses a reusable style:

```xml
<EditText
    android:id="@+id/editText"
    style="@style/MyEditTextStyle"
    android:hint="Enter text" />
```

### 3. Custom Button Background

A separate drawable file called **`button_background.xml`** is used to define the background of the Submit button.

```text
res/drawable/button_background.xml
```

The drawable defines:

- Background color
- Rounded corners
- Padding

```xml
<shape
    xmlns:android="http://schemas.android.com/apk/res/android"
    android:shape="rectangle">

    <solid
        android:color="@color/brand_primary" />

    <corners
        android:radius="6dp" />

</shape>
```

### 4. Colors

Custom colors are stored in **`colors.xml`** so they can be reused throughout the application.

```xml
<color name="brand_primary">#6200EE</color>
<color name="brand_primary_variant">#3700B3</color>
<color name="brand_secondary">#03DAC6</color>
<color name="white">#FFFFFF</color>
<color name="black">#000000</color>
```

### 5. Theme

The application theme defines the primary and secondary colors used throughout the application.

```xml
<style name="Theme.StyleSheet"
    parent="Theme.Material3.Light.NoActionBar">

    <item name="colorPrimary">
        @color/brand_primary
    </item>

    <item name="colorSecondary">
        @color/brand_secondary
    </item>

</style>
```

### 6. Button Click Event

The **`MainActivity.java`** file handles the Submit button click.

```java
button.setOnClickListener(v -> {

    String input =
            editText.getText().toString();

    editText.setText(
            "You entered: " + input
    );
});
```

When the user clicks **SUBMIT**, the entered text is displayed in the EditText.

## 🖼️ Expected Output

```text
┌──────────────────────────────────┐
│                                  │
│          Style Sheet             │
│                                  │
│                                  │
│                                  │
│                                  │
│     Enter text                   │
│     ───────────────────────      │
│                                  │
│             SUBMIT               │
│                                  │
│                                  │
│                                  │
└──────────────────────────────────┘
```

The application uses a purple styled button and a teal-colored EditText underline/background based on the defined styles and colors.

## ▶️ How to Run

1. Open the project in Android Studio.
2. Allow Gradle to sync.
3. Start an Android emulator or connect an Android device.
4. Click **Run**.
5. Enter text in the EditText.
6. Click the **SUBMIT** button.
7. The entered text will be displayed in the EditText.

## 📚 Learning Objective

The objective of this practical is to understand how Android styles, themes, colors, and drawable resources can be created and reused to design consistent application components.

## 👩‍💻 Author

**Adima Zareen**
```
