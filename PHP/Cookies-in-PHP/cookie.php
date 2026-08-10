<?php 
// Create a cookie (valid for 1 hour) 
setcookie("username", "Adima", time() + 3600, "/"); 
setcookie("role", "Admin", time() + 3600, "/"); 
echo "Cookies are set.<br>"; 
echo "<a href='get_cookie.php'>Go to Next Page</a>"; 
?>
