# Android RelativeLayout - Login Activity

A simple Android application demonstrating how to create a login interface using **RelativeLayout** in Android.

## 📱 Description

This practical demonstrates how to design an Android user interface using `RelativeLayout` and position different UI components relative to each other.

The application contains a simple login screen with:

- A welcome title
- Username input field
- Password input field
- Login button

When the user clicks the **LOGIN** button, the application checks whether both the username and password fields are filled.

- If either field is empty, a Toast message displays **"Please enter both fields"**.
- If both fields are filled, a Toast message displays **"Welcome, username!"**.

## 🎯 Objective

The objective of this practical is to understand how to:

- Create an Android UI using `RelativeLayout`
- Position views relative to other views
- Use `TextView`, `EditText`, and `Button`
- Handle button click events
- Perform basic input validation
- Display messages using `Toast`

## 🛠️ Technologies Used

- Java
- XML
- Android Studio
- Android SDK
- RelativeLayout
- TextView
- EditText
- Button
- Toast
- OnClickListener

## 📂 Project Structure

```text
RelativeLayout/
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
            │   └── com/example/relativelayout/
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

## 🖥️ User Interface

The login screen contains the following components:

| Component | ID | Purpose |
|---|---|---|
| TextView | `titleText` | Displays the welcome title |
| EditText | `usernameInput` | Accepts the username |
| EditText | `passwordInput` | Accepts the password |
| Button | `loginButton` | Handles the login action |

## 📐 RelativeLayout

`RelativeLayout` is a `ViewGroup` that allows UI components to be positioned relative to the parent layout or relative to other views.

The main layout is:

```xml
<RelativeLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:padding="16dp"
    android:background="#F5F5F5">

</RelativeLayout>
```

## 📌 RelativeLayout Attributes Used

### `layout_centerHorizontal`

The title and Login button are centered horizontally:

```xml
android:layout_centerHorizontal="true"
```

### `layout_below`

The username field is placed below the title:

```xml
android:layout_below="@id/titleText"
```

The password field is placed below the username field:

```xml
android:layout_below="@id/usernameInput"
```

The Login button is placed below the password field:

```xml
android:layout_below="@id/passwordInput"
```

### `layout_marginTop`

Top margins are used to create spacing between the UI components:

```xml
android:layout_marginTop="20dp"
```

## 📝 Username Input

The username is entered using an `EditText`:

```xml
<EditText
    android:id="@+id/usernameInput"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:hint="Enter your username"
    android:layout_below="@id/titleText"
    android:layout_marginTop="20dp" />
```

## 🔒 Password Input

The password is entered using an `EditText`.

The `textPassword` input type hides the entered password:

```xml
<EditText
    android:id="@+id/passwordInput"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:hint="Enter your password"
    android:inputType="textPassword"
    android:layout_below="@id/usernameInput"
    android:layout_marginTop="16dp" />
```

## 🔘 Login Button

The Login button is positioned below the password field and centered horizontally:

```xml
<Button
    android:id="@+id/loginButton"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:layout_below="@id/passwordInput"
    android:layout_centerHorizontal="true"
    android:layout_marginTop="24dp"
    android:background="#FF0000"
    android:text="Login"
    android:textColor="#FF000000" />
```

## 💻 MainActivity.java

The UI components are connected to the Java activity using `findViewById()`:

```java
usernameInput = findViewById(R.id.usernameInput);
passwordInput = findViewById(R.id.passwordInput);
loginButton = findViewById(R.id.loginButton);
```

The Login button uses an `OnClickListener`:

```java
loginButton.setOnClickListener(v -> {

    String username = usernameInput.getText().toString();
    String password = passwordInput.getText().toString();

    if (username.isEmpty() || password.isEmpty()) {

        Toast.makeText(
            MainActivity.this,
            "Please enter both fields",
            Toast.LENGTH_SHORT
        ).show();

    } else {

        Toast.makeText(
            MainActivity.this,
            "Welcome, " + username + "!",
            Toast.LENGTH_SHORT
        ).show();

    }
});
```

## ✅ Input Validation

The application checks whether the username or password is empty:

```java
if (username.isEmpty() || password.isEmpty()) {
    // Display error message
}
```

If either field is empty, the following Toast message is displayed:

```text
Please enter both fields
```

If both fields are filled, the username is included in the success message:

```text
Welcome, Adima!
```

## 🖼️ Expected Output

```text
┌──────────────────────────────────────────┐
│                                          │
│         Welcome to Adima's App           │
│                                          │
│  ┌────────────────────────────────────┐  │
│  │ Enter your username                │  │
│  └────────────────────────────────────┘  │
│                                          │
│  ┌────────────────────────────────────┐  │
│  │ Enter your password                │  │
│  └────────────────────────────────────┘  │
│                                          │
│             ┌──────────────┐             │
│             │     LOGIN    │             │
│             └──────────────┘             │
│                                          │
└──────────────────────────────────────────┘
```

## ▶️ How to Run

1. Open the project in **Android Studio**.
2. Allow Gradle to sync completely.
3. Connect an Android device or start an Android Emulator.
4. Click **Run ▶**.
5. The RelativeLayout login screen will appear.
6. Enter a username.
7. Enter a password.
8. Click the **LOGIN** button.
9. The appropriate Toast message will be displayed.

## 📚 Learning Outcomes

After completing this practical, the student will understand:

- The purpose of `RelativeLayout`.
- How to position views relative to other views.
- How to use `layout_below`.
- How to use `layout_centerHorizontal`.
- How to create input fields using `EditText`.
- How to handle button clicks using `OnClickListener`.
- How to perform basic input validation.
- How to display messages using `Toast`.

## 👩‍💻 Author

**Adima**
