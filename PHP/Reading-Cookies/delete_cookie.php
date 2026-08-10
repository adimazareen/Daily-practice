<?php
// Delete the cookies by setting their expiration time in the past
setcookie("username", "", time() - 3600, "/");
setcookie("role", "", time() - 3600, "/");

echo "Cookies deleted! <a href='read_cookie.php'>Check Again</a>";
?>
