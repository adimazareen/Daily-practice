# Android Button Click - Login Activity

A simple Android application demonstrating how to handle a button click event using a Login Activity.

## 📱 Description

This application contains a simple login screen where the user can enter:

* Email
* Password

When the user clicks the **Login** button, the application validates the input fields.

If either field is empty, an error message is displayed using a Toast.

If both fields are filled, a success message is displayed on the screen and a Toast confirms that the login was successful.

## 🛠️ Technologies Used

* Java
* XML
* Android Studio
* LinearLayout
* EditText
* Button
* TextView
* Toast
* OnClickListener

## 📂 Project Structure

```text
ButtonClickDemo/
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
            │   └── com/example/buttonclick/
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

### 1. Button

A Button is used to trigger an action when the user clicks it.

```xml
<Button
    android:id="@+id/btnLogin"
    android:text="Login" />
```

### 2. OnClickListener

Java's `OnClickListener` is used to detect the button click:

```java
btnLogin.setOnClickListener(new View.OnClickListener() {

    @Override
    public void onClick(View v) {
        // Login logic
    }
});
```

### 3. EditText

`EditText` allows the user to enter information.

The email field uses:

```xml
android:inputType="textEmailAddress"
```

The password field uses:

```xml
android:inputType="textPassword"
```

### 4. Input Validation

The application checks whether the email or password is empty:

```java
if (email.isEmpty() || password.isEmpty()) {
    // Display error
}
```

### 5. Toast

A Toast displays a short message to the user:

```java
Toast.makeText(
    MainActivity.this,
    "Login Successful!",
    Toast.LENGTH_SHORT
).show();
```

### 6. TextView Visibility

The success message is initially hidden:

```xml
android:visibility="gone"
```

After successful login, it becomes visible:

```java
tvMessage.setVisibility(View.VISIBLE);
```

## 🖼️ Expected Output

```text
┌──────────────────────────────────┐
│                                  │
│          Login Please            │
│                                  │
│  Enter Email                     │
│  ──────────────────────────────  │
│                                  │
│  Enter Password                  │
│  ──────────────────────────────  │
│                                  │
│  ┌────────────────────────────┐  │
│  │            Login           │  │
│  └────────────────────────────┘  │
│                                  │
│                                  │
│                                  │
└──────────────────────────────────┘
```

## ▶️ How to Run

1. Open the project in Android Studio.
2. Allow Gradle to sync.
3. Start an Android emulator or connect an Android device.
4. Click **Run**.
5. Enter an email and password.
6. Click **Login**.
7. The application will display the appropriate message.

## 📚 Learning Objective

The objective of this practical is to understand how to handle button click events in Android using `OnClickListener`, perform basic input validation, and update a `TextView` dynamically.

## 👩‍💻 Author

Adima
