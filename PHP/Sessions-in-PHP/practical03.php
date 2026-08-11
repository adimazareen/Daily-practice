<?php 
// Start the session 
session_start(); 
// Store session variables 
$_SESSION["username"] = "Adima"; 
$_SESSION["role"] = "Admin"; 
echo "Session variables are set.<br>"; 
echo "<a href='get_session.php'>Go to Next Page</a>"; 
?>
