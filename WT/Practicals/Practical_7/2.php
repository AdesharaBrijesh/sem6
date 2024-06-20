<!DOCTYPE html>
<html>
<head>
    <title>Create Database</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            margin: 0;
            padding: 20px;
        }
        #container {
            background-color: #fff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
            width: 400px;
            margin: 0 auto;
        }
        input[type="text"] {
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
        .message {
            margin-top: 20px;
            text-align: center;
        }
    </style>
</head>
<body>
    <div id="container">
        <h2>Create Database</h2>
        <form method="post">
            <input type="text" name="database_name" placeholder="Enter database name" required><br>
            <input type="submit" name="submit" value="Create Database">
        </form>

        <?php
        if ($_SERVER["REQUEST_METHOD"] == "POST") {
            // Retrieve database name from form submission
            $database_name = $_POST['database_name'];

            // Connect to MySQL server
            $servername = "localhost"; // Change this if MySQL server is running on a different host
            $username = "root"; // Your MySQL username
            $password = ""; // Your MySQL password

            $conn = new mysqli($servername, $username, $password);

            // Check connection
            if ($conn->connect_error) {
                die("Connection failed: " . $conn->connect_error);
            }

            // Create the database
            $sql = "CREATE DATABASE $database_name";
            if ($conn->query($sql) === TRUE) {
                echo "<div class='message'>Database '$database_name' created successfully.</div>";
            } else {
                echo "<div class='message'>Error creating database: " . $conn->error . "</div>";
            }

            // Close connection
            $conn->close();
        }
        ?>
    </div>
</body>
</html>
