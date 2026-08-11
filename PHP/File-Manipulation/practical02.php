<?php 
// File name 
$filename = "example.txt"; 
// 1. Create and write into the file 
$file = fopen($filename, "w") or die("Unable to open file!"); 
fwrite($file, "Hello, this is a simple file manipulation example in PHP.\n"); 
fwrite($file, "You can write multiple lines into the file.\n"); 
fclose($file); 
echo "File written successfully.<br>"; 
// 2. Read the file content 
$file = fopen($filename, "r") or die("Unable to open file!"); 
echo "<b>File Content:</b><br>"; 
while (!feof($file)) { 
echo fgets($file) . "<br>"; 
} 
fclose($file); 
// 3. Append data to the file 
$file = fopen($filename, "a") or die("Unable to open file!"); 
fwrite($file, "This line is appended at the end of the file.\n"); 
fclose($file); 
echo "Data appended successfully.<br>"; 
// 4. Read again after appending 
$file = fopen($filename, "r") or die("Unable to open file!"); 
echo "<b>Updated File Content:</b><br>"; 
while (!feof($file)) { 
echo fgets($file) . "<br>"; 
} 
fclose($file); 
?> 
