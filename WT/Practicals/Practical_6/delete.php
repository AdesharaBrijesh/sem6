<?php
// File to be deleted
$file = $_GET['file'];

// Path to the file
$file_path = "uploads/" . $file;

// Check if the file exists
if (file_exists($file_path)) {
    // Delete the file
    if (unlink($file_path)) {
        echo "File deleted successfully.";
    } else {
        echo "Error: Failed to delete file.";
    }
} else {
    // File not found
    echo "Error: File not found.";
}
?>
