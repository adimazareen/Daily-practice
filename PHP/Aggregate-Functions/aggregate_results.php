<?php 
include "db_connect.php"; 

echo "<h2>Aggregate Function Results</h2>";

// 1. COUNT - total number of students 
$sql1 = "SELECT COUNT(*) AS total_students FROM Students"; 
$result1 = $conn->query($sql1); 
$row1 = $result1->fetch_assoc(); 
echo "<h3>Total Students: " . $row1['total_students'] . "</h3>"; 

// 2. AVG - average age of students 
$sql2 = "SELECT AVG(age) AS avg_age FROM Students"; 
$result2 = $conn->query($sql2); 
$row2 = $result2->fetch_assoc(); 
echo "<h3>Average Age: " . round($row2['avg_age'],2) . "</h3>"; 

// 3. SUM - total of all ages 
$sql3 = "SELECT SUM(age) AS total_age FROM Students"; 
$result3 = $conn->query($sql3); 
$row3 = $result3->fetch_assoc(); 
echo "<h3>Sum of Ages: " . $row3['total_age'] . "</h3>"; 

// 4. MIN - youngest student age 
$sql4 = "SELECT MIN(age) AS min_age FROM Students"; 
$result4 = $conn->query($sql4); 
$row4 = $result4->fetch_assoc(); 
echo "<h3>Youngest Age: " . $row4['min_age'] . "</h3>"; 

// 5. MAX - oldest student age 
$sql5 = "SELECT MAX(age) AS max_age FROM Students"; 
$result5 = $conn->query($sql5); 
$row5 = $result5->fetch_assoc(); 
echo "<h3>Oldest Age: " . $row5['max_age'] . "</h3>"; 

// 6. GROUP BY + COUNT (students per course) 
//$sql6 = "SELECT course_id, COUNT(*) AS total  
//FROM Students  
//GROUP BY course_id"; 
//$result6 = $conn->query($sql6); 

echo "<h3>Students per Course</h3>"; 
echo "<table border='1' cellpadding='10'> 
<tr><th>Course ID</th><th>Total Students</th></tr>"; 

//while($row6 = $result6->fetch_assoc()) { 
 //   echo "<tr><td>".$row6['course_id']."</td><td>".$row6['total']."</td></tr>"; 
//} 

echo "</table>"; 
$conn->close(); 
?>
