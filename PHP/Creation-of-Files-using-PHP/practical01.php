<?php 
// File name 
$filename = "example.txt"; 
// 1. Create / Open the file for writing ("w" mode creates a new file or overwrites if exists) 
$file = fopen($filename, "w") or die("Unable to open file!"); 
// 2. Write content to the file 
fwrite($file, "Hello, this is my first file handling program in PHP.\n"); 
fwrite($file, "PHP makes working with files very easy!\n"); 
// 3. Close the file after writing 
fclose($file); 
// 4. Open the file for reading ("r" mode) 
$file = fopen($filename, "r") or die("Unable to open file!"); 
// 5. Read and display the file content 
echo "<h3>File Content:</h3>"; 
while (!feof($file)) { 
echo fgets($file) . "<br>"; 
} 
// 6. Close the file after reading 
fclose($file); 
?> 
