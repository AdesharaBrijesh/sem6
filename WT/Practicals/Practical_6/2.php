<!DOCTYPE html>
<html>
<head>
    <title>File Upload Form</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        #container {
            background-color: #fff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
            width: 400px;
        }
        h2 {
            text-align: center;
        }
        input[type="file"] {
            width: 100%;
            padding: 10px;
            margin: 8px 0;
            box-sizing: border-box;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        input[type="submit"] {
            background-color: #4CAF50;
            color: white;
            padding: 14px 20px;
            margin: 8px 0;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            width: 100%;
        }
        input[type="submit"]:hover {
            background-color: #45a049;
        }
        .error {
            color: red;
            font-size: 12px;
        }
        .success {
            color: green;
            font-size: 14px;
            font-weight: bold;
            text-align: center;
        }
    </style>
</head>
<body>
    <div id="container">
        <h2>File Upload Form</h2>
        <form method="post" enctype="multipart/form-data">
            <input type="file" name="uploaded_file" required><br>
            <input type="submit" name="submit" value="Upload File">
        </form>

        <?php
        if ($_SERVER["REQUEST_METHOD"] == "POST") {
            // Check if file is uploaded successfully
            if (isset($_FILES["uploaded_file"]) && $_FILES["uploaded_file"]["error"] == UPLOAD_ERR_OK) {
                $uploaded_file_name = $_FILES["uploaded_file"]["name"];
                $uploaded_file_tmp = $_FILES["uploaded_file"]["tmp_name"];
                $uploaded_file_size = $_FILES["uploaded_file"]["size"];
                $uploaded_file_type = $_FILES["uploaded_file"]["type"];

                // Validate file type
                $allowed_types = array("image/jpeg", "image/png", "image/gif", "application/pdf");
                if (!in_array($uploaded_file_type, $allowed_types)) {
                    echo "<p class='error'>Error: Only JPG, PNG, GIF, or PDF files are allowed.</p>";
                    exit;
                }

                // Validate file size (limit to 5MB)
                $max_file_size = 5 * 1024 * 1024; // 5MB in bytes
                if ($uploaded_file_size > $max_file_size) {
                    echo "<p class='error'>Error: File size exceeds the maximum limit of 5MB.</p>";
                    exit;
                }

                // Move the uploaded file to a secure location
                $upload_dir = "uploads/";
                $destination_file = $upload_dir . basename($uploaded_file_name);
                if (move_uploaded_file($uploaded_file_tmp, $destination_file)) {
                    echo "<p class='success'>File uploaded successfully.</p>";
                } else {
                    echo "<p class='error'>Error: Failed to move the uploaded file.</p>";
                }
            } else {
                echo "<p class='error'>Error: No file uploaded or an error occurred during upload.</p>";
            }
        }
        ?>
    </div>
</body>
</html>
