<?php
// Set cookies before any HTML output
setcookie("username", "Adima", time() + 3600, "/");  // expires in 1 hour
setcookie("role", "Developer", time() + 3600, "/");

// Redirect to cookie reading page
echo "Cookies have been set! <a href='read_cookie.php'>Go to Read Cookies</a>";
?>
