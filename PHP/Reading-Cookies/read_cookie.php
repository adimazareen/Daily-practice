<?php 
// Read the cookies 
if(isset($_COOKIE["username"]) && isset($_COOKIE["role"])) { 
echo "Welcome, " . $_COOKIE["username"] . "!<br>"; 
echo "Your role is: " . $_COOKIE["role"] . "<br>"; 
} else { 
echo "No cookies found!<br>"; 
} 
echo "<a href='delete_cookie.php'>Delete Cookies</a>"; 
?>
