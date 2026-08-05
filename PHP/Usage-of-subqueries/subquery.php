<?php
include "db_connect.php";

if (isset($_POST['run'])) {
?>
<!DOCTYPE html>
<html>
<head>
    <title>Subquery Results</title>
</head>
<body>
    <h1>Subquery Results – Students Table</h1>

    <?php
    // 1️⃣ Students older than the average age
    $sql1 = "SELECT * FROM Students WHERE age > (SELECT AVG(age) FROM Students)";
    $result1 = $conn->query($sql1);

    echo "<h2>1. Students older than the average age</h2>";
    if ($result1 && $result1->num_rows > 0) {
        echo "<table border='1' cellpadding='10'>
                <tr><th>Name</th><th>Age</th></tr>";
        while ($row = $result1->fetch_assoc()) {
            echo "<tr><td>{$row['name']}</td><td>{$row['age']}</td></tr>";
        }
        echo "</table>";
    } else {
        echo "<p>No students found older than the average age.</p>";
    }

    // 2️⃣ Students enrolled in the same course as Alice
    $sql2 = "SELECT * FROM Students 
             WHERE course = (SELECT course FROM Students WHERE name='Alice' LIMIT 1)";
    $result2 = $conn->query($sql2);

    echo "<h2>2. Students in the same course as Alice</h2>";
    if ($result2 && $result2->num_rows > 0) {
        echo "<table border='1' cellpadding='10'>
                <tr><th>Name</th><th>Course</th></tr>";
        while ($row = $result2->fetch_assoc()) {
            echo "<tr><td>{$row['name']}</td><td>{$row['course']}</td></tr>";
        }
        echo "</table>";
    } else {
        echo "<p>No students found in the same course as Alice (check if 'Alice' exists in DB).</p>";
    }

    // 3️⃣ Students with maximum age
    $sql3 = "SELECT * FROM Students WHERE age = (SELECT MAX(age) FROM Students)";
    $result3 = $conn->query($sql3);

    echo "<h2>3. Oldest Student(s)</h2>";
    if ($result3 && $result3->num_rows > 0) {
        echo "<table border='1' cellpadding='10'>
                <tr><th>Name</th><th>Age</th></tr>";
        while ($row = $result3->fetch_assoc()) {
            echo "<tr><td>{$row['name']}</td><td>{$row['age']}</td></tr>";
        }
        echo "</table>";
    } else {
        echo "<p>No oldest student found (unexpected).</p>";
    }

    $conn->close();
    ?>

    <br>
    <a href="subquery_form.html">Back to Form</a>
</body>
</html>
<?php
} else {
    // If user tries to access PHP file directly
    echo "<p>Please run this from the <a href='subquery_form.html'>Subquery Form</a> page.</p>";
}
?>
