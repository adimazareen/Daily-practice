# Android Login Application

A simple Android application demonstrating username and password validation, login authentication, and navigation to a welcome screen displaying the username.

## 📱 Description

This application demonstrates how to create a basic Android login application using XML and Java.

The application provides:

- A username input field
- A password input field with hidden characters
- A Submit button to validate login credentials
- A Toast message displaying "Login Failed" when credentials are incorrect
- Navigation to the Home screen when login is successful
- A welcome message displaying the logged-in username

A `ConstraintLayout` is used as the root layout for both screens. `EditText` components collect the username and password, while a `Button` triggers validation. An explicit `Intent` passes the username from `MainActivity` to `HomeActivity`.

**Demo Credentials:**

- Username: `admin`
- Password: `1234`

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
- AppCompat
- Android Activity Lifecycle

## 📂 Project Structure

```text
LoginScreenApp/
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
            │   └── com/bcs/loginscreen_2/
            │       ├── MainActivity.java
            │       └── HomeActivity.java
            │
            └── res/
                ├── layout/
                │   ├── activity_main.xml
                │   └── activity_home.xml
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

`ConstraintLayout` is used as the main layout for the login and welcome screens.

```xml
<androidx.constraintlayout.widget.ConstraintLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:layout_width="match_parent"
    android:layout_height="match_parent">
</androidx.constraintlayout.widget.ConstraintLayout>
```

### 2. EditText

`EditText` is used to accept the username and password entered by the user.

Username input:

```xml
<EditText
    android:id="@+id/etUsername"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:hint="Enter username"
    android:inputType="text" />
```

Password input:

```xml
<EditText
    android:id="@+id/etPassword"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:hint="Enter password"
    android:inputType="textPassword" />
```

The `textPassword` input type hides the password characters while typing.

### 3. Button and Click Listener

A Submit button is used to check the entered credentials.

```java
btnLogin.setOnClickListener(new View.OnClickListener() {
    @Override
    public void onClick(View v) {
        // Validate login credentials
    }
});
```

The click listener executes the login validation code when the user presses the button.

### 4. Username and Password Validation

The entered username and password are checked using an `if-else` statement.

```java
String user = etUsername.getText().toString().trim();
String pass = etPassword.getText().toString();

if (user.equals("admin") && pass.equals("1234")) {
    // Login successful
} else {
    // Login failed
}
```

The `&&` operator ensures that both the username and password must match.

### 5. Toast Message

A Toast displays a short message when login fails.

```java
Toast.makeText(
    MainActivity.this,
    "Login Failed",
    Toast.LENGTH_SHORT
).show();
```

The message appears when the user enters incorrect credentials.

### 6. Intent

An explicit `Intent` is used to navigate from `MainActivity` to `HomeActivity`.

```java
Intent i = new Intent(
    MainActivity.this,
    HomeActivity.class
);

i.putExtra("username", user);
startActivity(i);
```

The `putExtra()` method sends the username to the next activity.

### 7. Receiving Data from Intent

The Home screen receives the username using `getStringExtra()`.

```java
String username = getIntent().getStringExtra("username");

txtWelcome.setText("Welcome, " + username + "!");
```

If the entered username is `admin`, the Home screen displays:

```text
Welcome, admin!
```

### 8. AndroidManifest.xml

Both activities must be declared in `AndroidManifest.xml`.

The `MainActivity` is configured as the launcher activity, while `HomeActivity` opens after successful login.

```xml
<activity
    android:name=".HomeActivity"
    android:exported="false" />

<activity
    android:name=".MainActivity"
    android:exported="true">

    <intent-filter>
        <action android:name="android.intent.action.MAIN" />
        <category android:name="android.intent.category.LAUNCHER" />
    </intent-filter>

</activity>
```

## 🖼️ Expected Output

### Login Screen

```text
┌──────────────────────────────────┐
│                                  │
│                                  │
│  Username       [ admin       ]  │
│                                  │
│  Password       [ ••••        ]  │
│                                  │
│              [ Submit ]          │
│                                  │
└──────────────────────────────────┘
```

### Successful Login

```text
┌──────────────────────────────────┐
│                                  │
│                                  │
│                                  │
│          Welcome, admin!         │
│                                  │
│                                  │
└──────────────────────────────────┘
```

### Failed Login

```text
┌──────────────────────────────────┐
│                                  │
│  Username       [ user        ]  │
│  Password       [ ****        ]  │
│                                  │
│              [ Submit ]          │
│                                  │
│          Login Failed            │
└──────────────────────────────────┘
```

## ▶️ How to Run

1. Open the project in Android Studio.
2. Allow Gradle to sync successfully.
3. Start an Android emulator or connect an Android device.
4. Click **Run** to launch the application.
5. Enter username `admin` and password `1234`.
6. Click **Submit** to navigate to the Home screen.
7. Verify that the welcome message displays `Welcome, admin!`.
8. Enter incorrect credentials to verify the `Login Failed` Toast message.

## 📚 Learning Objective

The objective of this practical is to understand how to create a basic Android login application using Java and XML, validate user credentials using conditional statements, display Toast messages, navigate between activities using explicit Intents, and transfer data from one activity to another.

**Note:** This application uses hardcoded credentials for educational purposes. Real-world applications should validate credentials securely using a backend authentication system.

## 👩‍💻 Author

**Adima Zareen**
