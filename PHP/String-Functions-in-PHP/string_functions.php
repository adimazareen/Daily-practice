<?php 
include "db_connect.php"; 

echo "<h2>String Functions Results</h2>";

// 1️⃣ Convert first student's name to uppercase
$sql1 = "SELECT UPPER(name) AS upper_name FROM Students LIMIT 1"; 
$result1 = $conn->query($sql1); 
$row1 = $result1->fetch_assoc(); 
echo "<h3>UPPER(): " . $row1['upper_name'] . "</h3>"; 

// 2️⃣ Convert one student's course to lowercase
$sql2 = "SELECT LOWER(course) AS lower_course FROM Students LIMIT 1"; 
$result2 = $conn->query($sql2); 
$row2 = $result2->fetch_assoc(); 
echo "<h3>LOWER(): " . $row2['lower_course'] . "</h3>"; 

// 3️⃣ Find the length of the first student's name
$sql3 = "SELECT name, LENGTH(name) AS name_length FROM Students LIMIT 1"; 
$result3 = $conn->query($sql3); 
$row3 = $result3->fetch_assoc(); 
echo "<h3>LENGTH(): " . $row3['name'] . " → " . $row3['name_length'] . " characters</h3>"; 

// 4️⃣ Display a substring of the first student's course (first 4 letters)
$sql4 = "SELECT course, SUBSTRING(course, 1, 4) AS short_course FROM Students LIMIT 1"; 
$result4 = $conn->query($sql4); 
$row4 = $result4->fetch_assoc(); 
echo "<h3>SUBSTRING(): " . $row4['course'] . " → " . $row4['short_course'] . "</h3>"; 

$conn->close(); 
?>
