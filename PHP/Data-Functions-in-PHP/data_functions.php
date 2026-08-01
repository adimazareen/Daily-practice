<?php 
include "db_connect.php"; 
// Current date 
$sql1 = "SELECT CURDATE() AS today"; 
$result1 = $conn->query($sql1); 
$row1 = $result1->fetch_assoc(); 
echo "Today: " . $row1['today'] . "<br>"; 
// Current time 
$sql2 = "SELECT CURTIME() AS now_time"; 
$result2 = $conn->query($sql2); 
$row2 = $result2->fetch_assoc(); 
echo "Current Time: " . $row2['now_time'] . "<br>"; 
// Year from date 
$sql3 = "SELECT YEAR('2025-10-16') AS year_val"; 
$result3 = $conn->query($sql3); 
$row3 = $result3->fetch_assoc(); 
echo "YEAR: " . $row3['year_val'] . "<br>"; 
// Difference in days 
$sql4 = "SELECT DATEDIFF('2025-12-31','2025-10-16') AS days_diff"; 
$result4 = $conn->query($sql4); 
$row4 = $result4->fetch_assoc(); 
echo "Days until 31-Dec-2025: " . $row4['days_diff'] . "<br>"; 
$conn->close(); 
?> 
