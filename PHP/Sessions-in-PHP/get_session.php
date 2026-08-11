<?php
// Start the session to access session variables
session_start();

// Check if session variables are set
if (isset($_SESSION["username"]) && isset($_SESSION["role"])) {
    echo "Username: " . $_SESSION["username"] . "<br>";
    echo "Role: " . $_SESSION["role"] . "<br>";
} else {
    echo "No session variables found.<br>";
}

// Optional: Add a link to go back to the main page
echo "<a href='practical03.php'>Go Back</a>";
?>
