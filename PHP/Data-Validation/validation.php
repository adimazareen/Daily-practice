<?php
// Initialize variables
$nameErr = $emailErr = $ageErr = "";
$name = $email = $age = "";

// Check if form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {

    // Validate Name
    if (empty($_POST["name"])) {
        $nameErr = "Name is required";
    } elseif (!preg_match("/^[a-zA-Z ]*$/", $_POST["name"])) {
        $nameErr = "Only letters and spaces allowed";
    } else {
        $name = $_POST["name"];
    }

    // Validate Email
    if (empty($_POST["email"])) {
        $emailErr = "Email is required";
    } elseif (!filter_var($_POST["email"], FILTER_VALIDATE_EMAIL)) {
        $emailErr = "Invalid email format";
    } else {
        $email = $_POST["email"];
    }

    // Validate Age
    if (empty($_POST["age"])) {
        $ageErr = "Age is required";
    } elseif (!filter_var($_POST["age"], FILTER_VALIDATE_INT)) {
        $ageErr = "Age must be a number";
    } elseif ($_POST["age"] < 18) {
        $ageErr = "Age must be at least 18";
    } else {
        $age = $_POST["age"];
    }

    // Display the result
    echo "<h2>Form Submission Result</h2>";

    if ($nameErr || $emailErr || $ageErr) {
        // Show errors
        echo "<p style='color:red;'>Please fix the following errors:</p>";
        echo $nameErr ? "Name: $nameErr<br>" : "";
        echo $emailErr ? "Email: $emailErr<br>" : "";
        echo $ageErr ? "Age: $ageErr<br>" : "";
        echo "<br><a href='validation.html'>Go back to form</a>";
    } else {
        // Show success message
        echo "<h3>Form Submitted Successfully!</h3>";
        echo "Name: $name <br>";
        echo "Email: $email <br>";
        echo "Age: $age <br>";
        echo "<br><a href='validation.html'>Submit another response</a>";
    }
} else {
    // Redirect to form if accessed directly
    header("Location: validation.html");
    exit();
}
?>
