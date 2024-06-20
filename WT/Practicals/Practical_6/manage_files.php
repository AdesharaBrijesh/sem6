<!DOCTYPE html>
<html>
<head>
    <title>Manage Uploaded Files</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            margin: 0;
            padding: 20px;
        }
        h2 {
            text-align: center;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 20px;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #f2f2f2;
        }
        .actions {
            display: flex;
            justify-content: center;
        }
        .actions a {
            margin-right: 10px;
        }
    </style>
</head>
<body>
    <h2>Uploaded Files</h2>
    <?php
    // Directory where uploaded files are stored
    $upload_dir = "uploads/";

    // Check if the directory exists
    if (is_dir($upload_dir)) {
        // Open directory
        if ($dh = opendir($upload_dir)) {
            // Display table header
            echo "<table>";
            echo "<tr><th>Filename</th><th>Size</th><th>Actions</th></tr>";

            // Read files from the directory
            while (($file = readdir($dh)) !== false) {
                // Skip directories and hidden files
                if ($file != "." && $file != "..") {
                    // Get file size
                    $file_size = filesize($upload_dir . $file);

                    // Format file size
                    $size_units = array('B', 'KB', 'MB', 'GB', 'TB');
                    $size_index = 0;
                    while ($file_size >= 1024 && $size_index < count($size_units) - 1) {
                        $file_size /= 1024;
                        $size_index++;
                    }
                    $formatted_size = round($file_size, 2) . " " . $size_units[$size_index];

                    // Display file details in table rows
                    echo "<tr>";
                    echo "<td>$file</td>";
                    echo "<td>$formatted_size</td>";
                    echo "<td class='actions'><a href='uploads/$file' target='_blank'>View</a> <a href='download.php?file=$file'>Download</a> <a href='delete.php?file=$file'>Delete</a></td>";
                    echo "</tr>";
                }
            }

            // Close directory and table
            closedir($dh);
            echo "</table>";
        } else {
            echo "<p>Error: Unable to open directory.</p>";
        }
    } else {
        echo "<p>Error: Upload directory does not exist.</p>";
    }
    ?>
</body>
</html>
