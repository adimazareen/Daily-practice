<?php
// Check if cookies are set
if (isset($_COOKIE["username"]) && isset($_COOKIE["role"])) {
    echo "Username: " . $_COOKIE["username"] . "<br>";
    echo "Role: " . $_COOKIE["role"] . "<br>";
} else {
    echo "Cookies are not set or have expired.<br>";
}

// Optional: Add a link to go back to the main page
echo "<a href='cookie.php'>Go Back</a>";
?>
