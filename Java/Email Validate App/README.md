# Android Email Validation Login App

A simple Android application demonstrating email validation, password checking, and login authentication using Java and XML.

## 📱 Description

This application demonstrates how to create a login screen that accepts an email address and password, validates the email format, and displays a Toast message based on the login result.

The application provides:

- An email input field
- A password input field with hidden characters
- Real-time email format validation
- A Login button that becomes enabled when the email format is valid
- A successful login Toast message for correct credentials
- An error Toast message for incorrect credentials

**Demo Credentials:**

- Email: **`admin@gmail.com`**
- Password: **`1234`**

The application uses **`ConstraintLayout`** to arrange the UI components and Android's **`Patterns.EMAIL_ADDRESS`** to validate the email format.

## 🛠️ Technologies Used

- Java
- XML
- Android Studio
- ConstraintLayout
- EditText
- TextView
- Button
- Toast
- TextWatcher
- Patterns.EMAIL_ADDRESS
- AppCompat
- Edge-to-Edge UI

## 📂 Project Structure

```text
EmailValidateApp/
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
            │   └── com/bcs/email_validate_3/
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

**`ConstraintLayout`** is used to arrange the email field, password field, and Login button on the screen.

```xml
<androidx.constraintlayout.widget.ConstraintLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:layout_width="match_parent"
    android:layout_height="match_parent">
</androidx.constraintlayout.widget.ConstraintLayout>
```

### 2. EditText

**`EditText`** accepts the email address and password entered by the user.

**Email input:**

```xml
<EditText
    android:id="@+id/etEmail"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:hint="Email"
    android:inputType="textEmailAddress" />
```

**Password input:**

```xml
<EditText
    android:id="@+id/etPassword"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:hint="Password"
    android:inputType="textPassword" />
```

The **`textEmailAddress`** input type provides an email-friendly keyboard, while **`textPassword`** hides the password characters.

### 3. Email Validation

Android's **`Patterns.EMAIL_ADDRESS`** is used to check whether the entered text matches a typical email address format.

```java
if (Patterns.EMAIL_ADDRESS.matcher(email).matches()) {
    btnLogin.setEnabled(true);
} else {
    btnLogin.setEnabled(false);
}
```

The Login button is enabled only when the email format is valid.

### 4. TextWatcher

**`TextWatcher`** monitors changes in the email field and performs validation while the user types.

```java
etEmail.addTextChangedListener(new TextWatcher() {

    @Override
    public void beforeTextChanged(
            CharSequence s, int start, int count, int after) {
    }

    @Override
    public void onTextChanged(
            CharSequence email, int start, int before, int count) {

        boolean isValid =
                Patterns.EMAIL_ADDRESS.matcher(email).matches();

        btnLogin.setEnabled(isValid);
    }

    @Override
    public void afterTextChanged(Editable s) {
    }
});
```

### 5. Login Authentication

The application compares the entered email and password with the demo credentials.

```java
if (email.equals("admin@gmail.com")
        && pass.equals("1234")) {

    // Login successful

} else {

    // Invalid credentials
}
```

Both conditions must be true for the login to succeed.

### 6. Toast Messages

A Toast displays a short message indicating whether the login was successful.

**Successful login:**

```java
Toast.makeText(
    MainActivity.this,
    "Login Successful",
    Toast.LENGTH_SHORT
).show();
```

**Unsuccessful login:**

```java
Toast.makeText(
    MainActivity.this,
    "Invalid Credentials",
    Toast.LENGTH_SHORT
).show();
```

### 7. Button Click Listener

The Login button performs the authentication check when clicked.

```java
btnLogin.setOnClickListener(view -> {

    String email = etEmail.getText().toString().trim();
    String pass = etPassword.getText().toString();

    if (email.equals("admin@gmail.com")
            && pass.equals("1234")) {

        // Show successful login message

    } else {

        // Show invalid credentials message
    }
});
```

## 🖼️ Expected Output

### Login Screen

```text
┌──────────────────────────────────┐
│                                  │
│                                  │
│  Email     admin@gmail.com       │
│            ─────────────────     │
│                                  │
│  Password  ••••                  │
│            ─────────────────     │
│                                  │
│             [ Login ]            │
│                                  │
│                                  │
└──────────────────────────────────┘
```

### Successful Login

Enter:

- Email: `admin@gmail.com`
- Password: `1234`

Toast message:

```text
Login Successful
```

### Unsuccessful Login

Enter an incorrect email/password combination, or use a valid-format email with the wrong password.

Toast message:

```text
Invalid Credentials
```

An invalid email format keeps the Login button disabled.

## ▶️ How to Run

1. Open the project in Android Studio.
2. Allow Gradle to sync.
3. Start an Android emulator or connect an Android device.
4. Click **Run**.
5. Enter `admin@gmail.com` in the email field.
6. Enter `1234` in the password field.
7. Click **Login**.
8. Verify the `Login Successful` Toast message.
9. Try incorrect credentials to verify the **`Invalid Credentials`** Toast message.

## 📚 Learning Objective

The objective of this practical is to understand how to create an Android login form, validate email addresses using **`Patterns.EMAIL_ADDRESS`**, monitor text changes using **`TextWatcher`**, check credentials using conditional statements, and display Toast messages.

**Note:** This application uses hardcoded demo credentials. Email format validation does not verify that an email address exists. Real applications should authenticate users securely through a backend or authentication provider.

## 👩‍💻 Author

**Adima Zareen**
