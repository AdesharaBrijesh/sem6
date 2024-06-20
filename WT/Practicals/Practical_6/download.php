<?php
// File to be downloaded
$file = $_GET['file'];

// Path to the file
$file_path = "uploads/" . $file;

// Check if the file exists
if (file_exists($file_path)) {
    // Set headers to force download
    header("Content-type: application/octet-stream");
    header("Content-Disposition: attachment; filename=\"$file\"");
    
    // Read the file and output its contents
    readfile($file_path);
    exit;
} else {
    // File not found
    echo "Error: File not found.";
}
?>
