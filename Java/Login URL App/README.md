# Android Login Application with URL Opening

A simple Android application demonstrating username and password validation and opening a website in the device's external browser after successful login.

## 📱 Description

This application demonstrates how to create a basic login screen using Java and XML.

The application provides:

- A username input field
- A password input field with hidden characters
- A Login button to validate credentials
- A Toast message displaying **"Login failed"** when credentials are incorrect
- Automatic opening of a website in the external browser after successful login
- Error handling when no browser is available

**Demo Credentials:**

- Username: `admin`
- Password: `1234`

**Target URL:** **`https://www.wikipedia.org`**

The application uses `ConstraintLayout` to arrange the UI components and an explicit login condition to decide whether to open the browser. An **`Intent`** with **`ACTION_VIEW`** launches the URL in a browser.

## 🛠️ Technologies Used

- Java
- XML
- Android Studio
- ConstraintLayout
- EditText
- TextView
- Button
- Toast
- Intent
- Uri
- ActivityNotFoundException
- AppCompat

## 📂 Project Structure

```text
LoginUrlApp/
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
            │   └── com/bcs/login_url_4/
            │       └── MainActivity.java
            │
            └── res/
                ├── layout/
                │   └── activity_login.xml
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

**`ConstraintLayout`** arranges the username field, password field, and Login button.

```xml
<androidx.constraintlayout.widget.ConstraintLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:layout_width="match_parent"
    android:layout_height="match_parent">
</androidx.constraintlayout.widget.ConstraintLayout>
```

### 2. EditText

**`EditText`** accepts the username and password entered by the user.

**Username field:**

```xml
<EditText
    android:id="@+id/etUsername"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:hint="Username"
    android:inputType="text" />
```

**Password field:**

```xml
<EditText
    android:id="@+id/etPassword"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:hint="Password"
    android:inputType="textPassword" />
```

The **`textPassword`** input type hides password characters while typing.

### 3. Username and Password Validation

The application checks whether the entered credentials match the predefined demo credentials.

```java
if (user.equals("admin") && pass.equals("1234")) {
    openBrowser(TARGET_URL);
} else {
    Toast.makeText(
        MainActivity.this,
        "Login failed",
        Toast.LENGTH_SHORT
    ).show();
}
```

Both the username and password must match for the login to succeed.

### 4. Intent and Uri

An implicit **`Intent`** with **`ACTION_VIEW`** opens the specified URL using an application capable of handling web links.

```java
Intent intent = new Intent(
    Intent.ACTION_VIEW,
    Uri.parse(TARGET_URL)
);

intent.addCategory(Intent.CATEGORY_BROWSABLE);
startActivity(intent);
```

- **`Intent.ACTION_VIEW`** requests an application to display the URL.
- **`Uri.parse()`** converts the URL string into a **`Uri`**.
- **`Intent.CATEGORY_BROWSABLE`** indicates that the link can be opened by a browsing application.
- **`startActivity()`** launches the selected application.

### 5. Opening a Website

The target website is defined as a constant in **`MainActivity.java`**.

```java
private static final String TARGET_URL =
        "https://www.wikipedia.org";
```

You can replace this URL with another website by changing the value of **`TARGET_URL`**.

### 6. Toast Message

A Toast displays a short message when the login credentials are incorrect.

```java
Toast.makeText(
    MainActivity.this,
    "Login failed",
    Toast.LENGTH_SHORT
).show();
```

### 7. Exception Handling

**`ActivityNotFoundException`** handles the situation in which Android cannot find an application to open the URL.

```java
try {
    Intent intent = new Intent(
        Intent.ACTION_VIEW,
        Uri.parse(TARGET_URL)
    );

    intent.addCategory(Intent.CATEGORY_BROWSABLE);
    startActivity(intent);

} catch (ActivityNotFoundException e) {
    Toast.makeText(
        this,
        "No browser found to open the link.",
        Toast.LENGTH_LONG
    ).show();
}
```

## 🖼️ Expected Output

### Login Screen

```text
┌──────────────────────────────────┐
│                                  │
|                                  |
│  Username   [ admin           ]  │
│                                  │
│  Password   [ ••••            ]  │
│                                  │
|                                  |
|                                  |
│             [ Login ]            │
|                                  |
│                                  │
└──────────────────────────────────┘
```

### Successful Login

Enter:

- Username: **`admin`**
- Password: **`1234`**

**Result:** The device opens the target website in an external browser.

### Failed Login

Enter an incorrect username or password.

**Toast message:**

```text
Login failed
```

## ▶️ How to Run

1. Open the project in Android Studio.
2. Allow Gradle to sync.
3. Start an Android emulator or connect an Android device.
4. Click **Run** to launch the application.
5. Enter username **`admin`**.
6. Enter password **`1234`**.
7. Click **Login**.
8. Verify that the external browser opens the target website.
9. Enter incorrect credentials to verify the **`Login failed`** Toast message.

## 📚 Learning Objective

The objective of this practical is to understand how to create a login screen, validate username and password using conditional statements, display Toast messages, launch external applications using implicit Intents, and open web URLs using Android's **`Uri`** class.

**Note:** This application uses hardcoded demo credentials for educational purposes. It does not provide real authentication or secure user verification.

## 👩‍💻 Author

**Adima Zareen**
