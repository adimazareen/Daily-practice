<?php
include "db_connect.php";

// Default sorting
$orderBy = "id";
$order = "ASC";

// If user submitted form
if (isset($_POST['sort'])) {
    $orderBy = $_POST['orderby'];
    $order = $_POST['order'];
}

// Fetch data with sorting
$sql = "SELECT * FROM Students ORDER BY $orderBy $order";
$result = $conn->query($sql);
?>

<!DOCTYPE html>
<html>
<head>
    <title>Sorted Students</title>
</head>
<body>
    <h2>Sorted Student Records</h2>

    <form method="post" action="practical09.php">
        Sort By:
        <select name="orderby">
            <option value="id" <?php if($orderBy == 'id') echo 'selected'; ?>>ID</option>
            <option value="name" <?php if($orderBy == 'name') echo 'selected'; ?>>Name</option>
            <option value="email" <?php if($orderBy == 'email') echo 'selected'; ?>>Email</option>
            <option value="age" <?php if($orderBy == 'age') echo 'selected'; ?>>Age</option>
            <option value="course" <?php if($orderBy == 'course') echo 'selected'; ?>>Course</option>
        </select>

        Order:
        <select name="order">
            <option value="ASC" <?php if($order == 'ASC') echo 'selected'; ?>>Ascending</option>
            <option value="DESC" <?php if($order == 'DESC') echo 'selected'; ?>>Descending</option>
        </select>

        <input type="submit" name="sort" value="Sort">
    </form>

    <hr>

    <?php
    if ($result && $result->num_rows > 0) {
        echo "<table border='1' cellpadding='10'>
                <tr>
                    <th>ID</th><th>Name</th><th>Email</th><th>Age</th><th>Course</th>
                </tr>";
        while ($row = $result->fetch_assoc()) {
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
        echo "<p>No records found!</p>";
    }

    $conn->close();
    ?>

    <br>
    <a href="sort_form.html">Back to Sort Form</a>
</body>
</html>
