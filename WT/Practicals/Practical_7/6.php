<!DOCTYPE html>
<html>
<head>
    <title>Create Table</title>
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
        input[type="number"] {
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
        <h2>Create Table</h2>
        <form method="post">
            <input type="text" name="table_name" placeholder="Enter table name" required><br>
            <input type="number" name="num_fields" placeholder="Number of fields" min="1" required><br>
            <?php
            // Display input fields for field names
            if ($_SERVER["REQUEST_METHOD"] == "POST") {
                $num_fields = $_POST['num_fields'];
                for ($i = 1; $i <= $num_fields; $i++) {
                    echo "<input type='text' name='field_name_$i' placeholder='Field $i Name' required><br>";
                }
            }
            ?>
            <input type="submit" name="submit" value="Create Table">
        </form>

        <?php
        if ($_SERVER["REQUEST_METHOD"] == "POST") {
            // Retrieve table name and number of fields from form submission
            $table_name = $_POST['table_name'];
            $num_fields = $_POST['num_fields'];

            // Construct SQL query to create the table
            $sql = "CREATE TABLE $table_name (";
            for ($i = 1; $i <= $num_fields; $i++) {
                $field_name = $_POST["field_name_$i"];
                $sql .= "$field_name VARCHAR(255) NOT NULL";
                if ($i < $num_fields) {
                    $sql .= ",";
                }
            }
            $sql .= ")";

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

            // Execute SQL query to create the table
            if ($conn->query($sql) === TRUE) {
                echo "<div class='message'>Table '$table_name' created successfully.</div>";
            } else {
                echo "<div class='message'>Error creating table: " . $conn->error . "</div>";
            }

            // Close connection
            $conn->close();
        }
        ?>
    </div>
</body>
</html>
