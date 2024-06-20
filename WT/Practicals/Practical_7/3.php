<!DOCTYPE html>
<html>
<head>
    <title>Create Customer Table</title>
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
        .message {
            margin-top: 20px;
            text-align: center;
        }
    </style>
</head>
<body>
    <div id="container">
        <h2>Create Customer Table</h2>

        <?php
        // Connect to MySQL server
        $servername = "localhost"; // Change this if MySQL server is running on a different host
        $username = "root"; // Your MySQL username
        $password = ""; // Your MySQL password
        $database = "WT_P7"; // Your MySQL database name

        $conn = new mysqli($servername, $username, $password, $database);

        // Check connection
        if ($conn->connect_error) {
            die("Connection failed: " . $conn->connect_error);
        }

        // SQL query to create customer table
        $sql = "CREATE TABLE Customer (
            C_Id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
            C_name VARCHAR(50) NOT NULL,
            Name_Item_purchased VARCHAR(100) NOT NULL,
            review_product TEXT
        )";

        if ($conn->query($sql) === TRUE) {
            echo "<div class='message'>Customer table created successfully.</div>";
        } else {
            echo "<div class='message'>Error creating customer table: " . $conn->error . "</div>";
        }

        // Close connection
        $conn->close();
        ?>
    </div>
</body>
</html>
