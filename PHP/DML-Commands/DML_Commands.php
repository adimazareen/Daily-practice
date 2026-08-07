<?php
include "db_connect.php";

// Show all PHP errors for debugging
error_reporting(E_ALL);
ini_set('display_errors', 1);

// --- INSERT DATA ---
if (isset($_POST['insert'])) {
    $name = $conn->real_escape_string($_POST['name']);
    $email = $conn->real_escape_string($_POST['email']);
    $age = intval($_POST['age']);
    $course = $conn->real_escape_string($_POST['course']);

    $sql = "INSERT INTO Students (name, email, age, course) 
            VALUES ('$name', '$email', $age, '$course')";

    if ($conn->query($sql) === TRUE) {
        // Redirect to refresh table
        header("Location: DML_Commands.php");
        exit();
    } else {
        echo "Error inserting record: " . $conn->error . "<br>";
    }
}

// --- UPDATE DATA ---
if (isset($_POST['update'])) {
    $id = intval($_POST['id']);
    $course = $conn->real_escape_string($_POST['course']);

    $sql = "UPDATE Students SET course='$course' WHERE id=$id";

    if ($conn->query($sql) === TRUE) {
        header("Location: DML_Commands.php");
        exit();
    } else {
        echo "Error updating record: " . $conn->error . "<br>";
    }
}

// --- DELETE DATA ---
if (isset($_POST['delete'])) {
    $id = intval($_POST['id']);

    $sql = "DELETE FROM Students WHERE id=$id";

    if ($conn->query($sql) === TRUE) {
        header("Location: DML_Commands.php");
        exit();
    } else {
        echo "Error deleting record: " . $conn->error . "<br>";
    }
}

// --- DISPLAY ALL STUDENTS ---
$result = $conn->query("SELECT * FROM Students");

if ($result->num_rows > 0) {
    echo "<table border='1' cellpadding='10'> 
            <tr> 
                <th>ID</th><th>Name</th><th>Email</th><th>Age</th><th>Course</th> 
            </tr>";
    while ($row = $result->fetch_assoc()) {
        echo "<tr> 
                <td>".$row['id']."</td>
                <td>".$row['name']."</td>
                <td>".$row['email']."</td>
                <td>".$row['age']."</td>
                <td>".$row['course']."</td>
              </tr>";
    }
    echo "</table>";
} else {
    echo "No records found!";
}

$conn->close();
?>
