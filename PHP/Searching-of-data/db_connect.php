<?php 
// Database connection 
$servername = $_ENV['servername']; 
$username = $_ENV['username']; 
$password = $_ENV['password']; 
$dbname = $_ENV['dbname']; 
$port = $_ENV['port']; 

// Create connection 
$conn = new mysqli($servername, $username, $password, $dbname, $port); 

// Check connection 
if ($conn->connect_error) { 
    die("Connection failed: " . $conn->connect_error); 
} 

// SQL query to create table with constraints 
// Optional: Create table if it doesn't exist
$sql = "CREATE TABLE IF NOT EXISTS Students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    age INT CHECK(age >= 18),
    course VARCHAR(50) DEFAULT 'PHP'
)";
$conn->query($sql);
?>
