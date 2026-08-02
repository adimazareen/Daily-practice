<?php
include "db_connect.php";

echo "<h2>Numeric Functions Results</h2>";

// 1️⃣ ABS - absolute value of the first student's age difference from 20
$sql1 = "SELECT age, ABS(age - 20) AS abs_val, name FROM Students LIMIT 1";
$result1 = $conn->query($sql1);
$row1 = $result1->fetch_assoc();
echo "<h3>ABS(): |{$row1['age']} - 20| for {$row1['name']} → " . $row1['abs_val'] . "</h3>";

// 2️⃣ POWER - square of the first student's age
$sql2 = "SELECT age, POWER(age, 2) AS pow_val, name FROM Students LIMIT 1";
$result2 = $conn->query($sql2);
$row2 = $result2->fetch_assoc();
echo "<h3>POWER(): {$row2['name']}'s age^2 → " . $row2['pow_val'] . "</h3>";

// 3️⃣ ROUND - round the average age to nearest integer
$sql3 = "SELECT ROUND(AVG(age), 0) AS round_val FROM Students";
$result3 = $conn->query($sql3);
$row3 = $result3->fetch_assoc();
echo "<h3>ROUND(): Average age rounded → " . $row3['round_val'] . "</h3>";

// 4️⃣ MOD - modulus of first student's age by 5
$sql4 = "SELECT age, MOD(age, 5) AS mod_val, name FROM Students LIMIT 1";
$result4 = $conn->query($sql4);
$row4 = $result4->fetch_assoc();
echo "<h3>MOD(): {$row4['name']}'s age % 5 → " . $row4['mod_val'] . "</h3>";

$conn->close();
?>
