<?php 
include "db_connect.php"; 

if (isset($_POST['search'])) { 
    $search = $_POST['search_term']; 
    $criteria = $_POST['criteria']; 

    // SQL query
    $sql = "SELECT * FROM Students WHERE $criteria LIKE '%$search%'"; 
    $result = $conn->query($sql); 

    echo "<h2>Search Results</h2>";

    if ($result && $result->num_rows > 0) { 
        echo "<table border='1' cellpadding='10'> 
                <tr> 
                    <th>ID</th><th>Name</th><th>Email</th><th>Age</th><th>Course</th> 
                </tr>"; 
        while($row = $result->fetch_assoc()) { 
            echo "<tr> 
                    <td>".$row["id"]."</td> 
                    <td>".$row["name"]."</td> 
                    <td>".$row["email"]."</td> 
                    <td>".$row["age"]."</td> 
                    <td>".$row["course"]."</td> 
                </tr>"; 
        } 
        echo "</table>"; 
    } else { 
        echo "<p>No matching records found.</p>"; 
    } 
} else {
    echo "<p>Please submit the form first from <a href='search_form.html'>here</a>.</p>";
}

$conn->close(); 
?>
